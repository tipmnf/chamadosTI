const modal = document.querySelector('#modal');
const buttonYesSair = document.querySelector('#buttonYesSair');
const buttonNoSair = document.querySelector('#buttonNoSair');
const fecharSair = document.querySelector('.fechar-sair');
const btnsApagar = document.querySelectorAll('.btn-apagar');

btnsApagar.forEach(btnApagar => {
    btnApagar.addEventListener('click', function (e) {
        e.preventDefault();
        console.log("Botão de apagar clicado");
        modal.style.display = 'block';
    });
});


buttonNoSair.addEventListener('click', function(){
    modal.style.display = 'none';
});

buttonYesSair.addEventListener('click', function(){
    const atendenteId = btnsApagar.getAttribute('href').split("/").pop();
    window.location.href = 'transformaParaServidor/' + atendenteId;
});

fecharSair.addEventListener('click', function(){
    modal.style.display = 'none';
});
