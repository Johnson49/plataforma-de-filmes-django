from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Filme


def index(request):
    return HttpResponse("Bem-vindo ao Play Filmes")


def filmes(request):
    filmes = Filme.objects.all()
    return render(request, "filme.html", {"filmes": filmes})


def registrar(request):
    criacao = request.POST.get("criacao")

    titulo = request.POST.get("titulo")

    genero = request.POST.get("genero")

    descricao = request.POST.get("descricao")

    duracao = request.POST.get("duracao")

    ano_lancamento = request.POST.get("ano_lancamento")

    url_imagem = request.POST.get("url_imagem")

    Filme.objects.create(
        titulo=titulo,
        ativo=True,
        criacao=criacao,
        genero=genero,
        descricao=descricao,
        ano_lancamento=ano_lancamento,
        url_imagem=url_imagem,
        duracao=duracao

    )
    filmes = Filme.objects.all()
    return render(request, "filme.html", {"filmes": filmes})


def detalhes(request, id):
    filme = Filme.objects.get(id=id)
    return render(request, "detalhes.html", {"filme": filme})

def editar(request,id ):
    filme = Filme.objects.get(id=id)
    return render(request, "atualizar.html", {"filme": filme})

def excluir(request, id):
    filme = Filme.objects.get(id=id)
    filme.delete()

    return redirect(filmes)

def atualizar(request, id):
    filme = Filme.objects.get(id=id)

    titulo = request.POST.get("titulo")

    genero = request.POST.get("genero")

    descricao = request.POST.get("descricao")

    duracao = request.POST.get("duracao")

    ano_lancamento = request.POST.get("ano_lancamento")

    url_imagem = request.POST.get("url_imagem")

    filme.titulo=titulo
    filme.genero=genero
    filme.descricao=descricao
    filme.ano_lancamento=ano_lancamento
    filme.url_imagem=url_imagem
    filme.duracao=duracao

    filme.save()

    return redirect(filmes)