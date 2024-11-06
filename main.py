import pygame, sys, random

pygame.init()

# Configuração da tela
largura = 1024
altura = 786
display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Sombra da Lua")

# Imagem de fundo
imagem = pygame.image.load("imagens/c6b9126928ba612211813f1c4b8dc6ec.jpg")
imagem = pygame.transform.scale(imagem, (largura, altura))

# Clock e configurações de fonte
fps = 60
clock = pygame.time.Clock()
main_menu = False
gameloop = True
jogando = False 

# Configuração de fonte e botão
def get_font(size):  # Função para carregar a fonte
    return pygame.font.Font('font.ttf', size)

fonte = get_font(24)
img_botao = pygame.image.load("imagens/cbbba.png")
img_botao = pygame.transform.scale(img_botao, (512, 393))

def img_principal():
    display.blit(imagem, (0, 0))

class Buttons:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.button = pygame.rect.Rect(self.pos[0], self.pos[1], 280, 80)

    def draw(self, tela):
        tela.blit(img_botao, self.button)
        text = fonte.render(self.text, True, (0, 0, 0))  
        tela.blit(text, (self.pos[0] + 31.5, self.pos[1] + 21))  # ajuste se necessário

    def checa_clique(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

def desenha_menu_principal():
    MENU_TEXT = get_font(100).render("MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(largura // 2, 100))
    display.blit(MENU_TEXT, MENU_RECT)
    
    # Botões do menu centralizados
    botao_menu = Buttons('Sair do Menu', (largura // 2 - 140, 400))
    jogar = Buttons('Jogar', (largura // 2 - 140, 500))

    botao_menu.draw(display)
    jogar.draw(display)
    
    
    if botao_menu.checa_clique():
        return 'sair_menu'
    elif jogar.checa_clique():
        return 'jogar'
    return None

def desenha_botao_inicio():
    button = Buttons('Menu Principal', (largura // 2 - 140, 600))
    button.draw(display)
    return button.checa_clique()

#gameloop

while gameloop:
    clock.tick(fps)
    display.fill((0, 0, 0))

    if jogando:
        display.fill((0, 0, 0))  

    elif main_menu:
        img_principal()
        acao = desenha_menu_principal()
        
        # Verificar qual botão foi clicado
        if acao == 'sair_menu':
            main_menu = False
        elif acao == 'jogar':
            jogando = True  # Inicia o jogo e mostra a tela preta

    else:
        img_principal()
        if desenha_botao_inicio():
            main_menu = True  # Abre o menu principal se o botão "Menu Principal" for clicado

    # Evento para fechar o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    pygame.display.flip()

pygame.quit()