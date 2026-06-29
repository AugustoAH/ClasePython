
from rich.console import Console
from rich.panel import Panel


def mostrar_menu():
    menu = """
    ╔═══════════════════════════════════════════════════╗
    ║     Manipulación de Ficheros en Python            ║
    ╚═══════════════════════════════════════════════════╝

    Ingrese la acción que desea realizar:

      [1] 📄 Crear fichero
      [2] 📖 Leer fichero
      [3] ✏️ Actualizar fichero
      [4] 🗑️ Eliminar fichero
      [0] ❌ Salir
    """
    print(menu)

def mostrar_menu_color():
    # Códigos ANSI para colores
    CYAN = '\033[96m'
    VERDE = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    print(f"{CYAN}{BOLD}")
    print("=" * 55)
    print("   PROGRAMA PARA LA MANIPULACIÓN DE FICHEROS")
    print("=" * 55)
    print(f"{RESET}")
    
    print("Ingrese la acción que desea realizar:\n")
    print(f"  {VERDE}[1]{RESET} Crear fichero")
    print(f"  {VERDE}[2]{RESET} Leer fichero")
    print(f"  {VERDE}[3]{RESET} Actualizar fichero")
    print(f"  {VERDE}[4]{RESET} Eliminar fichero")
    print(f"  {VERDE}[0]{RESET} Salir")



def mostrar_menu_rich():
    console = Console()

    # El contenido del menú
    opciones = (
        "[bold green]1.[/bold green] Crear fichero\n"
        "[bold green]2.[/bold green] Leer fichero\n"
        "[bold green]3.[/bold green] Actualizar fichero\n"
        "[bold red]4.[/bold red] Eliminar fichero\n\n"
        "[bold yellow]0.[/bold yellow] Salir"
    )

    # Crear un panel visual
    menu_panel = Panel(
        opciones, 
        title="[bold cyan]Manipulación de Ficheros[/bold cyan]", 
        subtitle="[dim]Seleccione una opción[/dim]",
        expand=False,
        border_style="cyan"
    )

    console.print(menu_panel)


if __name__ == "__main__":
    mostrar_menu()
    print("\n")
    mostrar_menu_color()
    print("\n")
    mostrar_menu_rich()



