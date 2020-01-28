from django.db import models

# Os serviços oferecidos pela clinica
class AppServicos(models.Model):
    servico = models.CharField(max_length=50)
    preco = models.FloatField()
    duracao = models.CharField(max_length=2)
    descricao = models.CharField(max_length=130)
# Agenda de disponibilidade dos serviços
class AppAgenda(models.Model):
    servico_id = models.ForeignKey('AppServicos',on_delete=models.CASCADE)
    horario = models.CharField(max_length=5)
