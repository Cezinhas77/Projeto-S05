def movimento_peao(tabuleiro, origem_linha, origem_coluna, destino_linha, destino_coluna):


    if tabuleiro[origem_linha][origem_coluna] != "PB":
        return False

    if destino_coluna == origem_coluna and destino_linha == origem_linha - 1:
        if tabuleiro[destino_linha][destino_coluna] == "--":  #casa vazia
            return True

    if origem_linha == 7 - 1 and destino_coluna == origem_coluna and destino_linha == origem_linha - 2:
        if tabuleiro[origem_linha - 1][origem_coluna] == "--" and tabuleiro[destino_linha][destino_coluna] == "--":
            return True

    if abs(destino_coluna - origem_coluna) == 1 and destino_linha == origem_linha - 1:
        if tabuleiro[destino_linha][destino_coluna] != "--":
            return True

    return False
