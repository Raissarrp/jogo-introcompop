import pygame

class Personagem:
    def __init__(self, nome, vida, ataque, defesa, agilidade, classe):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.agilidade = agilidade
        self.classe = classe
        self.vida_max = vida
        self.defesa_fisica = defesa
        self.defesa_magica = defesa

    def atacar(self, defensor):
        """Calcula o dano de ataque e subtrai da vida do defensor."""
        if self.classe == "Mago":
            dano = max(0, self.ataque - defensor.defesa_magica)
        else:
            dano = max(0, self.ataque - defensor.defesa_fisica)
        defensor.vida -= dano

    def __str__(self):
        return f"{self.nome} - Vida: {self.vida}/{self.vida_max} - Classe: {self.classe}"

class Guerreiro(Personagem):
    def __init__(self, nome, vida=100, ataque=20, defesa=10, agilidade=5):
        super().__init__(nome, vida, ataque, defesa, agilidade, "Guerreiro")

class Mago(Personagem):
    def __init__(self, nome, vida=80, ataque=15, defesa=5, agilidade=15):
        super().__init__(nome, vida, ataque, defesa, agilidade, "Mago")

    def ataque_especial(self, alvo):
        """Ataque mágico que causa dano a todos os inimigos."""
        dano_extra = 20
        for inimigo in self.inimigos:
            dano = self.ataque + dano_extra - inimigo.defesa_magica
            inimigo.vida -= dano

class Curandeiro(Personagem):
    def __init__(self, nome, vida=70, ataque=10, defesa=8, agilidade=12):
        super().__init__(nome, vida, ataque, defesa, agilidade, "Curandeiro")

    def curar(self, aliado):
        """Restaura uma quantidade fixa de vida do aliado."""
        cura = 20
        aliado.vida = min(aliado.vida + cura, aliado.vida_max)

class Ladino(Personagem):
    def __init__(self, nome, vida=90, ataque=18, defesa=6, agilidade=18):
        super().__init__(nome, vida, ataque, defesa, agilidade, "Ladino")

    def ataque_critico(self, alvo):
        """Causa dano extra baseado na vida atual do alvo."""
        dano_extra = int(alvo.vida * 0.10)
        dano = self.ataque + dano_extra - alvo.defesa_fisica
        alvo.vida -= dano

# Atribuição de personagens
esqueleto = Guerreiro("Esqueleto", vida=120, ataque=18)
goblin = Mago("Goblin", vida=90, ataque=12, defesa=3)
um = Curandeiro("Um", vida=60, ataque=8, agilidade=18)
divapop = Mago("Divapop", vida=75, ataque=18, defesa=6)
mrsax = Guerreiro("Mrsax", vida=110, ataque=22, defesa=8)
mashal = Curandeiro("Mashal", vida=80, ataque=9, cura=20)
ladino = Ladino("Ladino", vida=95, ataque=16, defesa=4)

def criar_grupos():
    """Cria e retorna dois grupos de personagens."""
    grupo1 = [esqueleto, goblin, um]
    grupo2 = [divapop, mrsax, mashal, ladino]
    return grupo1, grupo2

def turno_de_batalha(grupo1, grupo2):
    """Gerenciador de turnos de batalha."""
    grupo1.sort(key=lambda x: x.agilidade, reverse=True)
    grupo2.sort(key=lambda x: x.agilidade, reverse=True)

    for personagem in grupo1:
        if personagem.vida > 0:
            for inimigo in grupo2:
                if inimigo.vida > 0:
                    personagem.atacar(inimigo)
                    if inimigo.vida <= 0:
                        print(f"{inimigo} foi derrotado!")
                        grupo2.remove(inimigo)
                        break
            print(f"{personagem} atacou!")

    for personagem in grupo2:
        if personagem.vida > 0:
            for inimigo in grupo1:
                if inimigo.vida > 0:
                    personagem.atacar(inimigo)
                    if inimigo.vida <= 0:
                        print(f"{inimigo} foi derrotado!")
                        grupo1.remove(inimigo)
                        break
            print(f"{personagem} contra-atacou!")

    print("\n---------- Próximo Turno ----------\n")

def exibir_menu_inicial():
    """Exibe o menu inicial e permite ao jogador escolher os personagens."""
    print("Bem-vindo ao jogo de batalha!")
    print("Selecione os personagens para cada grupo:")
    
    grupo1 = []
    grupo2 = []
    
    while len(grupo1) < 3 or len(grupo2) < 3:
        print("\nGrupo 1:")
        for i, personagem in enumerate(grupo1, 1):
            print(f"{i}. {personagem}")
        print("\nGrupo 2:")
        for i, personagem in enumerate(grupo2, 1):
            print(f"{i}. {personagem}")
        
        escolha = input("Escolha um personagem (1-9) ou digite 'batalha' para iniciar: ")
        
        if escolha.isdigit():
            indice = int(escolha) - 1
            if indice < 6:
                if indice < 3:
                    grupo1.append(criar_personagem(indice))
                else:
                    grupo2.append(criar_personagem(indice - 3))
            else:
                print("Escolha inválida.")
        elif escolha.lower() == 'batalha':
            break
        else:
            print("Entrada inválida. Por favor, digite um número de 1 a 9 ou 'batalha'.")

def criar_personagem(indice):
    """Cria um personagem com base no índice fornecido."""
    personagens = [esqueleto, goblin, um, divapop, mrsax, mashal, ladino]
    return personagens[indice]

def iniciar_jogo():
    grupo1, grupo2 = criar_grupos()
    exibir_menu_inicial()
    
    while True:
        turno_de_batalha(grupo1, grupo2)

        if not any(personagem.vida > 0 for personagem in grupo1):
            print("Grupo 1 foi derrotado!")
            break
        elif not any(personagem.vida > 0 for personagem in grupo2):
            print("Grupo 2 foi derrotado!")
            break

# Iniciar o jogo
iniciar_jogo()