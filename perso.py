class personagem:
    def __init__(self, nome, hp, velocidade, defesa, ataque ):
        self.nome = nome
        self.hp = hp
        self.velocidade = velocidade
        self.defesa = defesa
        self.ataque = ataque

    def atacar(self, alvo):
        dano = self.ataque * ((50) / (50 + self.defesa))
        alvo.hp -= dano
        if alvo.hp <= 0:
            print(f"{alvo.nome} foi derrotado!")


        def vivo(self):
            return self.hp > 0
    
    pass