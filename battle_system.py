import random

class BattleSystem:
    """Gerencia a lógica de batalha do jogo"""
    def __init__(self, personagens_jogador, personagens_inimigos):
        self.personagens_jogador = personagens_jogador
        self.personagens_inimigos = personagens_inimigos
        self.todos_personagens = personagens_jogador + personagens_inimigos
        self.turno_atual = 0
        self.mensagens = []

    def ordenar_turnos(self):
        """Ordena os personagens por velocidade"""
        return sorted(
            [p for p in self.todos_personagens if p.vivo()],
            key=lambda x: x.velocidade,
            reverse=True
        )

    def executar_turno_ia(self, personagem):
        """Executa o turno de um personagem controlado pela IA"""
        alvos_vivos = [p for p in self.personagens_jogador if p.vivo()]
        if not alvos_vivos:
            return None
            
        alvo = random.choice(alvos_vivos)
        # 20% de chance de defender
        if random.random() < 0.2:
            return personagem.defender()
        else:
            return personagem.atacar(alvo)

    def verificar_fim_batalha(self):
        """Verifica se a batalha terminou"""
        jogador_vivo = any(p.vivo() for p in self.personagens_jogador)
        inimigos_vivos = any(p.vivo() for p in self.personagens_inimigos)
        
        if not jogador_vivo:
            return "derrota"
        elif not inimigos_vivos:
            return "vitoria"
        return None