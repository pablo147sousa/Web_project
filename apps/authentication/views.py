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
            return redirect('artigos:index')
    else:
        form = AuthenticationForm()

    return render(request, 'authentication/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'authentication/logout.html')

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('artigos:index')
    else:
        form = UserCreationForm()


    return render(request, 'authentication/registration.html', {'form': form,})