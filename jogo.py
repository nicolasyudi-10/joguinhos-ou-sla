import pygame, sys, random
from pygame.locals import *


#INICIALIZAÇÃO
pygame.init()


#placar
fonte=pygame.font.SysFont(None, 28)
placarN=0



#TELA
screen=pygame.display.set_mode((650,650))
pygame.display.set_caption('PING-PONG')

  

#FPS
FPS=pygame.time.Clock()


#fator rebote
numx=10
numy=10


#DIRECAO PERSONAGEM
direita=1
esquerda=2
cima=3
baixo=4
parado=5


#CORES
azul=pygame.Color(0,0,139)
verdegay=pygame.Color(173,216,230)
brancox=pygame.Color(255,250,250)
vermelho=pygame.Color(139,0,0)

#personagem
personagem=[(500, 500)]
personagem_skin=pygame.Surface((20,10))
personagem_skin.fill(verdegay)


#IMPACTO
def impacto(r, b): 
    if r[0][1] - 10 <= b[0][1] <= r[0][1] + 10:
            for n in range(650):
                    if r[0][0]+n==b[0][0]:
                        return(True)
            return(False)

    else:
        return(False)
           
    



#jogo em si
while True:
    FPS.tick(60)
    
    #INICIALIZANDO
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        teclas=pygame.key.get_pressed()
        if teclas[pygame.K_d]:
                personagem[0]=(personagem[0][0] + 10, personagem[0][1])
        elif teclas[pygame.K_a]:
                personagem[0]=(personagem[0][0] - 10, personagem[0][1])
               
        elif teclas[pygame.K_w]:
                personagem[0]=(personagem[0][0], personagem[0][1]-10)
                
        elif teclas[pygame.K_s]:
                personagem[0]=(personagem[0][0], personagem[0][1]+10)
                

        
    #ATUALIZANDO TELA
    screen.fill((0,0,139))

    placar=fonte.render(f'Pontos:{placarN}', True, (255,255,255))
    screen.blit(placar, (10, 0))


    #DESENHO DO PERSONAGEM
    for pos in personagem:
        screen.blit(personagem_skin, pos)


    pygame.display.update()