def matriz_tabuleiro(tabuleiro):
    print("  1  2  3  4  5  6  7  8")  #coluna
    for i in range(8):      # for percorre as linhas                                      
        linha = str(i + 1) + " "  #usado para criar cada linha a partir de 1  (+ " " é para dar espaçamento a cada caractere)
        for j in range(8):     #for percorre as colunas
            linha += tabuleiro[i][j] + " "      
        print(linha)

#tabuleiro
tabuleiro = [
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["PB", "PB", "PB", "PB", "PB", "PB", "PB", "PB"],
    ["TB", "CB", "BP", "KB", "QB", "BP", "CB", "TB"]
]

#inputs
while True:
    matriz_tabuleiro(tabuleiro)
    peca = input("Qual peça deseja mover?: ").upper()
    origem_linha = int(input("Linha de origem (1-8): ")) - 1
    origem_coluna = int(input("Coluna de origem (1-8): ")) - 1
    destino_linha = int(input("Linha de destino (1-8): ")) - 1
    destino_coluna = int(input("Coluna de destino (1-8): ")) - 1
