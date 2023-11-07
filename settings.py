class Settings:
    """Classe para armazenar as configurações do jogo Invasão Alienígena"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        # config da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # config da espaçonave
        self.ship_speed = 4.0

        # config. do projétil
        self.bullet_speed = 1.50
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
    #-------------------------------------------------------------

