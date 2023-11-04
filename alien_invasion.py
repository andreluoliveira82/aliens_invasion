import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        """Inicialia o jogo e cria recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alen Invasion")

        self.ship = Ship(self)

        # # define a cor do background
        # self.bg_color = (230, 230, 230)

    #--------------------------------------------------------------------    
    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            # observa eventos de teclado e de mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redesenha a tela a cada passagem pelo loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            # Deixa a tela desenhada mais recente visível
            pygame.display.flip()
            self.clock.tick(5)
        
            if __name__ =='__main__':
                # Cria uma instancia do jogo e executa o jogo
                ai = AlienInvasion()
                ai.run_game

    #--------------------------------------------------------------------  

new_game = AlienInvasion()
new_game.run_game()