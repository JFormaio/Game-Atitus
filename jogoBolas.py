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
    pygame.draw.line(tela, preto, (100,50), (250,400), 2)
    pygame.draw.line(tela, preto, (250,400), (500,300), 2)
    pygame.draw.line(tela, preto, (500,275), (700,275), 2)
    pygame.draw.circle(tela, branco, (100,50), 50, 0)
    pygame.draw.circle(tela, preto, (100,50), 50, 5)
    pygame.draw.circle(tela, branco, (250,400), 50, 0)
    pygame.draw.circle(tela, preto, (250,400), 50, 5)
    pygame.draw.circle(tela, branco, (475,275), 50, 0)
    pygame.draw.circle(tela, preto, (475,275), 50, 5)
    pygame.draw.circle(tela, branco, (700,275), 50, 0)
    pygame.draw.circle(tela, preto, (700,275), 50, 5)

    pygame.display.update()
    clock.tick(60)