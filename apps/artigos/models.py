from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()

    def get_autor(self):
        return Autor.id # type: ignore
    
    def __str__(self):
        return f"{self.user.username}"

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.FileField(blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='artigos')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo}"


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário do artigo: {self.artigo}"


class Avaliacao(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='avaliacoes')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliacoes')
    pontuacao = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avaliacao de {self.autor.username} para {self.artigo.titulo} foi {self.pontuacao} estrelas'