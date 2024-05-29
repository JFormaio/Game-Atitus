import pygame  # importando lib do pygame 
pygame.init()
tamanho  = ( 1000, 700)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Game Título")
branco  = (255,255,255)
preto = (0,0,0)
posicaoXBolinha = 0
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
    tela.fill(branco)
    #pygame.draw.line(tela, preto, (0,200), (200,200), 2)
    pygame.draw.circle(tela, preto, (posicaoXBolinha,200), 50, 5)
    posicaoXBolinha = posicaoXBolinha + 1
    #pygame.draw.rect(tela, preto, (20,50, 30, 50), 2)
    

    pygame.display.update()
    clock.tick(60)
