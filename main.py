from core.fonts import Fonts
import pygame
import sys
from core.game_state import GameState
import random


def office_survival():
    pygame.init()

    game_state = GameState()

    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Office Survival')
    clock = pygame.time.Clock()

    fonts = Fonts()
    fonts.fonts()




    running = True

    next_message_time = 545

    while running:
        dt = clock.tick(60) / 1000
        screen.fill((30, 40, 50))

        game_state.time_accumulator += dt
        if game_state.time_accumulator >= 1:
            game_state.time_minutes += 1
            game_state.time_accumulator -= 1

        if game_state.time_minutes >= next_message_time:
            message = random.choice(game_state.message_pool)
            game_state.active_messages.append(message)
            game_state.can_reply = True
            next_message_time += random.randint(5, 10)

        task_surface = None
        if game_state.active_messages:
            last_message = game_state.active_messages[game_state.selected_message]
            task = f'{last_message["sender"]}:{last_message["text"]}'
            task_surface = fonts.hud_font.render(task, True, (255, 255, 255))



            for index, choice in enumerate(last_message["choices"]):
                choice_text = f"{index + 1}. {choice['text']}"

                choice_surface = fonts.hud_font.render(
                    choice_text,
                    True,
                    (200, 200, 200)
                )

                # Каждая choice
                # ниже предыдущей
                #
                screen.blit(
                choice_surface,
                    (700, 500 + index * 40)
                )

                for index, message in enumerate(game_state.active_messages):
                    sender = message["sender"]
                    sender_surface = fonts.hud_font.render(sender, True, (255, 255, 255))
                    screen.blit(sender_surface, (200, 600 + index * 40))




        hours = game_state.time_minutes // 60
        minutes = game_state.time_minutes % 60
        time_text = f"{hours:02}:{minutes:02}"
        time_surface = fonts.clock_font.render(time_text,
                    True,
                    (255, 255, 255))
        burnout_text = f"Burnout: {game_state.burnout}"
        burnout_surface = fonts.hud_font.render(burnout_text,True, (255, 255, 255))

        suspicion_text = f"Suspicion: {game_state.suspicion}"
        suspicion_surface = fonts.hud_font.render(suspicion_text,True, (255, 255, 255))

        if game_state.time_minutes >= 18 * 60:
            win = f"You have survived the day!"
            win_font = fonts.ending_font.render(win, True, (255, 255, 255))
            screen.blit(win_font, (100, 100))
        elif game_state.burnout >= 100:
            lose = f"You died from anxiety!"
            lose_font = fonts.ending_font.render(lose, True, (238, 75, 43))
            screen.blit(lose_font, (100, 100))
        elif game_state.suspicion >= 100:
            fired = f"You are fired!"
            fired_font = fonts.ending_font.render(fired, True, (227, 11, 92))
            screen.blit(fired_font, (100, 100))

        for event in pygame.event.get():
            if game_state.active_messages and game_state.can_reply:
                #keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected_choice = last_message["choices"][0]
                        game_state.burnout += selected_choice["burnout"]
                        game_state.burnout = max(0, game_state.burnout)
                        game_state.suspicion += selected_choice["suspicion"]
                        game_state.suspicion = max(0, game_state.suspicion)
                        game_state.can_reply = False
                    elif event.key == pygame.K_2:
                        selected_choice = last_message["choices"][1]
                        game_state.burnout += selected_choice["burnout"]
                        game_state.burnout = max(0, game_state.burnout)
                        game_state.suspicion += selected_choice["suspicion"]
                        game_state.suspicion = max(0, game_state.suspicion)
                        game_state.can_reply = False
                    elif event.key == pygame.K_3:
                        selected_choice = last_message["choices"][2]
                        outcome = random.randint(1, 3)
                        if outcome == 1:
                            game_state.burnout -= selected_choice["burnout"]
                            game_state.burnout = max(0, game_state.burnout)
                            game_state.suspicion += selected_choice["suspicion"]
                            game_state.suspicion = max(0, game_state.suspicion)
                            reply = f'{last_message["choices"][2]["delegate"]} agreed'
                            game_state.notification.append(reply)

                        elif outcome == 2:
                            game_state.suspicion -= selected_choice["suspicion"]
                            game_state.suspicion = max(0, game_state.suspicion)
                            game_state.burnout += selected_choice["burnout"]
                            game_state.burnout = max(0, game_state.burnout)
                            reply = f'{last_message["choices"][2]["delegate"]} said he is  busy'
                            game_state.notification.append(reply)

                        else:
                            game_state.suspicion += selected_choice["suspicion"]
                            game_state.suspicion = max(0, game_state.suspicion)
                            game_state.burnout += selected_choice["burnout"]
                            game_state.burnout = max(0, game_state.burnout)
                            reply = f'{last_message["choices"][2]["delegate"]} told to manager'
                            game_state.notification.append(reply)
                        game_state.can_reply = False
                    if event.key == pygame.K_UP:
                        if game_state.selected_message < len(game_state.active_messages) - 1:
                            game_state.selected_message + 1
                    if event.key == pygame.K_DOWN:
                        if game_state.selected_message > 0:
                            game_state.selected_message - 1









            #quit the game
            if event.type == pygame.QUIT:
                running = False



        screen.blit(time_surface, (50, 50))
        screen.blit(suspicion_surface, (50, 170))
        screen.blit(burnout_surface, (50, 200))
        if task_surface:
            screen.blit(task_surface, (70, 500))
        if game_state.notification:
            answer = f'{game_state.notification[-1]}'
            reaction = fonts.ending_font.render(answer, True, (227, 11, 92))
            screen.blit(reaction, (500, 300))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    office_survival()