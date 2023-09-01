# arquivo com jogo local sem comunicação
# para rodar o jogo com comunicação rodar os arquivos server.py e client.py

import pygame
from sys import exit
from View import Board, Gameboard, BoardPosition, Player

FPS=20
cross=1
circle=2
empty=0

local=1
server=2

if __name__ == "__main__":
    pygame.init()
    
    surface = pygame.display.set_mode((1000,1000))
    clock = pygame.time.Clock()
   
    game = Board(surface, pygame)

    game.addPlayer(Player(local,cross,"Jogador 1"))
    game.addPlayer(Player(server,circle,"Jogador 2"))
    
    running = True
    while running:
        clock.tick(FPS)
        game.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit();exit()
            if event.type == pygame.MOUSEBUTTONUP:
                game.mouseClick(event.pos)
        game.update()
        game.draw()
        game.updateStatus()
        pygame.display.update()