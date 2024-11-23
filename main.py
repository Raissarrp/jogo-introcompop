import pygame
import sys
from config import *
from character import Character
from battle_system import BattleSystem
from ui import Button

class Game:
    """Classe principal que gerencia o jogo"""
    def __init__(self):
        pygame.init()
        self.setup_display()
        self.setup_game_assets()
        self.setup_game_state()

    def setup_display(self):
        """Configura a tela e recursos básicos"""
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sombra da Lua")
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.Font('8-BIT WONDER.TTF', FONT_SIZE)

    def setup_game_assets(self):
        """Carrega imagens e cria personagens"""
        self.imagem_fundo = pygame.image.load("imagens/DALL.webp")
        self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.img_botao = pygame.image.load("imagens/botao.png")
        
        self.personagens_disponiveis = [
            Character("DivaPop", 120, 80, 40, 70, "imagens/divapop.png", (50, 150)),
            Character("Goblin", 100, 70, 30, 50, "imagens/goblin.png", (200, 150)),
            Character("Mashal", 150, 60, 70, 50, "imagens/mashal.png", (350, 150)),
            Character("MrSax", 200, 40, 90, 80, "imagens/mrsax.png", (500, 150)),
        ]

    def setup_game_state(self):
        """Inicializa o estado do jogo"""
        self.jogando = False
        self.personagens_jogador = []
        self.personagens_inimigos = [
            Character("Goblin", 100, 70, 30, 50, "imagens/goblin.png", (700, 300)),
            Character("Goblin", 100, 70, 30, 50, "imagens/goblin.png", (800, 300)),
            Character("Goblin", 100, 70, 30, 50, "imagens/goblin.png", (900, 300)),
        ]
        self.battle_system = None

    def run(self):
        """Loop principal do jogo"""
        while True:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

    def handle_events(self):
        """Processa eventos do Pygame"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        """Atualiza o estado do jogo"""
        if not self.jogando:
            self.update_menu()
        else:
            self.update_battle()

    def update_menu(self):
        """Atualiza o menu principal"""
        botao_jogar = Button("Jogar", (SCREEN_WIDTH // 2 - 140, 300), self.img_botao)
        botao_sair = Button("Sair", (SCREEN_WIDTH // 2 - 140, 400), self.img_botao)

        if botao_jogar.is_clicked():
            self.personagens_jogador = self.selecionar_personagens()
            self.battle_system = BattleSystem(self.personagens_jogador, self.personagens_inimigos)
            self.jogando = True
        if botao_sair.is_clicked():
            pygame.quit()
            sys.exit()

    def update_battle(self):
        """Atualiza o estado da batalha"""
        if not self.battle_system:
            return

        resultado = self.battle_system.verificar_fim_batalha()
        if resultado:
            self.finalizar_batalha(resultado)
            return

        # Implementar lógica de turnos aqui

    def draw(self):
        """Renderiza todos os elementos na tela"""
        self.display.fill((0, 0, 0))
        self.display.blit(self.imagem_fundo, (0, 0))

        if not self.jogando:
            self.draw_menu()
        else:
            self.draw_battle()

    def draw_menu(self):
        """Desenha o menu principal"""
        texto = self.fonte.render("MENU PRINCIPAL", True, (255, 255, 255))
        self.display.blit(texto, (SCREEN_WIDTH // 2 - texto.get_width() // 2, 50))

        botao_jogar = Button("Jogar", (SCREEN_WIDTH // 2 - 140, 300), self.img_botao)
        botao_sair = Button("Sair", (SCREEN_WIDTH // 2 - 140, 400), self.img_botao)

        botao_jogar.draw(self.display, self.fonte)
        botao_sair.draw(self.display, self.fonte)

    def draw_battle(self):
        """Desenha a tela de batalha"""
        if not self.battle_system:
            return

        for personagem in self.personagens_jogador + self.personagens_inimigos:
            if personagem.vivo():
                personagem.draw(self.display, self.fonte)

    def selecionar_personagens(self):
        """Interface de seleção de personagens"""
        escolhidos = []
        while len(escolhidos) < 3:
            self.display.fill((0, 0, 0))
            texto = self.fonte.render(f"Escolha {3 - len(escolhidos)} personagens", True, (255, 255, 255))
            self.display.blit(texto, (SCREEN_WIDTH // 2 - texto.get_width() // 2, 50))

            for personagem in self.personagens_disponiveis:
                if personagem not in escolhidos:
                    personagem.draw(self.display, self.fonte)
                    
                    mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and \
                       personagem.pos[0] < mouse[0] < personagem.pos[0] + 100 and \
                       personagem.pos[1] < mouse[1] < personagem.pos[1] + 100:
                        escolhidos.append(personagem)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(FPS)

        return escolhidos

    def finalizar_batalha(self, resultado):
        """Finaliza a batalha e mostra o resultado"""
        self.jogando = False
        # Implementar tela de resultado aqui

if __name__ == "__main__":
    game = Game()
    game.run()