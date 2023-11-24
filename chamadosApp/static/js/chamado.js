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

const submitChamado = document.querySelector('#submit-chamado');

submitChamado.addEventListener('click', e =>{
    submitChamado.setAttribute("disabled", "disabled");
    submitChamado.textContent = "Enviando Comentário...";
    submitChamado.style.transition = "ease 3s"
    submitChamado.classList.add('btn-success')
});