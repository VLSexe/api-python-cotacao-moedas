from django.db import models
from django.contrib.postgres.fields import JSONField



class Cotacao(models.Model):
    code = models.CharField(max_length=11)
    parametros = models.JSONField()
    #status = models.CharField(max_length=25)
    created_on = models.DateTimeField('Solicitacao criada em', auto_now_add = True, editable = False)

    def __str__(self):
        return self.code


class Fila(models.Model):
    solicitacao = models.ForeignKey(Cotacao, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=25)
    robo_atendimento = models.IntegerField(null=True)
    created_on = models.DateTimeField('Registro criado em', auto_now_add = True, editable = False)
    modified_on = models.DateTimeField('Registro modificado em', auto_now=True, editable=False)

    def __str__(self):
        return self.solicitacao.code


#segunda página, adicionar solicitações que foram atendidas com status de atendimento.
#class CotacaoAtualizada(models.Model):
#    solicitacao = models.ForeignKey(Cotacao, on_delete=models.DO_NOTHING)
#    robo_atendimento = models.ForeignKey(Fila, on_delete=models.DO_NOTHING)
#    status_atendimento