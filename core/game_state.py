import pygame

class GameState:

    def __init__(self):

        # ---------------------------------
        # ИГРОВОЕ ВРЕМЯ
        # ---------------------------------

        # 09:00
        self.time_minutes = 9 * 60

        # accumulator копит
        # реальное время
        self.time_accumulator = 0

        # ---------------------------------
        # СТАТЫ ИГРОКА
        # ---------------------------------

        self.burnout = 0

        self.suspicion = 0

