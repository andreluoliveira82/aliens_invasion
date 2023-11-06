import pygame

class MyGame:
    """..."""

    def __init__(self):
        """Inicializa os atributos da classe"""
        pygame.init()

        self.screen = pygame.display.set_mode(1366,768)

        #define a cor do background
        self.bg_color = (135, 206, 250)


new_game = MyGame()
