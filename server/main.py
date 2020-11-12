import asyncio
import logging
import websockets

logging.basicConfig()
CLIENTS = set()

def register_client(client):
    CLIENTS.add(client)

#Método que envia un mensaje a todos los clientes registrados
async def send_messages(message):
    if CLIENTS:
        for client in CLIENTS:
            await client.send(message)

#Función que se ejecuta cuando un cliente se conecta o active un evento
async def event(websocket, _):

    #Registrar el cliente en caso de que no estar registrado previamente
    register_client(websocket)

    #Enviar el mensaje a todos los clientes registrados
    async for message in websocket:
        await send_messages(message)

#Instanciar el servidor de websockets
start_server = websockets.serve(event, "127.0.0.1", 6789)

#Iniciar la escucha del servidor
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
