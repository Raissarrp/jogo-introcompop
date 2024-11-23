import pygame

class Character:
    """
    Classe base para todos os personagens do jogo.
    Implementa atributos básicos e métodos de combate.
    """
    def __init__(self, nome, hp, velocidade, defesa, ataque, img_path, pos):
        self.nome = nome
        self.hp = hp
        self.hp_max = hp
        self.velocidade = velocidade
        self.defesa_base = defesa
        self.defesa = defesa
        self.ataque = ataque
        self.defesa_ativa = False
        self.pos = pos
        self.carregar_imagem(img_path)
        
    def carregar_imagem(self, img_path):
        """Carrega e redimensiona a imagem do personagem"""
        self.imagem = pygame.image.load(img_path)
        self.imagem = pygame.transform.scale(self.imagem, (100, 100))

    def atacar(self, alvo):
        """
        Executa um ataque contra o alvo especificado.
        Retorna uma mensagem descrevendo o resultado do ataque.
        """
        dano = self.calcular_dano(alvo)
        alvo.receber_dano(dano)
        return f"{self.nome} atacou {alvo.nome} causando {int(dano)} de dano!"

    def calcular_dano(self, alvo):
        """Calcula o dano baseado na fórmula especificada"""
        return self.ataque * (BASE_DEFENSE / (BASE_DEFENSE + alvo.defesa))

    def receber_dano(self, dano):
        """Processa o dano recebido"""
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0

    def defender(self):
        """Ativa estado de defesa, duplicando a defesa"""
        if not self.defesa_ativa:
            self.defesa *= DEFENSE_MULTIPLIER
            self.defesa_ativa = True
        return f"{self.nome} está em posição defensiva!"

    def cancelar_defesa(self):
        """Cancela o estado de defesa"""
        if self.defesa_ativa:
            self.defesa = self.defesa_base
            self.defesa_ativa = False

    def draw(self, tela, fonte):
        """Desenha o personagem e sua barra de vida"""
        # Desenha o personagem
        tela.blit(self.imagem, self.pos)
        
        # Desenha a barra de vida
        self.desenhar_barra_vida(tela)
        
        # Desenha o nome e HP
        texto = fonte.render(f"{self.nome}: {int(self.hp)}/{self.hp_max}", True, (255, 255, 255))
        tela.blit(texto, (self.pos[0], self.pos[1] + 110))

    def desenhar_barra_vida(self, tela):
        """Desenha uma barra de vida com cores dinâmicas"""
        largura_barra = 100
        altura_barra = 10
        x = self.pos[0]
        y = self.pos[1] - 15
        
        # Barra de fundo (vermelha)
        pygame.draw.rect(tela, (255, 0, 0), (x, y, largura_barra, altura_barra))
        
        # Barra de vida atual (verde)
        vida_percentual = max(0, self.hp / self.hp_max)
        largura_vida = int(largura_barra * vida_percentual)
        pygame.draw.rect(tela, (0, 255, 0), (x, y, largura_vida, altura_barra))

    def vivo(self):
        """Verifica se o personagem ainda está vivo"""
        return self.hp > 0