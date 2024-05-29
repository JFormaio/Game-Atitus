import pygame
pygame.init()
tamanho  = ( 600, 400)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Game Título")
branco  = (255,255,255)
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
    
    tela.fill(branco)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
