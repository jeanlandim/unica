from django.db import models

# Os serviços oferecidos pela clinica
class AppServicos(models.Model):
    servico = models.CharField(max_length=50)
    preco = models.FloatField()
    duracao = models.CharField(max_length=2)
    descricao = models.TextField()
# Agenda de disponibilidade dos serviços
class AppAgenda(models.Model):
    servico_id = models.ForeignKey('AppServicos',on_delete=models.CASCADE)
    horario = models.CharField(max_length=5)
# Textos do site
class AppTextos(models.Model):
    titulo = models.CharField(max_length=20)
    texto = models.TextField()
    pagina = models.CharField(max_length=20) # Página do site para determinado texto

    def __str__(self):
        return self.titulo



