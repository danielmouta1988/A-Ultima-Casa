import pygame
import random
import os
import json

pygame.init()

LARGURA = 600
ALTURA = 680

janela = pygame.display.set_mode((LARGURA, ALTURA))

import visual

pygame.display.set_caption("A Última Casa - Chess")

ALTURA_HUD = 80

rodando = True

TAMANHO_CASA = 100

jogador_linha = random.randint(0, 4)
jogador_coluna = random.randint(0, 4)
ultima_casa_linha = random.randint(0, 4)
ultima_casa_coluna = random.randint(0, 4)

while (
    ultima_casa_linha == jogador_linha
    and ultima_casa_coluna == jogador_coluna):
    ultima_casa_linha = random.randint(0, 4)
    ultima_casa_coluna = random.randint(0, 4)

venceu = False
perdeu = False
tem_saida = False
movimentos = 0
tempo_inicio = 0
tempo_final = 0

ARQUIVO_RECORDE = os.path.join(
    os.path.dirname(__file__),
    "recordes.json"
) 
recordes = []

def carregar_recordes():
    try:
        with open(ARQUIVO_RECORDE, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_recordes():
    with open(ARQUIVO_RECORDE, "w", encoding="utf-8") as arquivo:
        json.dump(recordes, arquivo, ensure_ascii=False, indent=4)

def criar_mapa():
    return [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True]
    ]

tabuleiro = criar_mapa()
recordes = carregar_recordes()

def registrar_recorde():
    global recordes

    resultado = [movimentos, tempo_jogo]

    recordes.append(resultado)

    recordes.sort(
        key=lambda resultado: (-resultado[0], resultado[1])
    )

    recordes = recordes[:5]

    salvar_recordes()

def reiniciar_jogo():
    global jogador_linha
    global jogador_coluna
    global tabuleiro
    global venceu
    global perdeu
    global tem_saida
    global movimentos
    global ultima_casa_linha
    global ultima_casa_coluna
    global tempo_inicio
    global tempo_final



    jogador_linha = random.randint(0, 4)
    jogador_coluna = random.randint(0, 4)
    tabuleiro = criar_mapa()

    ultima_casa_linha = random.randint(0, 4)
    ultima_casa_coluna = random.randint(0, 4)

    while (
        ultima_casa_linha == jogador_linha
        and ultima_casa_coluna == jogador_coluna
    ):
        ultima_casa_linha = random.randint(0, 4)
        ultima_casa_coluna = random.randint(0, 4)


    venceu = False
    perdeu = False
    tem_saida = False
    movimentos = 0
    tempo_inicio = pygame.time.get_ticks()
    tempo_final = 0
    
  
