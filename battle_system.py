import pygame
import sys

# Definição de constantes e cores
LARGURA, ALTURA = 1024, 768
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Batalha RPG")

# Função para exibir texto na tela
def exibir_texto(tela, texto, tamanho, cor, x, y):
    fonte = pygame.font.SysFont('arial', tamanho)
    texto_renderizado = fonte.render(texto, True, cor)
    tela.blit(texto_renderizado, (x, y))

# Função para exibir a interface de batalha
def exibir_interface(tela, grupo1, grupo2, turno):
    tela.fill(PRETO)

    # Exibir informações do jogador
    for i, personagem in enumerate(grupo1, 1):
        exibir_texto(tela, f"{i}. {personagem}", 20, BRANCO, 10, i * 30 + 10)
        exibir_texto(tela, f"Vida: {personagem.vida}/{personagem.vida_max}", 20, VERDE, 10, i * 30 + 30)

    # Exibir informações do inimigo
    for i, personagem in enumerate(grupo2, 1):
        exibir_texto(tela, f"{i}. {personagem}", 20, BRANCO, LARGURA - 200, i * 30 + 10)
        exibir_texto(tela, f"Vida: {personagem.vida}/{personagem.vida_max}", 20, VERMELHO, LARGURA - 200, i * 30 + 30)

    # Exibir informações do turno
    exibir_texto(tela, f"Turno: {turno}", 30, BRANCO, LARGURA // 2, ALTURA - 50)

    pygame.display.update()

# Função para criar grupos (exemplo)
def criar_grupos():
    # Esta função deve retornar dois grupos de personagens
    # Exemplo de retorno:
    return [Personagem("Heroi", 100, 100)], [Personagem("Inimigo", 100, 100)]

# Função para o turno de batalha (exemplo)
def turno_de_batalha(grupo1, grupo2):
    # Esta função deve implementar a lógica do turno de batalha
    pass

# Classe Personagem (exemplo)
class Personagem:
    def __init__(self, nome, vida, vida_max):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida_max

    def __str__(self):
        return self.nome

# Função principal do jogo
def main():
    grupo1, grupo2 = criar_grupos()
    turno = 1

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        exibir_interface(tela, grupo1, grupo2, turno)
        turno_de_batalha(grupo1, grupo2)

        if not any(personagem.vida > 0 for personagem in grupo1):
            exibir_texto(tela, "Grupo 1 foi derrotado!", 30, VERMELHO, LARGURA // 2, ALTURA // 2)
            pygame.display.update()
            pygame.time.wait(3000)
            break
        elif not any(personagem.vida > 0 for personagem in grupo2):
            exibir_texto(tela, "Grupo 2 foi derrotado!", 30, VERDE, LARGURA // 2, ALTURA // 2)
            pygame.display.update()
            pygame.time.wait(3000)
            break

if __name__ == "__main__":
    main()