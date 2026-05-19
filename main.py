

import pygame
import sys

from pygame import font

from core.game_state import GameState


def office_survival():
    pygame.init()

    game_state = GameState()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Office Survival')
    clock = pygame.time.Clock()

    clock_font = pygame.font.Font(None, 50)
    hud_font = pygame.font.Font(None, 30)


    running = True

    while running:
        dt = clock.tick(60) / 1000

        game_state.time_accumulator += dt
        if game_state.time_accumulator >= 1:
            game_state.time_minutes += 1
            game_state.time_accumulator -= 1

        hours = game_state.time_minutes // 60
        minutes = game_state.time_minutes % 60
        time_text = f"{hours:02}:{minutes:02}"
        time_surface = clock_font.render(time_text,
                    True,
                    (255, 255, 255))
        burnout_text = f"Burnout:{game_state.burnout}"
        burnout_surface = hud_font.render(burnout_text,True, (255, 255, 255))

        suspicion_text = f"Suspicion:{game_state.suspicion}"
        suspicion_surface = hud_font.render(suspicion_text,True, (255, 255, 255))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((30, 40, 50))
        screen.blit(time_surface, (50, 50))
        screen.blit(suspicion_surface, (50, 170))
        screen.blit(burnout_surface, (50, 200))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    office_survival()