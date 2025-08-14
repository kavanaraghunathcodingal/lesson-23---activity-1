import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game Window")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Exit loop

    screen.fill((0, 0, 0))  # Optional: fill with black
    pygame.display.flip()

pygame.quit()


            
