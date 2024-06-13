from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Artigo
from .models import Avaliacao
from .models import Autor
from .models import Comentario
from .forms import AutorForm,ArtigoForm,ComentarioForm,AvaliacaoForm


# Create your views here.
def index_view(request):
    artigos = Artigo.objects.all()
    context = {
        'artigos': artigos,
    }
    return render(request, "artigos/index.html", context)


def article_view(request, article_id):
    article = get_object_or_404(Artigo, id=article_id)
    comments = Comentario.objects.filter(artigo=article_id)
    rating = Avaliacao.objects.filter(artigo=article_id)
    context = {
        'article': article,
        'comments': comments,
        'rating': rating,
    }
    return render(request, "artigos/article.html", context)


def autor_view(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    artigos = autor.artigos.all() # type: ignore
    context = {
        'autor': autor,
        'artigos': artigos,
    }
    return render(request, "artigos/autor.html", context)

# Manipulação Autores

@login_required
def new_author_view(request):
    try:
        has_author = bool(Autor.objects.get(user= request.user))
    except:
        has_author = False
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save(commit=False)
            autor.user = request.user
            autor.save()
            return redirect('artigos:autor',autor.id)
    else:
        form = AutorForm()

    context = {'form': form,'has_author':has_author}
    return render(request, 'artigos/novo_autor.html', context)

def edita_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)

    if request.POST:
        form = AutorForm(request.POST or None, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('artigos:autor',autor.id) # type: ignore
    else:
        form = AutorForm(instance=autor)  # cria formulário com dados da instância autor

    context = {'form': form, 'autor':autor}
    return render(request, 'artigos/edita_autor.html', context)


def apaga_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect('artigos:index')

# Manipulação Artigos

@login_required
def novo_artigo_view(request):
    # Obter o objeto Autor associado ao usuário autenticado
    autor = get_object_or_404(Autor, usuario=request.user)

    form = ArtigoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = autor
        artigo.save()
        # Redirecionar para a página de detalhes do artigo ou uma página de lista de artigos
        return redirect('detalhes_artigo', artigo_id=artigo.id)

    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)


def edit_article_view(request, article_id):
    article = Artigo.objects.get(id=article_id)
    is_author = request.user == article.autor
    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect('artigos:article',article.id) # type: ignore
    else:
        form = ArtigoForm(instance=article)  # cria formulário com dados da instância artigo

    context = {'form': form, 'article':article,'is_author': is_author,}
    return render(request, 'artigos/edita_artigo.html', context)


def apaga_artigo_view(request, article_id):
    artigo = Artigo.objects.get(id=article_id)
    artigo.delete()
    return redirect('artigos:index')

# Interações

@login_required
def comment_article(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    if request.method == "POST":
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            return redirect('article_view', artigo_id=artigo.id) # type: ignore

    return redirect('article_view', artigo_id=artigo.id) # type: ignore

@login_required
def rate_article(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    if request.method == "POST":
        avaliacao_form = AvaliacaoForm(request.POST)
        if avaliacao_form.is_valid():
            avaliacao = avaliacao_form.save(commit=False)
            avaliacao.artigo = artigo
            avaliacao.autor = request.user
            avaliacao.save()
            return redirect('article_view', artigo_id=artigo.id) # type: ignore

    return redirect('article_view', artigo_id=artigo.id) # type: ignore