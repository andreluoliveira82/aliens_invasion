import pygame

class Ship:
    """Classe para cuidar da espaçonave"""
    
    def __init__(self, ai_game):
        """inicializa a espaçonave e defina sua posição inicial"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()


        # sobe a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Começa cada espaconave no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # armazena um float para a posição horizontal exata da espaçonave
        self.x = float(self.rect.x)

        # começa com uma espaçonave que não está se movendo
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Atualiza a posição da espaçonave com base na flag de movimento"""

        # atualiza o valor de x da espaçonave, não o rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        
        # Atualiza o objeto rect de self.x
        self.rect.x = self.x


    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.screen.blit(self.image, self.rect)
