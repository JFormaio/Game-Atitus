import pygame  # importando lib do pygame 
pygame.init()
tamanho  = ( 800, 600)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Game Título")
branco  = (255,255,255)
preto = (0,0,0)
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
    tela.fill(branco)
    pygame.draw.line(tela, preto, (0,300), (800,300), 2)
    pygame.draw.line(tela, preto, (50,100), (50,500), 2)
    pygame.draw.line(tela, preto, (50,100), (150,400), 2)
    pygame.draw.line(tela, preto, (150,400), (250,150), 2)
    pygame.draw.line(tela, preto, (250,150), (250,450), 2)
    pygame.draw.line(tela, preto, (250,450), (450,100), 2)
    pygame.draw.line(tela, preto, (450,100), (750,500), 2)

    pygame.display.update()
    clock.tick(60)