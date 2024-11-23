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

Dano = (Ataque do Atacante) × (50 / (50 + Defesa do Alvo))

- - O jogo encerra quando todos os personagens de um dos grupos são derrotados.

### Interface Gráfica

- **Área de Batalha**: Mostra os personagens dos dois grupos.
- **Menu de Ações**: Exibe opções como **Atacar** e **Defender**.
- **Indicadores de Turno**: Informa qual personagem está jogando.

### Menu Inicial

- Permite ao jogador selecionar três personagens antes de iniciar a batalha.
- Navegação através das setas do teclado e confirmação com a tecla `Z`.

---

## Requisitos de Implementação

### Obrigatórios

1. Uso de **Programação Orientada a Objetos**.
2. Implementação da **batalha** com ataque, defesa e turnos.
3. Criação de um **menu inicial** navegável.
4. Interface gráfica funcional e intuitiva.

### Extras

- **Efeitos Sonoros e Música**: Adicionar sons ao jogo.
- **Easter Eggs**: Funcionalidades ocultas criativas.
- **Ações Únicas**: Habilidades específicas para cada personagem.
- **Sistema de Tipos de Dano**: Diferenciação entre ataques físicos e mágicos.
- **Análise de Alvo**: Mostrar informações detalhadas de inimigos.

---

## Boas Práticas

- **Funções Modulares**: Divida o código em funções pequenas e coerentes.
- **Comentários**: Documente o código para facilitar a compreensão.
- **Estrutura Clara**: Organize o projeto em classes e métodos.

---

## Entrega

O trabalho será dividido em duas entregas:

1. **Sistema de Batalha**: (16/11/2024) Implementação da lógica de batalha e interface básica.
2. **Menu Inicial**: (07/12/2024) Desenvolvimento da tela inicial e integração com a batalha.

Os arquivos devem ser enviados em um **.zip**, organizados em pastas, incluindo código-fonte, imagens, sons e outros recursos utilizados.

---

## Instruções de Uso

1. Instale as dependências com:
 ```bash
 pip install pygame
