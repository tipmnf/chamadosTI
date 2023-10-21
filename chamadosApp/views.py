from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.db import connection
from django.urls import reverse
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
    chamados = chamados.order_by('-numero')
    
    context = {
        'chamados': chamados,
        'form': form,
    }
    
    return render(request, 'mainPage.html', context)

@login_required
def abrirChamado(request):
    servidor = Servidor.objects.get(user=request.user)
    form = Chamado_Form()
    
    if request.method=='POST':
        form = Chamado_Form(request.POST)
        if form.is_valid():
            chamado=form.save(commit=False)
            chamado.requisitante = servidor
            chamado.secretaria = servidor.setor.secretaria
            chamado.setor = servidor.setor
            chamado.setNumero()
            
            return render(request, 'chamado.html', {'chamado': chamado})
    
    context={
        'form': form,
        'servidor': servidor,
    }
            
    
    return render(request, 'abrirChamado.html', context)

@login_required
def chamado(request, idChamado):
    chamado = Chamado.objects.get(id=idChamado)
    atendentes = Atendente.objects.all() 
    
    if request.method == 'POST':
        chamado = atualizaChamado(request, chamado)

    context = {
        'chamado': chamado,
        'atendentes': atendentes,
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
    
def cadastroView(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'cadastro.html')
    
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
    dataInicio = form.cleaned_data['dataInicio']
    dataFim = form.cleaned_data['dataFim']
    status = form.cleaned_data['status']
    
    
    sql = "SELECT id FROM chamadosApp_chamado WHERE "
    
    params = []

    if status:
        if status != '3':
            sql += " status LIKE %s"
            params.append(f'%{status}%')
        else:
            sql += " status IS NOT NULL ORDER BY status DESC"
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


    
    if dataInicio and dataFim:
        sql+= " AND DATE(dataAbertura) BETWEEN %s AND %s"
        params.append(dataInicio)
        params.append(dataFim)
    elif dataInicio:
        sql+= " AND DATE(dataAbertura) >= %s"
        params.append(dataInicio)
    elif dataFim:
        sql+= " AND DATE(dataAbertura) <= %s"
        params.append(dataFim)
        
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        query = cursor.fetchall()
    
    print(sql)
    print(dataInicio)
    print(dataFim)
    
    idList = [idTuple[0] for idTuple in query]
    chamados = Chamado.objects.filter(id__in=idList)
    

        
    return chamados
    

def atualizaChamado(request, chamado):
    
    newPrioridade = request.POST.get('prioridade')
    newStatus = request.POST.get('status')
    
    newAtendente = request.POST.get('atendente')
    try:
        newAtendente = Atendente.objects.get(id=newAtendente)
    except:
        newAtendente = None
    
    chamado.prioridade = newPrioridade
    chamado.status = newStatus
    chamado.atendente = newAtendente
    
    chamado.save()
    
    return chamado


@login_required
def editaChamado(request, idChamado):
    chamado = Chamado.objects.get(id=idChamado)
    
    if request.method == 'POST':
        form = editaChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect(reverse('chamado', args=[chamado.id]))
    else:
        form = editaChamadoForm(instance=chamado)        
    
    return render(request, 'editaChamado.html', {'form': form, 'chamado': chamado})


@login_required
def indicadores(request):
    setores = Setor.objects.all()
    secretarias = Secretaria.objects.all()

    context = {
        'setores': setores,
        'secretarias': secretarias
    }
    return render(request, 'indicadores.html', context)

@login_required
def atendentes(request):
    atendentes = Atendente.objects.all()
    context = {
        'atendentes': atendentes,
    }
    return render(request, 'atendentes.html', context)