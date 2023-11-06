import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Classe geral para gerenciar os ativos e comportamento do jogo"""

    def __init__(self):
        """Inicialia o jogo e cria recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alen Invasion")

        self.ship = Ship(self)

    #--------------------------------------------------------------------    
    def _check_events(self):
        # responde as teclas pressionadas e a  eventos do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    #--------------------------------------------------------------------
    def _check_keydown_events(self, event):
        """Responde a teclas pressionadas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # caso o usuario pressionar a tecla 'q' encerra o jogo
        elif event.key == pygame.K_q:
            sys.exit()
    #--------------------------------------------------------------------
    def _check_keyup_events(self, event):
        """Responde a teclas soltas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    #--------------------------------------------------------------------
    def _update_screen(self):
        
        # Redesenha a tela a cada passagem pelo loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            
        # Deixa a tela desenhada mais recente visível
        pygame.display.flip()

    #--------------------------------------------------------------------
    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()          
            self.clock.tick(25)
        
            if __name__ =='__main__':
                # Cria uma instancia do jogo e executa o jogo
                ai = AlienInvasion()
                ai.run_game

    #--------------------------------------------------------------------  

new_game = AlienInvasion()
new_game.run_game()