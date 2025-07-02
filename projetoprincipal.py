#importa os módulos com as regras de movimento de cada peça

import peao
import cavalo
import torre
import bispo
import rainha

#função que exibe o tabuleiro 

def matriz_tabuleiro(tabuleiro):
    print("\n  1  2  3  4  5  6  7  8")  #colunas representas visualmente atráves de um print
    for i in range(8):      # for percorre as linhas                                      
        linha = str(i + 1) + " "  #usado para numerar cada linha a partir de 1  (+ " " é para dar espaçamento a cada caractere)
        for j in range(8):     #for percorre as colunas
            linha += tabuleiro[i][j] + " "      #adiciona a peça ou -- na linha
        print(linha)                            #imprime a linha 

#tabuleiro
tabuleiro = [
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["PB", "PB", "PB", "PB", "PB", "PB", "PB", "PB"],
    ["TB", "CB", "BB", "KB", "QB", "BB", "CB", "TB"]
]

#inputs
while True:
    matriz_tabuleiro(tabuleiro)                                     #chama a função e exibe o tabuleiro 
    peca = input("\nQual peça deseja mover?: ").upper()             #nome da peça
    origem_linha = int(input("Linha de origem (1-8): ")) - 1        # o -1 serve para a conversão do índice
    origem_coluna = int(input("Coluna de origem (1-8): ")) - 1
    destino_linha = int(input("Linha de destino (1-8): ")) - 1
    destino_coluna = int(input("Coluna de destino (1-8): ")) - 1

    if peca == "PB":
        if peao.movimento_peao(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):  #chama a função e faz a verificação
            tabuleiro[destino_linha][destino_coluna] = "PB"     #atualiza e move o peão caso o movimento seja válido
            tabuleiro[origem_linha][origem_coluna] = "--"       #atualiza a linha e a coluna de origem para vazia
        else:
            print("\nMovimento inválido para o Peão!")

    elif peca == "TB":
        if torre.movimento_torre(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):        #torre branca
            tabuleiro[destino_linha][destino_coluna] = "TB"
            tabuleiro[origem_linha][origem_coluna] = "--"
        else:
            print("\nMovimento inválido para a Torre!")

    elif peca == "CB":
        if cavalo.movimento_cavalo(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):      #cavalo branco
            tabuleiro[destino_linha][destino_coluna] = "CB"
            tabuleiro[origem_linha][origem_coluna] = "--"
        else:
            print("\nMovimento inválido para o Cavalo!")

    elif peca == "BB":
        if bispo.movimento_bispo(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):        #bispo branco
            tabuleiro[destino_linha][destino_coluna] = 'BB'
            tabuleiro[origem_linha][origem_coluna] = '--'
        else:
            print('\nMovimento inválido para o Bispo!')

    elif peca == "KB":      #rei branco (ainda não implementado)
        print('')

    elif peca == "QB":
        if rainha.movimento_rainha(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):      #rainha branca
            tabuleiro[destino_linha][destino_coluna] = 'QB'
            tabuleiro[origem_linha][origem_coluna] = '--'
        else:
            print('\nMovimento inválido para a Rainha!')

    else:
        print("\nPeça não encontrada")      #se a peça não for reconhecida printa que a peça não foi encontrada
