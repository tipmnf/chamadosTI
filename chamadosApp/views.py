from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import Chamado_Form

# Create your views here.

@login_required
def mainPage(request):
    form = Chamado_Form()
    
    if request.method=='POST':
        form = Chamado_Form(request.POST)
        if form.is_valid():
         chamado=form.save(commit=False)
         chamado.save()
    
    context={
        'form': form,
    }
            
    
    return render(request, 'mainPage.html', context)

def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            form =  AuthenticationForm()
        
        return render(request, 'login.html', {'form': form})
    
