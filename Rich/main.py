import argparse
from personalizador import layout, painel, progresso, estilo

modulos = {
    'layout': layout,
    'painel': painel,
    'progresso': progresso,
    'estilo': estilo
}

funcoes_modulo = {
    'layout': ['mostrar_layout', 'mostrar_texto_simples'],
    'painel': ['mostrar_painel', 'mostrar_painel_destacado'],
    'progresso': ['mostrar_progresso', 'mostrar_progresso_customizado'],
    'estilo': ['mostrar_texto_estilizado', 'mostrar_texto_colorido']
}

def main():
    parser = argparse.ArgumentParser(description="Interface de formatação usando Rich")
    
    parser.add_argument('texto', help="Texto ou nome do arquivo que deseja imprimir formatado.")
    parser.add_argument('-a', '--arquivo', action='store_true', help="Indica que o argumento é o caminho para um arquivo.")
    
    parser.add_argument('-m', '--modulo', choices=modulos.keys(), required=True,
                        help=f"Escolhe o módulo para acessar. Opções: {', '.join(modulos.keys())}")
    
    parser.add_argument('-f', '--funcao', required=True,
                        help="Escolhe a função do módulo que quer acessar. Exemplo: mostrar_layout, mostrar_painel.")
    args = parser.parse_args()

    modulo_selecionado = modulos[args.modulo]

    if args.funcao not in funcoes_modulo[args.modulo]:
        print(f"Função '{args.funcao}' não é válida para o módulo '{args.modulo}'.")
        print(f"Funções válidas para o módulo '{args.modulo}': {', '.join(funcoes_modulo[args.modulo])}")
        return
    funcao_selecionada = getattr(modulo_selecionado, args.funcao)
    funcao_selecionada(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
