import sys
import pygame

class AlienInvasion:
    def __init__(self):
        """Inicialia o jogo e cria recursos do jogo"""
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alen Invasion")

    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            # observa eventos de teclado e de mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    sys.exit()
            
            # Deixa a tela desenhada mais recente visível
            pygame.display.flip()
        
            if __name__ =='__main__':
                # Cria uma instancia do jogo e executa o jogo
                ai = AlienInvasion()
                ai.run_game