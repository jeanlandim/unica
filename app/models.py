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

    class Meta:
        verbose_name="Texto do Site"
        verbose_name_plural="Textos do Site"

    def __str__(self):
        return self.titulo



