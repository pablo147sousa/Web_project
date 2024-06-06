from django.shortcuts import render,get_object_or_404,redirect
from .models import Artigo
from .models import Avaliacao
from .models import Autor
from .models import Comentario
from .forms import AutorForm,ArtigoForm
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

def new_author_view(request):

    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('artigos:index')

    context = {'form': form}
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

def novo_artigo_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)  # Retrieve the Autor object using autor_id
    form = ArtigoForm(request.POST or None, request.FILES)

    if form.is_valid():
        livro = form.save(commit=False)
        livro.autor = autor
        livro.save()
        return redirect('artigos:autor',autor.id) # type: ignore

    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)

def edit_article_view(request, article_id):
    article = Artigo.objects.get(id=article_id)

    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect('artigos:article',article.id) # type: ignore
    else:
        form = ArtigoForm(instance=article)  # cria formulário com dados da instância artigo

    context = {'form': form, 'article':article}
    return render(request, 'artigos/edita_artigo.html', context)

def apaga_artigo_view(request, article_id):
    artigo = Artigo.objects.get(id=article_id)
    artigo.delete()
    return redirect('artigos:index')