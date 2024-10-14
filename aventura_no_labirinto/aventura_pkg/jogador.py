import pynput
from pynput.keyboard import Key, Listener
from labirinto import criar_labirinto  # Importa o labirinto gerado

# Função para iniciar o jogador
def iniciar_jogador(labirinto):
    jogador_posicao = [1, 1]  # Posição inicial do jogador (linha, coluna)

    def mostrar_labirinto():
        for i, linha in enumerate(labirinto):
            for j, celula in enumerate(linha):
                if i == jogador_posicao[0] and j == jogador_posicao[1] * 3 + 1:  # Ajusta a posição para o mapa
                    print("P", end="")
                else:
                    print(celula, end="")
            print()

    def mover_jogador(direcao):
        x, y = jogador_posicao

        if direcao == "w":  # Move para cima
            if x > 0 and labirinto[x * 2][y * 3 + 1] == "   ":  # Verifica se a célula acima está livre
                jogador_posicao[0] -= 1
        elif direcao == "s":  # Move para baixo
            if x < (len(labirinto) - 1) // 2 and labirinto[(x + 1) * 2][y * 3 + 1] == "   ":
                jogador_posicao[0] += 1
        elif direcao == "a":  # Move para a esquerda
            if y > 0 and labirinto[x * 2][(y - 1) * 3 + 1] == "   ":
                jogador_posicao[1] -= 1
        elif direcao == "d":  # Move para a direita
            if y < (len(labirinto[0]) // 3 - 1) and labirinto[x * 2][(y + 1) * 3 + 1] == "   ":
                jogador_posicao[1] += 1

        mostrar_labirinto()

    def on_press(key):
        try:
            if key.char in ["w", "a", "s", "d"]:
                mover_jogador(key.char)
        except AttributeError:
            if key == Key.esc:
                # Pressione ESC para sair do jogo
                return False

    print("Use W, A, S, D para mover o jogador. Pressione ESC para sair.")
    mostrar_labirinto()

    with Listener(on_press=on_press) as listener:
        listener.join()

# Chame a função iniciar_jogador com o labirinto gerado
labirinto = criar_labirinto()  # Cria o labirinto dinamicamente
iniciar_jogador(labirinto)
