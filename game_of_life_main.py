import pygame
import sys

pygame.init()

cellsize: int = 20

W, H = 30, 30

fps = 60

if ("-cellsize") in sys.argv:

	cellsize = int(sys.argv[sys.argv.index("-cellsize") + 1])

if ("-geometry") in sys.argv:

	V = (sys.argv[sys.argv.index("-geometry") + 1])

	V = V.lower()

	l, r = V.split("x")

	W = int(l)
	H = int(r)

if ("-fps") in sys.argv:

	fps = int(sys.argv[sys.argv.index("-fps") + 1])


grid: list[list[bool]] = [[False for i in range(W)] for j in range(H)]

screen = pygame.display.set_mode((W*cellsize, H*cellsize))

running = True

clock = pygame.time.Clock()

def redraw():

	screen.fill((0xFF, 0xFF, 0xFF))

	for y in range(H):
		for x in range(W):

			if grid[y][x]:
				pygame.draw.rect(screen, (0x0, 0xff, 0x0), (x * cellsize, y * cellsize, cellsize, cellsize))
			else:
				pygame.draw.rect(screen, (128, 128, 128), (x * cellsize, y * cellsize, cellsize, cellsize), 1)


	pygame.display.update()

choosing = True

while (running):


	clock.tick(fps)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False


	if choosing:

		mstate = pygame.mouse.get_pressed()
		mx, my = pygame.mouse.get_pos()

		if mstate[0]:

			grid[my//cellsize][mx//cellsize] = True

		if mstate[2]:

			grid[my//cellsize][mx//cellsize] = False

		if mstate[1]:

			choosing = False


	else:

		pass


	redraw()



