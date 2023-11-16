const chatSocket = new WebSocket(`ws://${window.location.host}/`);

function updateChamados(){
    console.log("cheguei aqui")
    return true;
}

console.log(chatSocket);

//Logic to receive messages
chatSocket.addEventListener("message", event => {
    const data = JSON.parse(event.data);
    updateChamados();
});

chatSocket.addEventListener("close", event => {
    console.error("The WebSocket socked unexpectedly");
});
