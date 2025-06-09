import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	my_clock = pygame.time.Clock()
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updateable, drawable)
	Asteroid.containers = (updateable, drawable)
	AsteroidField.containers = (updateable)
	player = Player(x, y)
	asteroid_field = AsteroidField()

	while True:
		screen.fill((0, 0, 0))
		updateable.update(dt)
		for draw in drawable:
			draw.draw(screen)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return	
		dt = my_clock.tick(60) / 1000

if __name__ == "__main__":
	main()
