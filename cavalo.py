def movimentos_cavalo(x, y, tamanho_tabuleiro):
    movimentos_possiveis = [
        (x - 2, y - 1),
        (x - 2, y + 1),
        (x - 1, y - 2),
        (x - 1, y + 2),
        (x + 1, y - 2),
        (x + 1, y + 2),
        (x + 2, y - 1),
        (x + 2, y + 1),
    ]
