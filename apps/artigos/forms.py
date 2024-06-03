from django import forms    # formulários Django
from .models import Autor
from .models import Artigo

class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.

class ArtigoForm(forms.ModelForm):
  class Meta:
    model = Artigo
    fields = '__all__'