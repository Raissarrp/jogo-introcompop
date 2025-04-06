from config import BUTTON_SIZE
import pygame

class Button:
    """Classe para criar e gerenciar botões interativos"""
    def __init__(self, text, pos, img_botao, tamanho=BUTTON_SIZE, text_color=(255, 255, 255), hover_color=(200, 200, 200)):
        self.text = text
        self.pos = pos
        self.image = pygame.transform.scale(img_botao, tamanho)
        self.rect = pygame.Rect(pos[0], pos[1], tamanho[0], tamanho[1])

    def draw(self, tela, fonte):
        """Desenha o botão e seu texto"""
        tela.blit(self.image, self.pos)
        texto = fonte.render(self.text, True, (255, 255, 255))
        pos_texto = (
            self.pos[0] + (self.rect.width - texto.get_width()) // 2,
            self.pos[1] + (self.rect.height - texto.get_height()) // 2
        )
        tela.blit(texto, pos_texto)

    def is_clicked(self):
        """Verifica se o botão foi clicado"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        return self.rect.collidepoint(mouse) and click[0]