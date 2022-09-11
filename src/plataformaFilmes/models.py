from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_now = True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Filme(Base):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    descricao = models.TextField()
    duracao = models.CharField(max_length=15)
    ano_lancamento = models.IntegerField()
    url_imagem = models.URLField(unique=True)

    class Meta:
        verbose_name: "Filme"
        verbose_name_plural: "Filmes"

    def __str__(self):
        return f"{self.titulo} ‧ {self.genero} ‧ {self.ano_lancamento}"
    

class Avaliacao(Base):
    filme = models.ForeignKey(Filme, related_name="avaliacoes", on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default="")
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name: "Avaliação"
        verbose_name_plural: "Avaliações"
        unique_together = ["email", "filme"]
    

    def __str__(self):
        return f'{self.nome} avaliou o filme "{self.filme}" com a nota {self.avaliacao}.'