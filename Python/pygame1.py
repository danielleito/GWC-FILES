import pygame

#define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255, 0, 0)
BLUE = (0,0,255)

pygame.init()
size (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("MY FIRST GAME")
clock=pygame.time.Clock()
done = False

while not done:
	if event in pygame.event.get():
		if event.type=pygame.QUIT:
		done=True
screen.fill(BLUE)
pygame.display.flip()
clock.tick(60)
pygame.quit()
exit()