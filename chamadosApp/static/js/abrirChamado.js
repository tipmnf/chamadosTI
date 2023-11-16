const chatSocket = new WebSocket(`ws://${window.location.host}/`);

const $chamadoForm = document.querySelector("#chamadoForm");

//Logic to send a message when the $chatForm is submitted.
$chatForm.addEventListener("submit", event => {
    const message = true;
    chatSocket.send(JSON.stringify({
        "message": message
    }));

});
