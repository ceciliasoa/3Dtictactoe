import pygame
import math
from sys import exit
from collections import defaultdict

cross=1
circle=2
empty=0
class BoardPosition:    
    def getPlan1Position(self,x,y):
            if (70 < y < 125 and 150 < x < 314) or (124 < y < 130 and 155 < x < 270):
                return [(0,0,0), (238, 112)]
            elif (70 < y < 125 and 321 < x < 474) or (124 < y < 150 and 280 < x < 470):
                return [(1,0,0), (370, 129)]
            elif (70 < y < 125 and 450 < x < 491) or (124 < y < 173 and 450 < x < 525):
                return [(2,0,0), (492, 151)]
            elif (139 < y < 155 and 132 < x < 231) or (154 < y < 178 and 88 < x < 210):
                return [(0,1,0), (156, 163)]
            elif (140 < y < 189 and 240 < x < 399) or (188 < y < 210 and 186 < x < 365):
                return [(1,1,0), (285, 180)]
            elif (175 < y < 200 and 400 < x < 490) or (199 < y < 231 and 348 < x < 487):
                return [(2,1,0), (426, 202)]
            elif (194 < y < 223 and 60 < x < 135) or (222 < y < 245 and 55 < x < 101):
                return [(0,2,0), (86, 217)]
            elif (208 < y < 247 and 83 < x < 295) or (246 < y < 267 and 150 < x < 274):
                return [(1,2,0), (189, 241)]
            elif (233 < y < 267 and 239 < x < 426) or (266 < y < 289 and 267 < x < 375):
                return [(2,2,0), (335, 263)]
            else:
                return -1, -1  
            
    def getPlan2Position(self,x,y):
            if (320 < y < 338 and 165 < x < 314) or (337 < y < 354 and 165 < x < 260):
                return [(0,0,1), (237, 330)]
            elif (333 < y < 360 and 287 < x < 472) or (359 < y < 375 and 287 < x < 458):
                return [(1,0,1), (365, 349)]
            elif (354 < y < 378 and 447 < x < 528) or (377 < y < 388 and 450 < x < 528):
                return [(2,0,1), (493, 369)]
            elif (359 < y < 387 and 94 < x < 225) or (386 < y < 410 and 150 < x < 195):
                return [(0,1,1), (158, 379)]
            elif (373 < y < 415 and 195 < x < 380) or (414 < y < 431 and 205 < x < 370):
                return [(1,1,1), (296, 403)]   
            elif (391 < y < 429 and 352 < x < 490) or (428 < y < 453 and 352 < x < 490):
                return [(2,1,1), (435, 422)]    
            elif (417 < y < 444 and 70 < x < 136) or (443 < y < 466 and 55 < x < 70):
                return [(0,2,1), (87, 434)] 
            elif (433 < y < 467 and 102 < x < 298) or (466 < y < 495 and 102 < x < 222):
                return [(1,2,1), (200, 462)]      
            elif (453 < y < 493 and 239 < x < 393) or (492 < y < 514 and 239 < x < 400):
                return [(2,2,1), (338, 482)]
            else:
                return -1, -1    
                   
    def getPlan3Position(self,x,y):
            if (523 < y < 556 and 226 < x < 298) or (555 < y < 569 and 156 < x < 255):
                return [(0,0,2), (237, 551)]
            elif (549 < y < 579 and 285 < x < 472) or (578 < y < 597 and 283 < x < 440):
                return [(1,0,2), (368, 569)]
            elif (576 < y < 595 and 446 < x < 528) or (594 < y < 611 and 446 < x < 528):
                return [(2,0,2), (497, 593)] 
            elif (590 < y < 601 and 98 < x < 402) or (600 < y < 628 and 90 < x < 198):
                return [(0,1,2), (153, 601)]
            elif (591 < y < 630 and 205 < x < 395) or (629 < y < 655 and 185 < x < 362):
                return [(1,1,2), (289, 620)]    
            elif (618 < y < 648 and 370 < x < 494) or (647 < y < 673 and 352 < x < 475):
                return [(2,1,2), (425, 639)]         
            elif (635 < y < 669 and 61 < x < 141) or (668 < y < 690 and 35 < x < 100):
                return [(0,2,2), (85, 657)] 
            elif (646 < y < 690 and 102 < x < 298) or (689 < y < 716 and 83 < x < 261):
                return [(1,2,2), (188, 680)]      
            elif (674 < y < 715 and 264 < x < 437) or (714 < y < 753 and 235 < x < 380):
                return [(2,2,2), (343, 703)]
            else:
                return -1, -1
            
    def rotate_point(self, point, origin, angle_degrees=60):
        angle_radians = math.radians(angle_degrees)
        x, y = point
        ox, oy = origin
        new_x = ox + math.cos(angle_radians) * (x - ox) - math.sin(angle_radians) * (y - oy)
        new_y = oy + math.sin(angle_radians) * (x - ox) + math.cos(angle_radians) * (y - oy)
        
        return int(new_x), int(new_y)

           
