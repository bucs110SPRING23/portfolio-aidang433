import pygame

pygame.init()


screen = pygame.display.set_mode([400,600])

pygame.draw.circle(screen,"white",[200,500],50)
pygame.draw.circle(screen,"white",[200,450],40)
pygame.draw.circle(screen,"white",[200,400],30)
pygame.display.flip()
pygame.time.wait(5000)
