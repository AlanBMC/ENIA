from django.db import models

# Create your models here.
class Pagina(models.Model):
    titulo = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.textos


class Usuario(models.Model):
    pagina =  models.ForeignKey(Pagina, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100, default='123')

class Caixa_de_texto(models.Model):
    textos = models.TextField()
    id_pg = models.ForeignKey(Pagina, on_delete=models.CASCADE)    
    date_added = models.DateTimeField(auto_now_add=True)

