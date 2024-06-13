from django import forms    # formulários Django
from .models import Autor
from .models import Artigo
from .models import Comentario
from .models import Avaliacao

class AutorForm(forms.ModelForm):
    bio = forms.CharField(
        widget=forms.Textarea,
        help_text="Descreva sobre você como autor",
        label="Biografia"
    )

    class Meta:
        model = Autor
        fields = ['bio']

class ArtigoForm(forms.ModelForm):
  class Meta:
    model = Artigo
    fields = '__all__'


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['pontuacao']
