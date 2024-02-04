from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    senha = models.TextField(max_length=100,)
    email = models.EmailField(unique=True,  null=True)


class Pagina(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='paginas', null=True)  # Adicionando related_name para acessar páginas de um usuário


class CaixaTextos(models.Model):
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE, related_name='caixas_textos')  # Adicionando related_name para acessar caixas de texto de uma página
    texto = models.TextField()
    datahora = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"Caixa de Texto da Página: {self.pagina.titulo}"
