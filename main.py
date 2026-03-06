"""
CAC - Crow Auto Clicker
Arquivo principal que inicializa a aplicação
"""

import sys
import ctypes
from PySide6.QtWidgets import QApplication
from ui import MainWindow

def is_admin():
    """Verifica se o programa está executando como administrador"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def solicitar_admin():
    """Solicita privilégios de administrador se necessário"""
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            " ".join([f'"{arg}"' for arg in sys.argv]),
            None,
            1,
        )
        sys.exit()

def main():
    """Função principal"""
    app = QApplication(sys.argv)
    
    print("=" * 50)
    print("CAC - CROW AUTO CLICKER")
    print("=" * 50)
    print("\nATALHOS:")
    print("  F3 - Capturar posição do mouse")
    print("  F2 - Iniciar/Parar cliques")
    print("  ESC - Parar (emergência)")
    print("\nIniciando aplicação...")
    print("-" * 50)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    solicitar_admin()
    main()