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
    
    pygame.display.update()
    clock.tick(60)
