from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.db import connection
from .forms import *
from .models import *

# Create your views here

@login_required
def mainPage(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            chamados = filtraChamado(request, form)   
    else:
        form = SearchForm()    
        try:
            atendente = Atendente.objects.get(user=request.user)
        except:
            atendente = False
        
        if atendente:
            chamados = Chamado.objects.all()
        else:
            chamados = Chamado.objects.filter(requisitante=request.user)
    
    
    
    context = {
        'chamados': chamados,
        'form': form,
    }
    
    return render(request, 'mainPage.html', context)

@login_required
def abrirChamado(request):
    form = Chamado_Form()
    
    if request.method=='POST':
        form = Chamado_Form(request.POST)
        if form.is_valid():
         chamado=form.save(commit=False)
         chamado.save()
         
         return render(request, 'chamado.html', {'chamado': chamado})
    
    context={
        'form': form,
    }
            
    
    return render(request, 'abrirChamado.html', context)

@login_required
def chamado(request, idChamado):
    chamado = Chamado.objects.get(id=idChamado) 

    context = {
        'chamado': chamado,
    }

    return render(request, 'chamado.html', context)

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
    
@login_required
def sairFunc(request):
    logout(request)
    return redirect('/login/')
    
@login_required
def filtraChamado(request, form):
    
    numero = form.cleaned_data['numero']
    assunto = form.cleaned_data['assunto']
    requisitante = form.cleaned_data['requisitante']
    tipo = form.cleaned_data['tipo']
    secretaria = form.cleaned_data['secretaria']
    setor = form.cleaned_data['setor']
    
    sql = "SELECT id FROM chamadosApp_chamado WHERE status = '0'"
    
    params = []

    if numero:
        sql += " AND numero LIKE %s"
        params.append(f'%{numero}%')
    if assunto:
        sql += " AND assunto LIKE %s"
        params.append(f'%{assunto}%')
    if requisitante:
        sql += " AND requisitante_id LIKE %s"
        params.append(f'%{requisitante}%')
    if tipo:
        sql += " AND tipo_id LIKE %s"
        params.append(f'%{tipo}%')
    if secretaria:
        sql += " AND secretaria_id LIKE %s"
        params.append(f'%{secretaria}%')
    if setor:
        sql += " AND setor_id LIKE %s"
        params.append(f'%{setor}%')

    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        query = cursor.fetchall()
    
    
    idList = [idTuple[0] for idTuple in query]
    chamados = Chamado.objects.filter(id__in=idList)
        
    return chamados
    