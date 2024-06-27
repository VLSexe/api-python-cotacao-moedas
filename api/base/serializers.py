from rest_framework import serializers

from base.models import *



class CotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotacao
        fields = '__all__' 


class FilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fila
        fields = '__all__' 