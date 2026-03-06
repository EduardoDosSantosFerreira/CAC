"""
CAC - Crow Auto Clicker
Camada de lógica - gerencia cliques e automação
"""

import ctypes
import time
import threading
from ctypes import wintypes
from PySide6.QtCore import QObject, Signal

# Constantes do Windows
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

class POINT(ctypes.Structure):
    """Estrutura para coordenadas do mouse"""
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

class ClickerLogic(QObject):
    """Gerencia a lógica de cliques automáticos"""
    
    # Sinais para comunicação com a UI
    click_executado = Signal(int)
    iniciou = Signal(float)
    parou = Signal()
    erro = Signal(str)
    contador_atualizado = Signal(int)
    posicao_capturada = Signal(int, int)
    
    def __init__(self):
        super().__init__()
        self.clicando = False
        self.thread_clique = None
        self.intervalo = 3.0
        self.pos_x = None
        self.pos_y = None
        self.contador = 0
    
    def get_posicao_mouse(self):
        """Retorna a posição atual do mouse"""
        try:
            point = POINT()
            ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
            return point.x, point.y
        except:
            return None, None
    
    def capturar_posicao(self):
        """Captura a posição atual do mouse"""
        x, y = self.get_posicao_mouse()
        if x is not None and y is not None:
            self.pos_x = x
            self.pos_y = y
            self.posicao_capturada.emit(x, y)
            return True
        return False
    
    def clique_direto(self, x, y):
        """Executa um clique em coordenadas específicas"""
        try:
            ctypes.windll.user32.SetCursorPos(x, y)
            time.sleep(0.05)
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(0.05)
            ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            return True
        except Exception as e:
            self.erro.emit(str(e))
            return False
    
    def loop_cliques(self):
        """Loop principal de cliques (executado em thread separada)"""
        while self.clicando:
            try:
                if self.pos_x is not None and self.pos_y is not None:
                    if self.clique_direto(self.pos_x, self.pos_y):
                        self.contador += 1
                        self.click_executado.emit(self.contador)
                        self.contador_atualizado.emit(self.contador)
                
                # Aguarda o intervalo com verificações
                for _ in range(int(self.intervalo * 10)):
                    if not self.clicando:
                        break
                    time.sleep(0.1)
                    
            except Exception as e:
                self.erro.emit(str(e))
                break
        
        self.parou.emit()
    
    def iniciar(self, intervalo=None):
        """Inicia os cliques automáticos"""
        if self.clicando:
            return False
        
        if self.pos_x is None or self.pos_y is None:
            return False
        
        if intervalo is not None:
            self.intervalo = max(0.5, float(intervalo))
        
        self.clicando = True
        self.thread_clique = threading.Thread(
            target=self.loop_cliques, 
            daemon=True
        )
        self.thread_clique.start()
        
        self.iniciou.emit(self.intervalo)
        return True
    
    def parar(self):
        """Para os cliques automáticos"""
        if self.clicando:
            self.clicando = False
            if self.thread_clique and self.thread_clique.is_alive():
                self.thread_clique.join(timeout=1.0)
            return True
        return False
    
    def reset_contador(self):
        """Reseta o contador de cliques"""
        self.contador = 0
        self.contador_atualizado.emit(0)
    
    def is_running(self):
        """Verifica se está clicando"""
        return self.clicando