import pygame, sys, random
from perso import personagem

pygame.init()

# Configuração da tela
largura = 1024
altura = 768
display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sombra da Lua")

# Imagem de fundo
imagem = pygame.image.load("imagens\DALL.webp")
imagem = pygame.transform.scale(imagem, (largura, altura))

# Clock e configurações f ou t
fps = 60
clock = pygame.time.Clock()
main_menu = False
gameloop = True
jogando = False 

# Configuração de fonte e botão
def get_font(size): 
    return pygame.font.Font('8-BIT WONDER.TTF', size)

fonte = get_font(20)
img_botao = pygame.image.load("imagens\Quit Rect (1).png")
img_botao = pygame.transform.scale(img_botao, (200, 60))## ajustar a merda da imagem q ta toda fudida tambem 

def img_principal():
    display.blit(imagem, (0, 0))

class Buttons: # ajustar esse negocio dos botoes q ta uma merda
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.button = pygame.rect.Rect(self.pos[0], self.pos[1], 280, 80)

    def draw(self, tela):
        tela.blit(img_botao, self.button)
        text = fonte.render(self.text, True, (0, 0, 0))  
        tela.blit(text, (self.pos[0] + 31.5, self.pos[1] + 21))  # ajustar isso aq

    def checa_clique(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

def desenha_menu_principal():
    textoMenu = get_font(100).render("MENU", True, "#b68f40")
    menuCent = textoMenu.get_rect(center=(largura // 2, 100))
    display.blit(textoMenu, menuCent)
    
    # botoes menu 
    botao_menu = Buttons('Sair', (largura // 2 - 140, 500))
    jogar = Buttons('Jogar', (largura // 2 - 140, 400))
    

    botao_menu.draw(display)
    jogar.draw(display)
    
    
    if jogar.checa_clique():
        return 'jogar'
    if botao_menu.checa_clique():
        return 'sair_menu'
    return None

class Personagem:
    def __init__(self, nome, hp, velocidade, defesa, ataque, img_per, pos):
        self.nome = nome
        self.hp = hp
        self.velocidade = velocidade
        self.defesa = defesa
        self.ataque = ataque
        self.img_per = pygame.image.load(img_per)  
        self.img_per = pygame.transform.scale(self.img_per, (100, 100))  
        self.pos = pos

    def atacar(self, alvo):
        dano = self.ataque * (50 / (50 + alvo.defesa))
        alvo.hp -= dano
        if alvo.hp <= 0:
            print(f"{alvo.nome} foi derrotado!")

    def vivo(self):
        return self.hp > 0

    def draw(self, tela):
        tela.blit(self.img_per, self.pos)
        text = fonte.render(self.nome, True, (0, 0, 0))
        tela.blit(text, (self.pos[0], self.pos[1] + 110))

#personagens
personagem1 = Personagem(
    nome="Lux",
    hp=120,
    velocidade=80,
    defesa=40,
    ataque=70,
    img_per="imagens/divapop.jpg",
    pos=(50, 50),
)

personagem2 = Personagem(
    nome="Lucas",
    hp=150,
    velocidade=60,
    defesa=70,
    ataque=50,
    img_per="imagens/mashal.png",
    pos=(200, 50),
)

personagem3 = Personagem(
    nome="Marco",
    hp=200,
    velocidade=40,
    defesa=90,
    ataque=80,
    img_per="imagens/mrsax.jpg",
    pos=(350, 50),
)

personagem4 = Personagem(
    nome="Ogro",
    hp=100,
    velocidade=100,
    defesa=30,
    ataque=60,
    img_per="imagens/goblin.jpg",
    pos=(500, 50),
)

personagens = [personagem1, personagem2, personagem3, personagem4 ]

#gameloop

while gameloop:
    clock.tick(fps)
    display.fill((0, 0, 0)) 
    if jogando:
        for personagem in personagens:
            personagem.draw(display)
        

    elif main_menu:
        img_principal()
        acao = desenha_menu_principal()
        
        if acao == 'sair_menu':
            gameloop = False
        elif acao == 'jogar':
            jogando = True  

    else:
        img_principal()
        if desenha_menu_principal():
            main_menu = True  


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    pygame.display.flip() 
    