while rodando:

    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r and (venceu or perdeu):
                reiniciar_jogo()
                
        if evento.type == pygame.KEYDOWN and not venceu and not perdeu:

            linha_anterior = jogador_linha
            coluna_anterior = jogador_coluna

            moveu = False 

            if evento.key == pygame.K_UP:
                if jogador_linha > 0:
                    if tabuleiro[jogador_linha - 1][jogador_coluna ]:
                        jogador_linha -= 1
                        moveu = True

            if evento.key == pygame.K_DOWN:
                if jogador_linha < 4:
                    if tabuleiro[jogador_linha + 1][jogador_coluna]:
                        jogador_linha += 1
                        moveu = True

            if evento.key == pygame.K_LEFT:
                if jogador_coluna > 0:
                    if tabuleiro[jogador_linha][jogador_coluna - 1]:
                        jogador_coluna -= 1
                        moveu = True

            if evento.key == pygame.K_RIGHT:
                if jogador_coluna < 4:
                   
                    if tabuleiro[jogador_linha][jogador_coluna + 1]:
                        jogador_coluna += 1
                        moveu = True

            if moveu:
                tabuleiro[linha_anterior][coluna_anterior] = False
                movimentos += 1
    tem_saida = False
    
    #cima
    if jogador_linha > 0:
        if tabuleiro[jogador_linha - 1][jogador_coluna]:
            tem_saida = True

    #baixo
    if jogador_linha < 4:
        if tabuleiro[jogador_linha + 1][jogador_coluna]:
            tem_saida = True
            
    #esquerda
    if jogador_coluna > 0:
        if tabuleiro[jogador_linha][jogador_coluna - 1]:
            tem_saida = True
            
    #direita
    if jogador_coluna < 4:
        if tabuleiro[jogador_linha][jogador_coluna + 1]:
            tem_saida = True

    if jogador_linha == ultima_casa_linha and jogador_coluna == ultima_casa_coluna:
        if not venceu:
            venceu = True
            tempo_final = pygame.time.get_ticks()
            tempo_jogo = (tempo_final - tempo_inicio) / 1000
            registrar_recorde()

    if not tem_saida and not venceu:
        if not perdeu:
            perdeu = True
            tempo_final = pygame.time.get_ticks()

    if venceu or perdeu:
        tempo_jogo = (tempo_final - tempo_inicio) / 1000
    else:
        tempo_atual = pygame.time.get_ticks()
        tempo_jogo = (tempo_atual - tempo_inicio) / 1000

    janela.fill((20, 20, 20))
    pygame.draw.line(
        janela,
        (70, 70, 70),
        (10, ALTURA_HUD - 1),
        (590, ALTURA_HUD - 1),
        1
    )

    for linha in range(5):

        for coluna in range(5):

            x = coluna * TAMANHO_CASA
            y = ALTURA_HUD + linha * TAMANHO_CASA

            if tabuleiro[linha][coluna]:

                visual.desenhar_casa(
                    janela,
                    x,
                    y,
                    TAMANHO_CASA,
                    linha,
                    coluna
                )
            else:
                visual.desenhar_casa_usada(
                    janela,
                    x,
                    y,
                    TAMANHO_CASA
                )
            
    x_jogador = jogador_coluna * TAMANHO_CASA
    y_jogador = ALTURA_HUD + jogador_linha * TAMANHO_CASA

    visual.desenhar_rei(
        janela,
        x_jogador,
        y_jogador,
        TAMANHO_CASA
    )
    x_ultima_casa = ultima_casa_coluna * TAMANHO_CASA
    y_ultima_casa = ALTURA_HUD + ultima_casa_linha * TAMANHO_CASA


    visual.desenhar_objetivo(
        janela,
        x_ultima_casa,
        y_ultima_casa,
        TAMANHO_CASA
    )
    visual.desenhar_rainha(
        janela,
        x_ultima_casa,
        y_ultima_casa,
        TAMANHO_CASA
    )

    if venceu:
        camada = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
        camada.fill((20, 20, 20, 150))
        janela.blit(camada, (0, 0))

        fonte_titulo = visual.criar_fonte(60)
        fonte_resultado = visual.criar_fonte(32)
        fonte_info = visual.criar_fonte(24)

        texto = fonte_titulo.render(
            "VOCÊ VENCEU!",
            True,
            (218, 165, 32)
        )

        resultado = fonte_resultado.render(
            f"{movimentos} CASAS  |  {tempo_jogo:.2f}s",
            True,
            (255, 255, 255)
        )

        instrução = fonte_info.render(
            "R  |  JOGAR NOVAMENTE",
            True,
            (180, 180, 180)
        )

        janela.blit(
            texto,
            (
                (LARGURA - texto.get_width()) // 2,
                245
            )
        )

        janela.blit(
            resultado,
            (
                (LARGURA - resultado.get_width()) // 2,
                315
            )
        )

        janela.blit(
            instrução,
            (
                (LARGURA - instrução.get_width()) // 2,
                365
            )
        )

    if perdeu:
        camada = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
        camada.fill((20, 20, 20, 150))
        janela.blit(camada, (0, 0))

        fonte_titulo = visual.criar_fonte(48)
        fonte_resultado = visual.criar_fonte(32)
        fonte_info = visual.criar_fonte(24)

        texto = fonte_titulo.render(
            "VOCÊ PERDEU!",
            True,
            (180, 70, 70)
        )

        resultado = fonte_resultado.render(
            f"{movimentos} CASAS  |  {tempo_jogo:.2f}s",
            True,
            (255, 255, 255)
        )

        instrucao = fonte_info.render(
            "R  |  TENTAR NOVAMENTE",
            True,
            (180, 180, 180)
        )

        janela.blit(
            texto,
            (
                (LARGURA - texto.get_width()) // 2,
                245
            )
        )

        janela.blit(
            resultado,
            (
                (LARGURA - resultado.get_width()) // 2,
                315
            )
        )

        janela.blit(
            instrucao,
            (
                (LARGURA - instrucao.get_width()) // 2,
                365
            )
        )

    fonte_rotulo = visual.criar_fonte(18)
    fonte_valor = visual.criar_fonte(32)

    texto_movimentos_rotulo = fonte_rotulo.render(
        "MOVIMENTOS",
        True,
        (150, 150, 150)
    )

    texto_movimentos_valor = fonte_valor.render(
        str(movimentos),
        True,
        (230, 230, 230)
    )

    janela.blit(
        texto_movimentos_rotulo,
        (15, 8)
    )

    janela.blit(
        texto_movimentos_valor,
        (15, 28)
    )


    texto_tempo_rotulo = fonte_rotulo.render(
        "TEMPO",
        True,
        (150, 150, 150)
    )

    texto_tempo_valor = fonte_valor.render(
        f"{tempo_jogo:.2f}s",
        True,
        (230, 230, 230)
    )

    janela.blit(
        texto_tempo_rotulo,
        (180, 8)
    )

    janela.blit(
        texto_tempo_valor,
        (180, 28)
    )

    fonte_ranking = visual.criar_fonte(12)

    for posicao, (casas, tempo) in enumerate(recordes):
        texto_ranking = fonte_ranking.render(
            f"{posicao + 1}º  {casas} casas | {tempo:.2f}s",
            True,
            (190, 190, 190)
        )

        janela.blit(
            texto_ranking,
            (380, 15 + posicao * 12)
        )
    pygame.draw.line(
        janela,
        (80, 80, 80),
        (20, 590),
        (580, 590),
        1
    )

    fonte_instrucoes = visual.criar_fonte(20)

    texto_instrucoes = fonte_instrucoes.render(
        "Setas Mover     •     R  Reiniciar após o fim",
        True,
        (180, 180, 180)
    )

    janela.blit(
        texto_instrucoes,
        (
            (LARGURA - texto_instrucoes.get_width()) // 2,
            605
        )
    )

    texto_objetivo = fonte_instrucoes.render(
        "Objetivo: alcance a Dama sem voltar às casas percorridas.",
        True,
        (130, 130, 130)
    )

    janela.blit(
        texto_objetivo,
        (
            (LARGURA - texto_objetivo.get_width()) // 2,
            635
        )
    )
    pygame.display.flip()



pygame.quit()


