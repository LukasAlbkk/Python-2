from rich.console import Console
from rich.layout import Layout

console = Console()

def mostrar_layout(texto: str, isArquivo: bool):
    """
    Exibe o texto dentro de um layout.

    Args:
        texto (str): Texto a ser exibido ou caminho para um arquivo de texto.
        isArquivo (bool): Se True, o texto é interpretado como o caminho para um arquivo.

    """
    if isArquivo:
        with open(texto, 'r') as file:
            conteudo = file.read()
    else:
        conteudo = texto

    layout = Layout()
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1)
    )
    layout["header"].update("[bold]Cabeçalho[/bold]")
    layout["body"].update(conteudo)
    
    console.print(layout)

def mostrar_texto_simples(texto: str, isArquivo: bool):
    """
    Exibe o texto de forma simples.

    Args:
        texto (str): Texto a ser exibido ou caminho para um arquivo de texto.
        isArquivo (bool): Se True, o texto é interpretado como o caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as file:
            conteudo = file.read()
    else:
        conteudo = texto

    console.print(conteudo)
