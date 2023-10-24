document.addEventListener('DOMContentLoaded', function() {
    let buttonPesquisaChamado = document.getElementById("button-pesquisa-chamado");
    let formMainPage = document.getElementById("form-pesquisa-chamado");

    buttonPesquisaChamado.addEventListener('click', function(){
        let computedStyle = window.getComputedStyle(formMainPage);
        if (computedStyle.display === 'none') {
            formMainPage.style.display = 'block';
        } else {
            formMainPage.style.display = 'none';
        }
    });
});
