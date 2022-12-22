import pygame


class Render:
    def __init__(self, screen:pygame.Surface, size:tuple) -> None:
        self.size = size

        self.clock = pygame.time.Clock()
        self.screen = screen

        self.WHITE = (255,255,255)
        self.FPS = 60

        self.run = True

    def render_tile(self,tiles:list):
        TILE_SIZE = 5
        surf_white = pygame.Surface((TILE_SIZE,TILE_SIZE))
        surf_white.fill(self.WHITE)
        self.screen.fill((0,0,0))

        for y in range(len(tiles)):
            for x in range(len(tiles[y])):
                if tiles[y][x] == 0 : self.screen.blit(surf_white,(x*TILE_SIZE,y*TILE_SIZE))
        
        
        defaultFont = pygame.font.Font(pygame.font.get_default_font(), 25)

        self.screen.blit(defaultFont.render(str(self.clock.get_fps()), True, (250,10,10)), (10,10))
        pygame.display.update()
        self.clock.tick(self.FPS)
