import json
import copy

from django.db import transaction

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import *
from base.serializers import *

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from datetime import datetime
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404



class CotacaoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Cotacao.objects.all()
    serializer_class = CotacaoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['code', 'id']

    def list(self, request):
        queryset = Cotacao.objects.all()
        serializer = self.serializer_class(
            self.filter_queryset(queryset), many=True)
        response = serializer.data

        #Implementando Paginacao
        paginator = Paginator(queryset, 20)
        page = request.GET.get("page", 1)
        queryset_paginado = paginator.get_page(page)
        serializer = self.serializer_class(queryset_paginado.object_list, many=True)

        #Logica para saber o numero de paginas
        total_paginas = queryset_paginado.paginator.num_pages
        next_page = queryset_paginado.number + 1
        atual_page = queryset_paginado.number
        previous_page = queryset_paginado.number

        #Logica para saber a proxima pagina e a pagina anterior

        if(next_page > total_paginas):
            next_page = next_page - 1
        if(previous_page > 0 and previous_page <= total_paginas):
            previous_page = previous_page - 1
            if(previous_page == 0):
                previous_page = previous_page + 1

        response = serializer.data
        return Response(response)
        #http://127.0.0.1:8000/cotacao/?page=

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        solicitacao = Cotacao.objects.get(id=response.data['id'])
        Fila(solicitacao=solicitacao, status='nova').save()
        return response
    
    def delete(self, request, train_id=None):
        route = get_object_or_404(Cotacao, pk=None)
        response = u'Sucesseful delete route {}'.format(route.display_name())
        route.delete()
        return response
    
    def retrieve(self, request, pk=None):
        queryset = Cotacao.objects.all()
        status = get_object_or_404(queryset, pk=pk)
        serializer = CotacaoSerializer(status)
        return Response(serializer.data)
        

class GetFirstSolicitacao(APIView):
    def get(self, request):
        """
        Endpoint que retorna a primeira solicitação com status 'nova'
        Lida com race condition, não deixando que em diferentes requisições seja retornada
        a mesma solicitação.
        """
        #   select_for_update bloqueia as linhas do queryset montado
        #   o parâmentro skip_locked=True não deixa que linhas bloqueadas sejam acessadas por outras requisições
        #   o slice [:1] não executa a query, apenas cria um novo queryset com o LIMIT, por exemplo
        qs_first = Fila.objects.select_for_update(skip_locked=True).filter(status='nova')[:1]
        #   uso do transaction.atomic() vai bloquear a linha selecionada na execução da query
        #   e vai liberar após o fim da transação, no nosso caso, estamos mudando o status
        #   essa linha também não será mais acessível por outra requisição
        with transaction.atomic():
            try:
                first_solicitacao = qs_first[0]
            except IndexError:
                robo_atendimento = request.headers['robo-id']
                return Response('Fila vazia.')
            first_solicitacao.robo_atendimento = request.headers['robo-id']
            first_solicitacao.status = 'andamento'
            first_solicitacao.save()
        serializer = CotacaoSerializer(instance=first_solicitacao.solicitacao)
        return Response(serializer.data)


class FilaViewSet(viewsets.ViewSet):
    queryset = Fila.objects.all()
    serializer_class = FilaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['solicitacao', 'status', 'robo_atendimento']

    def list(self, request):
        queryset = Fila.objects.all()
        serializer = self.serializer_class(
            self.filter_queryset(queryset), many=True)
        response = serializer.data
        return Response(response)

    def partial_update(self, request, code=None):
        atendimento = self.queyset.get(solicitacao__code=code)
        serializer = self.serializer_class(atendimento, data=request, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)