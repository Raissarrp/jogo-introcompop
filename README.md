# IntroBattle - Trabalho Computacional 2024

Este repositório contém a implementação do **IntroBattle**, um projeto computacional baseado no desenvolvimento do sistema de batalha de um RPG, utilizando a biblioteca **Pygame**. Este trabalho foi proposto como parte do curso de programação, com foco em aplicar conceitos de **Programação Orientada a Objetos** e lógica de jogos.

---

## Sumário

- [Descrição do Projeto](#descrição-do-projeto)
- [Especificações Técnicas](#especificações-técnicas)
  - [Lógica da Batalha](#lógica-da-batalha)
  - [Interface Gráfica](#interface-gráfica)
  - [Menu Inicial](#menu-inicial)
- [Requisitos de Implementação](#requisitos-de-implementação)
  - [Obrigatórios](#obrigatórios)
  - [Extras](#extras)
- [Boas Práticas](#boas-práticas)
- [Entrega](#entrega)
- [Instruções de Uso](#instruções-de-uso)
- [Recursos Adicionais](#recursos-adicionais)

---

## Descrição do Projeto

O projeto consiste em desenvolver o sistema de batalha de um jogo RPG, onde o jogador controla três personagens contra um grupo inimigo gerenciado pelo computador. Este sistema contempla:

- Atributos básicos dos personagens: **Vida**, **Ataque**, **Defesa** e **Velocidade**.
- Combate por turnos, seguindo a ordem de velocidade dos personagens.
- Possibilidade de atacar ou defender.
- Interface gráfica para visualização dos turnos e ações.

---

## Especificações Técnicas

### Lógica da Batalha

- Cada personagem possui os atributos:
  - **Pontos de Vida (HP)**: Representa a saúde do personagem.
  - **Ataque**: Determina o dano infligido.
  - **Defesa**: Reduz o impacto do ataque inimigo.
  - **Velocidade**: Define a ordem de execução dos turnos.
- Fórmula para cálculo de dano:
