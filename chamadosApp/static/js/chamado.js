const prioridadeChamado = document.getElementById('prioridade-chamado')
if(prioridadeChamado.textContent == "Prioridade: Média"){
    prioridadeChamado.style.border = '1px solid yellow'
}

if(prioridadeChamado.textContent == "Prioridade: Alta"){
    prioridadeChamado.style.border = '1px solid red'
}

if(prioridadeChamado.textContent == "Prioridade: Baixa"){
    prioridadeChamado.style.border = '1px solid blue'
}