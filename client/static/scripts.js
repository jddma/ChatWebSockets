$(document).ready(function () {

    let websocket;
    let name = null;
    
    function connectSocket() { 

        let host = prompt("Digite el host del servidor");

        websocket = new WebSocket(`ws://${host}/`);
        websocket.onmessage = receiveMessage;

    }

    function sendMessage () {

        if (name == null) 
        {
            name = prompt("Digite su nombre");
        }

        let msg = {
            "name": name,
            "content": $("#msg").val()
        };

        websocket.send(JSON.stringify(msg));

    }

    function receiveMessage (event) {

        console.log(event.data);

    }

    $("#btn").click(function (e) { 
        
        sendMessage();
        
    });

    connectSocket();

});