import pygame
import os
import math


PASTA_ASSETS = os.path.join(
    os.path.dirname(__file__),
    "assets"
)


rei = pygame.image.load(
    os.path.join(PASTA_ASSETS, "rei.png")
).convert_alpha()


dama = pygame.image.load(
    os.path.join(PASTA_ASSETS, "dama.png")
).convert_alpha()

FONTE = os.path.join(
    PASTA_ASSETS,
    "Rajdhani-Regular.ttf"
)

def criar_fonte(tamanho):
    return pygame.font.Font(FONTE, tamanho)

def desenhar_casa(janela, x, y, tamanho, linha, coluna):

    if (linha + coluna) % 2 == 0:
        cor = (120,110,100)
    else:
        cor = (190, 180, 165)

    pygame.draw.rect(
        janela,
        cor,
        (
            x + 4,
            y + 4,
            tamanho - 8,
            tamanho - 8
        ),
        border_radius=14
    )

    pygame.draw.rect(
        janela,
        (180, 180, 180),
        (
            x + 4,
            y + 4,
            tamanho - 8,
            tamanho - 8
        ),
        2,
        border_radius=14
    )

def desenhar_casa_usada(janela, x, y, tamanho):
    pygame.draw.rect(
        janela,
        (45, 45, 45),
        (
            x + 4,
            y + 4,
            tamanho - 8,
            tamanho - 8
        ),
        border_radius=14
    )

    pygame.draw.rect(
        janela,
        (65, 65, 65),
        (
            x + 4,
            y + 4,
            tamanho - 8,
            tamanho - 8
        ),
        2,
        border_radius=14
    )

def desenhar_rei(janela, x, y, tamanho):
    tempo = pygame.time.get_ticks()

    pulso = (math.sin(tempo * 0.003) + 1) / 2
    brilho = int(15 + pulso * 30)

    centro_x = x + tamanho // 2
    centro_y = y + tamanho // 2

    # Aura externa, contida dentro da casa
    pygame.draw.circle(
        janela,
        (
            40 + brilho // 2,
            75 + brilho,
            130 + brilho
        ),
        (centro_x, centro_y),
        43
    )

    # Aura interna
    pygame.draw.circle(
        janela,
        (
            65 + brilho // 2,
            105 + brilho,
            165 + brilho
        ),
        (centro_x, centro_y),
        38
    )

    imagem = pygame.transform.smoothscale(
        rei,
        (70, 85)
    )

    pos_x = x + (tamanho - 70) // 2
    pos_y = y + (tamanho - 85) // 2

    janela.blit(
        imagem,
        (pos_x, pos_y)
    )

def desenhar_objetivo(janela, x, y, tamanho):
    tempo = pygame.time.get_ticks()

    pulso = (math.sin(tempo * 0.003) + 1) / 2

    brilho = int(5 + pulso * 70)

    cor_externa = (
        255,
        min(255, 165 + brilho),
        20
    )

    pygame.draw.rect(
        janela,
        cor_externa,
        (
            x + 2,
            y + 2,
            tamanho - 4,
            tamanho - 4
        ),
        border_radius=18
    )

    cor_borda = (
        255,
        210 + brilho // 2 if 210 + brilho // 2 <= 255 else 255,
        min(255, 55 + brilho)
    )

    pygame.draw.rect(
        janela,
        cor_borda,
        (
            x + 5,
            y + 5,
            tamanho - 10,
            tamanho - 10
        ),
        5,
        border_radius=15
    )

def desenhar_rainha(janela, x, y, tamanho):

    centro_x = x + tamanho // 2
    centro_y = y + tamanho // 2

    # Aura da Dama
    pygame.draw.circle(
        janela,
        (255, 210, 70),
        (centro_x, centro_y),
        43
    )

    pygame.draw.circle(
        janela,
        (255, 225, 120),
        (centro_x, centro_y),
        36
    )

    imagem = pygame.transform.smoothscale(
        dama,
        (70, 85)
    )

    pos_x = x + (tamanho - 70) // 2
    pos_y = y + (tamanho - 85) // 2

    janela.blit(
        imagem,
        (pos_x, pos_y)
    )