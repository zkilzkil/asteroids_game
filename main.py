import pygame
from constants import *
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
if __name__ == "__main__":
	for event in pygame.event.get():
    	if event.type == pygame.QUIT:
        	return
	run_program = True
	while run_program:
		screen.fill((0, 0, 0))
		pygame.display.flip()
	main()
