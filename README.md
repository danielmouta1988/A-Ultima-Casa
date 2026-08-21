# ♟️ A Última Casa - Chess

**A Última Casa - Chess** é um jogo de estratégia desenvolvido em **Python + Pygame**, no qual o jogador controla um Rei em um tabuleiro 5x5 e precisa alcançar a Dama antes de ficar sem movimentos disponíveis.

O jogo combina movimentação simples, planejamento e tomada de decisão. Cada movimento altera o caminho disponível, já que uma casa utilizada não pode ser utilizada novamente.

## 🎮 Como jogar

Você começa em uma posição aleatória do tabuleiro.

Seu objetivo é:

> **Alcançar a Dama utilizando o maior número possível de casas, sem ficar preso.**

A cada movimento realizado, a casa anterior é bloqueada.

O jogo termina de duas formas:

- 🏆 **Vitória:** o Rei alcança a Dama.
- 💀 **Derrota:** o Rei fica sem nenhuma casa disponível para continuar.

## 🕹️ Controles

| Tecla | Ação |
|---|---|
| ↑ | Mover para cima |
| ↓ | Mover para baixo |
| ← | Mover para esquerda |
| → | Mover para direita |
| R | Jogar novamente após o fim da partida |

## 🏆 Ranking

O jogo possui um ranking local com os **5 melhores resultados**.

Os resultados são armazenados no arquivo:

```text
recordes.json
```

O ranking considera o número de casas percorridas e, em caso de empate, o menor tempo.

O arquivo `recordes.json` não é enviado ao GitHub, pois faz parte dos dados locais de cada jogador.

## 🧩 Estrutura do projeto

```text
A-Ultima-Casa/
│
├── assets/
│   ├── Rajdhani-Regular.ttf
│   ├── dama.png
│   └── rei.png
│
├── main.py
├── visual.py
├── .gitignore
└── recordes.json
```

### `main.py`

Responsável pela lógica principal do jogo:

- criação do tabuleiro;
- movimentação do jogador;
- controle da partida;
- vitória e derrota;
- contagem de movimentos;
- cronômetro;
- ranking.

### `visual.py`

Responsável pelos elementos visuais:

- desenho das casas;
- Rei;
- Dama;
- destaque da casa objetivo;
- fonte utilizada pelo jogo.

## ⚙️ Tecnologias

- **Python 3**
- **Pygame**
- **Git**
- **GitHub**

## 🚀 Como executar

Clone o repositório:

```bash
git clone https://github.com/danielmouta1988/A-Ultima-Casa.git
```

Entre na pasta:

```bash
cd A-Ultima-Casa
```

Instale o Pygame:

```bash
pip install pygame-ce
```

Execute o jogo:

```bash
python main.py
```

## 📌 Versão

**v1.0.0**

Primeira versão jogável do projeto, contendo:

- tabuleiro 5x5;
- movimentação do Rei;
- Dama como objetivo;
- sistema de vitória;
- sistema de derrota;
- cronômetro;
- contador de movimentos;
- ranking local;
- destaque visual da casa objetivo;
- fonte personalizada;
- interface e instruções do jogo.

## 📄 Licença

Este projeto atualmente não possui uma licença definida.

---

Desenvolvido como projeto independente em Python e Pygame.
