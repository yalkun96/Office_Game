import pygame

class Fonts:
    def __init__(self):
        pygame.font.init()

    def fonts(self):
        self.clock_font = pygame.font.Font(None, 50)
        self.hud_font = pygame.font.Font(None, 30)
        self.ending_font = pygame.font.Font(None, 60)