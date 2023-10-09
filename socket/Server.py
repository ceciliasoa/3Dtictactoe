
import pygame
import pickle
import socket
import threading
import sys
from View import Board, Gameboard, BoardPosition, Player

FPS=20
cross=1
circle=2
empty=0

def handle_client(client_socket, move = 0):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received data from client: {data}")
            # Encaminha a mensagem para todos os outros clientes conectados
            for client in clients:
                if client != client_socket:
                    print(f"enviado")
                    client.send(data.encode('utf-8'))
        except:
            pass
        
    client_socket.close()
    clients.remove(client_socket)
    print(f"Conexão de jogador  encerrada")
    

def send_message():
    clients[0].send("1".encode('utf-8'))
        
      
host = '127.0.0.1'
port = 12345
   
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(2)

print(f"Server listening on {host}:{port}")

clients = []

# send_thread = threading.Thread(target=send_message)
# send_thread.start()

while len(clients) < 2:
    
    client_socket, _ = server.accept()
    clients.append(client_socket)
    # enviar player
    print(f"Accepted connection from {client_socket.getpeername()}")
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
send_message()
    # obj_encoded = pickle.dumps(game)
    # client_socket.send(obj_encoded)
    # client[0].send(obj_encoded)
    
    
    # enviar click e nome do jogador (via cli)
    # descobrir como roda 2x
    # botão de desistencia