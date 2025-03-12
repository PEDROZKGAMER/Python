
import pygame 
from pygame import mixer
from time import sleep
from random import randint 
from random import Random



x, y = (960, 540)
janela = pygame.display.set_mode([x, y])
pygame.display.set_caption('Retorno dos Aliens')


tiro_alvo = False 

pos_player_x = 430
pos_player_y = 400
velocidade_nave = 10

pos_inimigo_x = 430
pos_inimigo_y = 50
velocidade_inimigo = 15


vel_x_missil = 10
pos_x_missil = 430
pos_y_missil = 450

pontuação = 0

def colisoes():
    global pontuação 
    global pos_inimigo_y 
    global pos_inimigo_x
    global som_nave_colisao
    global som_missil
    global som_explosao

    #Se o player principal colidir com a nave inimiga.
    if player_rect.colliderect(inimigo_rect) or inimigo_rect.y > 500:
        pontuação -= 1
        print(pontuação)
        return True 
    elif tiro_rect.colliderect(inimigo_rect):
        pontuação += 1 
        pos_inimigo_y -= 1200
        if pos_inimigo_y < -1000:
            random_y = randint(1, 440)
            random_x = randint(1, 870)
            pos_inimigo_y -= 450
            pos_inimigo_y = random_y
            pos_inimigo_x = random_x
        print(pontuação)
        som_explosao.play()
        return True 

    else:
        return False 



def resultado():
    global pontuação 

    if pontuação < 0:
        print('Você perdeu o Jogo! GAME OVER!')
    else:
        print('Você ganhou o Jogo! PARABÉNS!')





rodando = True 

while rodando:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            rodando = False
        

        #Carregamento e inserção de Imagens na Janela.
        bg = pygame.image.load('C:/Users/p1097.DESKTOP-7B8R317/OneDrive/Documentos/Python/JOGOS/Aliens atack/space bg game.png')
        nave_principal = pygame.image.load('C:/Users/p1097.DESKTOP-7B8R317/OneDrive/Documentos/Python/JOGOS/Aliens atack/sprite_nave_pequena.png')
        janela.blit(bg, (0, 0))
        nave_inimiga = pygame.image.load('C:/Users/p1097.DESKTOP-7B8R317/OneDrive/Documentos/Python/JOGOS/Aliens atack/nave_inimiga_pequena.png')
        tiro = pygame.image.load('C:/Users/p1097.DESKTOP-7B8R317/OneDrive/Documentos/Python/JOGOS/Aliens atack/missil_pequeno.png')
        tiro = pygame.transform.scale(tiro, (30, 30))
        

        #Movimento do Inimigo
        
        pos_inimigo_y += 10
        
        """print(pos_inimigo_y)
        print(pos_y_missil)"""


        #pos_y_missil -= vel_x_missil

        
        if pos_inimigo_y > 530:
            random_y = randint(1, 440)
            random_x = randint(1, 870)
            pos_inimigo_y -= 450
            pos_inimigo_y = random_y
            pos_inimigo_x = random_x
           
        

            
        comandos = pygame.key.get_pressed()

        if comandos[pygame.K_UP] and pos_player_y > 1:   
            #Faz a Nave Subir
            pos_player_y -= velocidade_nave
            if not tiro_alvo:
                pos_y_missil -= vel_x_missil
                vel_x_missil = 10
                
        if comandos[pygame.K_DOWN] and pos_player_y < 440:
            #Faz a Nave Descer
            pos_player_y += velocidade_nave
            if not tiro_alvo:
                pos_y_missil += vel_x_missil
                vel_x_missil = 10
        if comandos[pygame.K_LEFT] and pos_player_x > 1:
            #Faz a nave ir para esquerda
            pos_player_x -= velocidade_nave
            if not tiro_alvo:
                pos_x_missil -= vel_x_missil
                vel_x_missil = 10
        if comandos[pygame.K_RIGHT] and pos_player_x < 870:
            pos_player_x += velocidade_nave
            if not tiro_alvo:
                tiro_alvo = False 
                pos_x_missil += vel_x_missil
                vel_x_missil = 10
        if comandos[pygame.K_SPACE]:
            tiro_alvo = True
            if tiro_alvo:
                vel_x_missil = 10
                pos_y_missil -= vel_x_missil
            if pos_y_missil < 1:
                #Respawna o Míssil de volta a Nave pronto para ser atirado novamente.
                tiro_alvo = True 
                pos_y_missil = pos_player_y 
                pos_x_missil = pos_player_x 
                vel_x_missil = -500

        
        

        player_rect = nave_principal.get_rect()
        inimigo_rect = nave_inimiga.get_rect()
        tiro_rect = tiro.get_rect()

        
            
        
        player_rect.y = pos_player_y
        player_rect.x = pos_player_x 

        inimigo_rect.y = pos_inimigo_y 
        inimigo_rect.x = pos_inimigo_x 

        tiro_rect.y = pos_y_missil
        tiro_rect.x = pos_x_missil 

        colisoes()
            
        if tiro_alvo:
                pos_y_missil -= vel_x_missil
            
            #Colisão do tiro com nave Inimiga.
         
        janela.blit(tiro, (pos_x_missil, pos_y_missil))
        janela.blit(nave_inimiga, (pos_inimigo_x, pos_inimigo_y))
        janela.blit(nave_principal, (pos_player_x, pos_player_y))

        #Transforma a imagem, em um objeto interativo.
    
    pygame.display.update()

print('-=' * 20)
resultado()
print('-=' * 20)