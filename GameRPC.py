import ast
import pygame
import Pyro4
import threading
import sys
from View import Board, Gameboard, BoardPosition, Player

FPS=20
cross=1
circle=2

@Pyro4.expose
class playerInteraction:
    def __init__(self, game):
        self.game = game
        self.isCurrentTurn = False
        self.meText = "você: "
        self.otherText = "adversário: "
        self.message = []
        self.input_text = ""
        self.input_active = False

    def register(self, name):
        try:
            daemon = Pyro4.Daemon()
            ns = Pyro4.locateNS()
            uri = daemon.register(self)
            ns.register(name, uri)

            threading.Thread(target=daemon.requestLoop).start()
        except:
            print("não foi possível realizar o registro")

    def conectWithServer(self, hostName, clientName):
        try:
            self.otherPlayer = Pyro4.Proxy("PYRONAME:" + hostName)
            self.otherPlayer.receiveConection(clientName)
            print("você entrou na sala " + hostName)
        except:
            print("não foi possível se conectar a essa sala") 
    
    def receiveConection(self, name):
        self.otherPlayer = Pyro4.Proxy("PYRONAME:" + name)
        print(name + " entrou na sala")
   
    def sendMessage(self):
        self.message.append(self.meText + self.input_text)
        self.otherPlayer.receiveMessage(self.input_text)
        self.input_text = ""
    
    def receiveMessage(self, message):
        self.message.append(self.otherText + message)
        
    def playMove(self, position): 
        if not self.game.gameboard.gameOver():
            isValid = game.mouseClick(position)
            if self.isCurrentTurn and isValid:
                self.otherPlayer.playMove(position)
                self.isCurrentTurn = False
            else:
                self.isCurrentTurn = True

def runGame(playerInteraction, game):
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit();exit()
            if event.type == pygame.MOUSEBUTTONUP:                
                if playerInteraction.isCurrentTurn:
                    playerInteraction.playMove(event.pos)
            elif event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    if game.gameboard.gameOver():
                        game.reset()
                if playerInteraction.input_active:
                    if event.key == pygame.K_RETURN:
                        playerInteraction.sendMessage()
                    elif event.key == pygame.K_BACKSPACE:
                        playerInteraction.input_text = playerInteraction.input_text[:-1]
                    else:
                        playerInteraction.input_text += event.unicode
                if event.key == pygame.K_RETURN:
                    playerInteraction.input_active = not playerInteraction.input_active
        game.update()
        game.draw()
        game.updateStatus()

        game.render_input(playerInteraction.input_text)
        game.render_messages(playerInteraction.message)
        pygame.display.update()
       
       
if __name__ == "__main__":
   
    pygame.init()
    pygame.display.set_caption('Jogo da Velha')
    surface = pygame.display.set_mode((1000,1000))
    clock = pygame.time.Clock()
    
    game = Board(surface, pygame)
    game.addPlayer(Player(1,cross,"Jogador 1"))
    game.addPlayer(Player(2,circle,"Jogador 2"))
    
    gameType = input("Digite 0 para criar uma partida e 1 para se conectar a uma partida existente\n")
    
    if gameType == '0':
        hostName = input("Digite o nome da sala: ")
        server = playerInteraction(game)
        server.register(hostName)
        server.isCurrentTurn = True
        runGame(server, game)
    else:
        playerName = input("Digite o nome do jogador: ")
        hostName = input("Digite o nome da sala existente: ")
        client = playerInteraction(game)
        client.register(playerName)
        client.conectWithServer(hostName, playerName)
        runGame(client, game)