class Gameboard:    
    winLines=[[(a,b,c) for a in range(0,3)]  for b in range(0,3) for c in range(0,3)]
    winColumns = [[(a,b,c) for b in range(0,3)]  for a in range(0,3) for c in range(0,3)]
    winDiag = [[(b,b,c) for b in range(0,3)] for c in range(0,3)]+[[(2-b,b,c) for b in range(0,3)] for c in range(0,3)]
    winInterColumns = [[(a,b,c) for c in range(0,3)]  for a in range(0,3) for b in range(0,3)]
    winInterLineDiag = [[(c,b,c) for c in range(0,3)] for b in range(0,3)]+[[(2-c,b,c) for c in range(0,3)] for b in range(0,3)]
    winInterColumnDiag = [[(a,c,c) for c in range(0,3)] for a in range(0,3)]+[[(a,2-c,c) for c in range(0,3)] for a in range(0,3)]
    winInterDiag = [[(0,0,0),(1,1,1),(2,2,2)],[(2,0,0),(1,1,1),(0,2,2)],[(2,2,0),(1,1,1),(0,0,2)],[(0,2,0),(1,1,1),(2,0,2)]]

    allWinPossibles = winLines + winColumns + winDiag + winInterColumns  + winInterLineDiag + winInterColumnDiag + winInterDiag
    possiblecells = [ (a,b,c) for a in range(0,3) for b in range(0,3) for c in range(0,3)]

    def __init__(self):
        self.moves=[]
        self.moveCenter = []
        self.gameover=False
        self.draw=False
        self.giveUp=False
        self.board=defaultdict(lambda:empty)

    def getFreePositions(self):
        return [x for x in self.possiblecells if not x in self.moves]

    def move(self,position,symbol):
        if self.board[position] != empty:
            return False
        self.board[position]=symbol
        self.moves.append(position)
        self.checkGameOver()
        return True
    
    def gameOver(self):
        return self.gameover

    def gameDraw(self):
        return self.draw
    
    def playerGiveUp(self):
        return self.giveUp
    
    def getWinner(self):
        if self.gameOver() and not self.gameDraw():
            return self.winner

    def checkGameOver(self):
        for win in self.allWinPossibles:
            px,py,pz=win
            if self.board[px] != empty and self.board[px]==self.board[py]==self.board[pz]:
                self.gameover = True
                self.winner = self.board[px]
                self.draw=False
                print(win)
                break
        else:
            if len(self.moves) == 27:
                self.draw=True
                self.gameover = True
            elif self.giveUp:
                self.gameover = True
            else:
                self.gameover = False

