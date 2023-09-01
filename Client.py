# para rodar o jogo é necessario rodar o servidor e dois clientes que serão os jogadores

import pygame
import pickle
import socket
import threading
import sys
import ast
import queue
from View import Board, Gameboard, BoardPosition, Player


FPS=20
cross=1
circle=2

class Message:
    def __init__(self, turns):
        self.queue = queue.Queue()
        self.turns = turns
        self.playerClicked = False
        self.player = ""
        
        self.chat = []
        self.input_text = ""
        self.input_active = False

    def receive_messages(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                self.queue.put(data)    
            except:
                break

    def checkQueue(self):
        while not self.queue.empty():
            response = self.queue.get()
            self.checkMessages(response)
            print("isCurrentTurn")
            print(self.turns.isCurrentTurn)
                
    def checkMessages(self, data):
        if data == "1":
            self.turns.isCurrentTurn = True
            self.turns.player = "jogador 1"
        elif data.startswith("("):
            self.turns.playerClicked = True
            print(f"Received data from client: {data}") 
            self.turns.otherPlayTurns(ast.literal_eval(data))
        else:
            self.chat.append(data)
            
        
class Turns:
    def __init__(self):
        self.isCurrentTurn = False 
        self.playerClicked = False      
                
    def otherPlayTurns(self, response):
        if self.playerClicked:
            print(response)
            game.mouseClick(response)
            self.isCurrentTurn = True
            self.playerClicked = False
            
            
if __name__ == "__main__":          
    host = '127.0.0.1'
    port = 12345

    turns = Turns()
    messages = Message(turns)            
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    pygame.init()
    pygame.display.set_caption('Jogo da Velha')
    surface = pygame.display.set_mode((1000,1000))
    clock = pygame.time.Clock()
    
    game = Board(surface, pygame)
    game.addPlayer(Player(1,cross,"Jogador 1"))
    game.addPlayer(Player(2,circle,"Jogador 2"))

    receiver = threading.Thread(target=messages.receive_messages, args=(client,))
    receiver.start()  

    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit();exit()
            if event.type == pygame.MOUSEBUTTONUP:
                print(turns.isCurrentTurn)
                if turns.isCurrentTurn:
                    click = str(event.pos)
                    client.send(click.encode('utf-8'))
                    game.mouseClick(event.pos)
                    turns.isCurrentTurn = False
            elif event.type == pygame.KEYDOWN:
                if messages.input_active:
                    if event.key == pygame.K_RETURN:
                        messages.chat.append(messages.input_text)
                        client.send(messages.input_text.encode('utf-8'))
                        messages.input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        messages.input_text = messages.input_text[:-1]
                    else:
                        messages.input_text += event.unicode
                if event.key == pygame.K_RETURN:
                    messages.input_active = not messages.input_active
                
        messages.checkQueue()
        game.update()
        game.draw()
        game.updateStatus()
    
        game.render_input(messages.input_text)
        game.render_messages(messages.chat)
        pygame.display.update()
        if game.gameboard.gameOver():
            turns.isCurrentTurn = True
    client.close()
