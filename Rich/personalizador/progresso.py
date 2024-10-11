from rich.console import Console
from rich.progress import track

console = Console()

def mostrar_progresso(texto: str, isArquivo: bool):
    """
    Simula um progresso enquanto exibe o texto.

    Args:
        texto (str): Texto a ser exibido ou caminho para um arquivo de texto.
        isArquivo (bool): Se True, o texto é interpretado como o caminho para um arquivo.

    """
    if isArquivo:
        with open(texto, 'r') as file:
            conteudo = file.read()
    else:
        conteudo = texto

    for _ in track(range(10), description="Processando..."):
        pass

    console.print(conteudo)

def mostrar_progresso_customizado(texto: str, isArquivo: bool):
    """
    Simula um progresso com uma barra de progresso customizada.

    Args:
        texto (str): Texto a ser exibido ou caminho para um arquivo de texto.
        isArquivo (bool): Se True, o texto é interpretado como o caminho para um arquivo.

    """
    if isArquivo:
        with open(texto, 'r') as file:
            conteudo = file.read()
    else:
        conteudo = texto

    for _ in track(range(5), description="Carregando dados..."):
        pass

    console.print(f"[green]{conteudo}[/green]")