class Board: 
    def __init__(self, surface, pygame):
         # interface
        self.font = pygame.font.SysFont('Corbel', 55) 
        self.smallFont = pygame.font.SysFont('Corbel', 25) 
        self.backgroundColor = (65, 61, 82)
        self.gridColor = (201, 173, 161)
        self.crossColor = (127, 222, 255)
        self.circleColor = (222, 246, 202)
        self.labelColor = (201, 173, 161)
        self.thickness = 10
        self.surface = surface
        
        # game
        self.gameboard = Gameboard()
        self.position = BoardPosition()
        self.players = []
        
    
    def draw(self):
        self.surface.fill(self.backgroundColor)
        
        #  board 1
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((200, 30), (200,180))), (self.position.rotate_point((200, 330), (200,180))), self.thickness)
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((400,80), (400,180))), (self.position.rotate_point((400, 380), (400,180))), self.thickness)
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((150, 130), (325,130), 0)), (self.position.rotate_point((500, 130), (325,130), 15)), self.thickness)
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((100, 230), (325,130), 10)), (self.position.rotate_point((450, 230), (325,130), 5)), self.thickness)
        
        # board 2
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((200, 250), (200,400))), (self.position.rotate_point((200, 550), (200,400))), self.thickness)
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((400,300), (400,400))), (self.position.rotate_point((400, 600), (400,400))), self.thickness)
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((150, 350), (325,350), 0)), (self.position.rotate_point((500, 350), (325,350), 15)), self.thickness)
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((100, 450), (325,350), 10)), (self.position.rotate_point((450, 450), (325,350), 5)), self.thickness)
        
        # board 3 
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((200, 470), (200,620))), (self.position.rotate_point((200, 770), (200,620))), self.thickness)
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((400, 520), (400,620) )), (self.position.rotate_point((400, 820), (400,620))), self.thickness)
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((150, 570), (325,570), 0)), (self.position.rotate_point((500, 570), (325,570), 15)), self.thickness)
        pygame.draw.line(self.surface, self.gridColor, (self.position.rotate_point((100, 670), (325,570), 10)), (self.position.rotate_point((450, 670), (325,570), 5)), self.thickness)
        
        self.drawButton()
        self.playMove()

    def mouseClick(self,pos):
        px,py=pos
        if self.gameboard.gameOver():
                self.reset()
        if (300 < px < 700) and (900 < py < 950):
            print("desistiu")
            self.gameboard.giveUp = True
        elif 65 < px < 537:
            if py < 295:
                cell, center = self.position.getPlan1Position(px,py)
                self.player1.mouseClick(cell, center)  
               
            elif 300 < py < 518:
                cell, center =self.position.getPlan2Position(px,py)
                self.player1.mouseClick(cell, center)
                
            elif 520 < py < 760:
                cell, center = self.position.getPlan3Position(px,py)
                self.player1.mouseClick(cell, center)
                
    def playMove(self):
        for i, move in enumerate(self.gameboard.moves):
            if self.gameboard.board[move] == circle:
                pygame.draw.circle(self.surface, self.circleColor, self.gameboard.moveCenter[i], 20, 5) 
            else:
                x,y = self.gameboard.moveCenter[i]
                pygame.draw.line(self.surface, self.crossColor, (x-15, y-15), (x+15, y+15), 5) 
                pygame.draw.line(self.surface, self.crossColor, (x-15, y+15), (x+15, y-15), 5) 
            
    def reset(self):
        self.gameboard=Gameboard()
        for player in self.players:
            player.setBoard(self.gameboard)
        self.player1,self.player2=self.player2,self.player1
                
    def update(self):
        if not self.gameboard.gameOver():
            nextpos=self.player1.getMove()
            if  nextpos is not None:
                self.gameboard.move(nextpos,self.player1.sign)  
                if not self.gameboard.gameOver():
                    self.player1,self.player2=self.player2,self.player1 
    
    def updateStatus(self):
        textstr=''
        if self.gameboard.gameOver():
            if self.gameboard.gameDraw():
                textstr="Deu velha. Clique para reiniciar"
            elif self.gameboard.playerGiveUp():
                textstr=self.player1.name+" desistiu."
            else:
                textstr=self.player1.name+" ganhou. Clique para reiniciar "
        else:
            textstr=" turno de "+self.player1.name+" "

        text = self.font.render(textstr, 1, self.labelColor)
        textpos = text.get_rect(centerx = self.surface.get_width()/2,y=850)
        self.surface.blit(text, textpos)
    
    def drawButton(self):
        rect = pygame.Rect(300, 900, 400, 50)
        pygame.draw.rect(self.surface, (197, 40, 61), rect)
        text_surface = self.font.render("desistir", True, self.gridColor)
        text_rect = text_surface.get_rect(center=rect.center)
        self.surface.blit(text_surface, text_rect)
        
    def render_messages(self, messages):
        y_offset = 130
        for message in messages:
            text_surface = self.smallFont.render(message, True, (197, 40, 61))
            self.surface.blit(text_surface, (570, y_offset))
            y_offset += 25

    def render_input(self, input_text):
        pygame.draw.rect(self.surface, self.gridColor, (550, 100, 550, 700))
        input_surface = self.smallFont.render("aperte enter para escrever >  " + input_text, True, (197, 40, 61))
        self.surface.blit(input_surface, (570, 750))    
                    
    def addPlayer(self,player):
        player.setBoard(self.gameboard)
        self.players.append(player)
        if (len(self.players) > 1):  
            self.player1=self.players[0]
            self.player2=self.players[1]   
              
class Player:
    def __init__(self,type,sign,name):
        self.type=type
        self.sign=sign
        self.name = name
        self.lastmove=-1

    def setBoard(self,board):
        self.board=board

    def getMove(self):
        if(self.lastmove != -1):
            move=self.lastmove
            self.lastmove=-1
            return move

    def mouseClick(self,cell, center):
        if cell!= -1 and not cell in self.board.moves:
            self.lastmove=cell
            self.board.moveCenter.append(center)

    def oppositeSign(self,sign):
        if sign == circle:
            return cross
        return circle        
 

     