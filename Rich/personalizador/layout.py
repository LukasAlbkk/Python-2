# arquivo: personalizador/layout.py

from rich.layout import Layout
from rich.console import Console

def mostrar_layout(texto: str, isArquivo: bool):
    """
    Exibe o texto dentro de um layout.

    Args:
        texto (str): O texto a ser exibido ou o caminho para um arquivo de texto.
        isArquivo (bool): Se True, o texto é interpretado como o caminho para um arquivo.
    """
    console = Console()
    layout = Layout()
    
    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()
    
    layout.split_column(
        Layout(texto)
    )
    
    console.print(layout)

def mostrar_texto_simples(texto: str, isArquivo: bool):
    """
    Exibe o texto de forma simples.

    Args:
        texto (str): O texto a ser exibido ou o caminho para um arquivo de texto.
        isArquivo (bool): Se True, o texto é interpretado como o caminho para um arquivo.
    """
    console = Console()

    if isArquivo:
        with open(texto, 'r') as file:
            texto = file.read()

    console.print(texto)
