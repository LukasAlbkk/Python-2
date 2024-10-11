from rich.console import Console

console = Console()

def mostrar_texto_estilizado(texto: str, isArquivo: bool):
    """
    Exibe o texto com formatação rica.

    Args:
        texto (str): Texto a ser exibido ou caminho para um arquivo de texto.
        isArquivo (bool): Se True, o texto é interpretado como o caminho para um arquivo.

    """
    if isArquivo:
        with open(texto, 'r') as file:
            conteudo = file.read()
    else:
        conteudo = texto

    console.print(f"[bold blue]{conteudo}[/bold blue]")

def mostrar_texto_colorido(texto: str, isArquivo: bool):
    """
    Exibe o texto com cores personalizadas.

    Args:
        texto (str): Texto a ser exibido ou caminho para um arquivo de texto.
        isArquivo (bool): Se True, o texto é interpretado como o caminho para um arquivo.

    """
    if isArquivo:
        with open(texto, 'r') as file:
            conteudo = file.read()
    else:
        conteudo = texto

    console.print(f"[italic red]{conteudo}[/italic red]")
