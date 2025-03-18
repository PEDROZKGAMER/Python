import pygame

# Inicializar o Pygame
pygame.init()

# Configurar a janela
LARGURA, ALTURA = 626, 626
janela = pygame.display.set_mode([LARGURA, ALTURA])
pygame.display.set_caption('Próximo Game')

# Carregar as imagens
imagem_fundo = pygame.image.load('C:/Users/p1097.DESKTOP-7B8R317/OneDrive/Documentos/Python/JOGOS/proximo jogo/vector-de-videogame-com-ceu-azul-em-fundo_1299084-7489.png')
player = pygame.image.load('C:/Users/p1097.DESKTOP-7B8R317/OneDrive/Documentos/Python/JOGOS/proximo jogo/png-clipart-mario-mario-removebg-preview.png')

# Configuração do player
posi_x_play = 100
posi_y_play = 455
velocidade_play = 10
player_redimensionado = pygame.transform.scale(player, (100, 100))

# Configuração do relógio (FPS)
clock = pygame.time.Clock()

# Loop principal
loop = True
while loop:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            loop = False

    # Verificar teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Movimento vertical
    if teclas[pygame.K_UP] and posi_y_play > 300:  # Limite superior
        posi_y_play -= velocidade_play
    if teclas[pygame.K_DOWN] and posi_y_play < ALTURA - 175:  # Limite inferior
        posi_y_play += velocidade_play

    # Movimento horizontal
    if teclas[pygame.K_LEFT] and posi_x_play > 0:  # Limite esquerdo
        posi_x_play -= velocidade_play
    if teclas[pygame.K_RIGHT] and posi_x_play < LARGURA - 100:  # Limite direito
        posi_x_play += velocidade_play

    # Desenhar o fundo
    janela.blit(imagem_fundo, (0, 0))

    # Desenhar o player
    janela.blit(player_redimensionado, (posi_x_play, posi_y_play))

    # Atualizar a tela
    pygame.display.update()

    # Controlar a taxa de quadros (FPS)
    clock.tick(30)

# Encerrar o Pygame
pygame.quit()
