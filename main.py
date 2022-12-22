import pygame
import render
from ca import *

pygame.init()

def main():
    screen = pygame.display.set_mode((800,800))
    Map = create_random_list((40*2,40*2), .5, "lkdfjld")

    renderer = render.Render(screen,(800,800))

    while renderer.run:
        renderer.render_tile(Map)
        for event in pygame.event.get():
            # joueur quitte ?
            if event.type == pygame.QUIT:
                pygame.quit()
                renderer.run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    Map = ca_moore_neighborhood(Map,5)
                if event.key == pygame.K_r:
                    Map = create_random_list((40*4,40*4), .5, rand.random())





if __name__ == "__main__":
    main()
    pygame.quit()
