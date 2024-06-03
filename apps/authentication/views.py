from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
# authentication/views.py

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('portfolio:index')
    else:
        form = AuthenticationForm()
        next_url = request.GET.get('next', '')

    return render(request, 'authentication/login.html', {'form': form, 'next': next_url})

def logout_view(request):
    logout(request)
    return redirect('pagina_inicial')

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('portfolio:index')
    else:
        form = UserCreationForm()


    return render(request, 'authentication/registration.html', {'form': form,})