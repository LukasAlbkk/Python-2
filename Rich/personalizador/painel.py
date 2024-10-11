# personalizador/painel.py
from rich.console import Console
from rich.panel import Panel

console = Console()

def mostrar_painel(texto: str, isArquivo: bool):
    """
    Exibe o texto dentro de um painel.

    Args:
        texto (str): Texto a ser exibido ou caminho para um arquivo de texto.
        isArquivo (bool): Se True, o texto é interpretado como o caminho para um arquivo.

    """
    if isArquivo:
        with open(texto, 'r') as file:
            conteudo = file.read()
    else:
        conteudo = texto

    console.print(Panel(conteudo, title="Painel de Texto", border_style="green"))

def mostrar_painel_destacado(texto: str, isArquivo: bool):
    """
    Exibe o texto dentro de um painel destacado.

    Args:
        texto (str): Texto a ser exibido ou caminho para um arquivo de texto.
        isArquivo (bool): Se True, o texto é interpretado como o caminho para um arquivo.

    """
    if isArquivo:
        with open(texto, 'r') as file:
            conteudo = file.read()
    else:
        conteudo = texto

    console.print(Panel(conteudo, title="Texto Destacado", border_style="magenta"))
