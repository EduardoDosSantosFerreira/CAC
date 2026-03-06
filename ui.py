"""
CAC - Crow Auto Clicker
Interface do usuário com design limpo e sem bordas
"""

import os
import sys
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QDoubleSpinBox, QFrame
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPixmap, QPainter, QColor, QBrush
from logic import ClickerLogic

class CircularImage(QLabel):
    """Widget que exibe uma imagem com fundo circular branco"""
    
    def __init__(self, image_path, size=104):
        super().__init__()
        self.size = size
        self.image_path = image_path
        self.setFixedSize(size, size)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Desenha o círculo branco
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, self.size, self.size)
        
        # Desenha a imagem por cima (se existir)
        if os.path.exists(self.image_path):
            pixmap = QPixmap(self.image_path)
            if not pixmap.isNull():
                # Redimensiona a imagem para caber dentro do círculo (com margem)
                img_size = self.size - 10
                scaled = pixmap.scaled(img_size, img_size, 
                                     Qt.AspectRatioMode.KeepAspectRatio, 
                                     Qt.TransformationMode.SmoothTransformation)
                
                # Centraliza a imagem no círculo
                x = (self.size - scaled.width()) // 2
                y = (self.size - scaled.height()) // 2
                painter.drawPixmap(x, y, scaled)

class ModernCounter(QLabel):
    """Widget de contador moderno"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setMinimumHeight(120)
        self.setMaximumHeight(160)
        
        # Fonte fixa e menor
        font = QFont("Arial", 36, QFont.Weight.Bold)
        self.setFont(font)
        
        self.update_style()
        
    def update_style(self, is_running=False):
        """Atualiza o estilo baseado no estado"""
        if is_running:
            self.setStyleSheet("""
                QLabel {
                    color: #88ff88;
                    background-color: transparent;
                }
            """)
        else:
            self.setStyleSheet("""
                QLabel {
                    color: #88c0ff;
                    background-color: transparent;
                }
            """)

class MainWindow(QMainWindow):
    """Janela principal do Crow Auto Clicker"""
    
    def __init__(self):
        super().__init__()
        self.logic = ClickerLogic()
        self.setup_ui()
        self.conecta_sinais()
        self.configura_hotkeys()
        self.aplicar_estilo_escuro()
        
    def resource_path(self, relative_path):
        """Obtém o caminho correto para recursos (funciona no .exe)"""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
        
    def setup_ui(self):
        """Configura a interface do usuário"""
        self.setWindowTitle("CAC - Crow Auto Clicker")
        self.setMinimumSize(500, 650)
        self.setMaximumSize(700, 800)
        
        # Widget central
        central = QWidget()
        self.setCentralWidget(central)
        
        # Layout principal
        layout = QVBoxLayout(central)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 12, 12, 12)
        
        # Cabeçalho
        self.adicionar_cabecalho(layout)
        
        # Atalhos
        self.adicionar_atalhos(layout)
        
        # Posição
        self.adicionar_posicao(layout)
        
        # Configurações
        self.adicionar_configuracoes(layout)
        
        # Status com contador
        self.adicionar_status(layout)
        
        # Timer para atualizar posição
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_posicao)
        self.timer.start(100)
    
    def aplicar_estilo_escuro(self):
        """Aplica o tema escuro à aplicação - sem bordas cinzas"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #000000;
            }
            QWidget {
                background-color: #000000;
                color: #ffffff;
            }
            QFrame {
                background-color: transparent;
                border: none;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
                background-color: transparent;
                border: none;
            }
            QPushButton {
                background-color: #1a1a1a;
                color: #ffffff;
                border: none;
                padding: 8px 12px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #2a2a2a;
            }
            QPushButton:pressed {
                background-color: #333333;
            }
            QDoubleSpinBox {
                background-color: #1a1a1a;
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 6px;
                font-size: 12px;
                font-weight: bold;
            }
            QDoubleSpinBox:focus {
                background-color: #222222;
            }
            QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
                width: 16px;
                background-color: #2a2a2a;
                border-radius: 2px;
                margin: 1px;
            }
            QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover {
                background-color: #3a3a3a;
            }
            QDoubleSpinBox::up-button:pressed, QDoubleSpinBox::down-button:pressed {
                background-color: #444444;
            }
        """)
    
    def adicionar_cabecalho(self, parent):
        """Adiciona cabeçalho com imagem CAC"""
        cabecalho = QHBoxLayout()
        cabecalho.setAlignment(Qt.AlignCenter)
        cabecalho.setSpacing(12)
        
        # Caminho da imagem
        imagem_path = self.resource_path("cac.png")
        
        # Imagem esquerda com círculo
        imagem_esq = CircularImage(imagem_path, 56)
        cabecalho.addWidget(imagem_esq)
        
        # Título
        titulo = QLabel("CROW AUTO CLICKER")
        titulo.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        titulo.setStyleSheet("color: #ffffff; letter-spacing: 1px; background: transparent;")
        cabecalho.addWidget(titulo)
        
        # Espaço vazio à direita para equilibrar
        cabecalho.addStretch()
        
        parent.addLayout(cabecalho)
    
    def adicionar_atalhos(self, parent):
        """Adiciona seção de atalhos"""
        # Título
        titulo = QLabel("ATALHOS")
        titulo.setStyleSheet("color: #888888; font-weight: bold; font-size: 10px; margin-top: 4px;")
        parent.addWidget(titulo)
        
        # Lista de atalhos em linha
        atalhos_layout = QHBoxLayout()
        atalhos_layout.setSpacing(15)
        atalhos_layout.setContentsMargins(0, 2, 0, 4)
        
        atalhos = [
            ("F3", "Capturar"),
            ("F2", "Iniciar/Parar"),
            ("ESC", "Emergência")
        ]
        
        for tecla, desc in atalhos:
            item_layout = QVBoxLayout()
            item_layout.setSpacing(0)
            
            tecla_label = QLabel(tecla)
            tecla_label.setFont(QFont("Arial", 13, QFont.Weight.Bold))
            tecla_label.setStyleSheet("color: #88c0ff; background: transparent;")
            tecla_label.setAlignment(Qt.AlignCenter)
            item_layout.addWidget(tecla_label)
            
            desc_label = QLabel(desc)
            desc_label.setStyleSheet("color: #666666; font-size: 9px; background: transparent;")
            desc_label.setAlignment(Qt.AlignCenter)
            item_layout.addWidget(desc_label)
            
            atalhos_layout.addLayout(item_layout)
        
        atalhos_layout.addStretch()
        parent.addLayout(atalhos_layout)
    
    def adicionar_posicao(self, parent):
        """Adiciona seção de posição"""
        # Título
        titulo = QLabel("POSIÇÃO DO MOUSE")
        titulo.setStyleSheet("color: #888888; font-weight: bold; font-size: 10px; margin-top: 8px;")
        parent.addWidget(titulo)
        
        # Posição atual
        self.pos_label = QLabel("X: 0 | Y: 0")
        self.pos_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.pos_label.setAlignment(Qt.AlignCenter)
        self.pos_label.setStyleSheet("""
            QLabel {
                color: #88c0ff;
                background-color: #0a0a0a;
                padding: 6px;
                border-radius: 4px;
            }
        """)
        parent.addWidget(self.pos_label)
        
        # Linha com botão e posição capturada
        linha = QHBoxLayout()
        linha.setSpacing(8)
        linha.setContentsMargins(0, 4, 0, 0)
        
        self.btn_capturar = QPushButton("📸 CAPTURAR")
        self.btn_capturar.setFixedWidth(100)
        self.btn_capturar.setStyleSheet("""
            QPushButton {
                background-color: #1a1a1a;
                color: #88c0ff;
                padding: 6px;
                font-weight: bold;
                font-size: 10px;
            }
            QPushButton:hover {
                background-color: #2a2a2a;
            }
        """)
        self.btn_capturar.clicked.connect(self.capturar_posicao)
        linha.addWidget(self.btn_capturar)
        
        self.capturado_label = QLabel("⚫ Nenhuma")
        self.capturado_label.setAlignment(Qt.AlignCenter)
        self.capturado_label.setStyleSheet("color: #666666; font-size: 10px; background: transparent;")
        linha.addWidget(self.capturado_label, 1)
        
        parent.addLayout(linha)
    
    def adicionar_configuracoes(self, parent):
        """Adiciona seção de configurações"""
        # Título
        titulo = QLabel("CONFIGURAÇÕES")
        titulo.setStyleSheet("color: #888888; font-weight: bold; font-size: 10px; margin-top: 8px;")
        parent.addWidget(titulo)
        
        # Linha de intervalo
        intervalo_layout = QHBoxLayout()
        intervalo_layout.setSpacing(8)
        intervalo_layout.setContentsMargins(0, 2, 0, 0)
        
        intervalo_label = QLabel("Intervalo:")
        intervalo_label.setStyleSheet("color: #cccccc; font-size: 11px; background: transparent;")
        intervalo_layout.addWidget(intervalo_label)
        
        # SpinBox
        self.intervalo_spin = QDoubleSpinBox()
        self.intervalo_spin.setRange(0.1, 10.0)
        self.intervalo_spin.setSingleStep(0.1)
        self.intervalo_spin.setValue(1.8)
        self.intervalo_spin.setSuffix("s")
        self.intervalo_spin.setAlignment(Qt.AlignCenter)
        self.intervalo_spin.setFixedWidth(85)
        intervalo_layout.addWidget(self.intervalo_spin)
        
        # Botões +/- com efeito hover
        btn_menos = QPushButton("−")
        btn_menos.setFixedSize(28, 28)
        btn_menos.setStyleSheet("""
            QPushButton {
                background-color: #1a1a1a;
                color: #88c0ff;
                font-size: 16px;
                font-weight: bold;
                padding: 0px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #2a5a8c;
                color: #ffffff;
            }
            QPushButton:pressed {
                background-color: #1a3a5c;
            }
        """)
        btn_menos.clicked.connect(lambda: self.intervalo_spin.setValue(
            max(0.1, self.intervalo_spin.value() - 0.1)
        ))
        
        btn_mais = QPushButton("+")
        btn_mais.setFixedSize(28, 28)
        btn_mais.setStyleSheet("""
            QPushButton {
                background-color: #1a1a1a;
                color: #88c0ff;
                font-size: 16px;
                font-weight: bold;
                padding: 0px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #2a5a8c;
                color: #ffffff;
            }
            QPushButton:pressed {
                background-color: #1a3a5c;
            }
        """)
        btn_mais.clicked.connect(lambda: self.intervalo_spin.setValue(
            min(10.0, self.intervalo_spin.value() + 0.1)
        ))
        
        intervalo_layout.addWidget(btn_menos)
        intervalo_layout.addWidget(btn_mais)
        intervalo_layout.addStretch()
        
        parent.addLayout(intervalo_layout)
        
        # Botão reset
        self.btn_reset = QPushButton("🔄 Reset")
        self.btn_reset.setFixedWidth(80)
        self.btn_reset.setStyleSheet("""
            QPushButton {
                background-color: #1a1a1a;
                color: #ffaa88;
                padding: 5px;
                font-size: 10px;
            }
            QPushButton:hover {
                background-color: #5a2a2a;
                color: #ffffff;
            }
        """)
        self.btn_reset.clicked.connect(self.reset_contador)
        parent.addWidget(self.btn_reset, alignment=Qt.AlignRight)
    
    def adicionar_status(self, parent):
        """Adiciona seção de status"""
        # Título
        titulo = QLabel("STATUS")
        titulo.setStyleSheet("color: #888888; font-weight: bold; font-size: 10px; margin-top: 8px;")
        parent.addWidget(titulo)
        
        # Contador (sem texto adicional por cima)
        self.contador_moderno = ModernCounter()
        self.contador_moderno.setText("0")
        parent.addWidget(self.contador_moderno)
        
        # Status
        self.status_label = QLabel("⏸️ Parado")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #ffff88; padding: 2px; font-size: 11px; background: transparent;")
        parent.addWidget(self.status_label)
        
        # Botão ação
        self.btn_acao = QPushButton("▶️ INICIAR")
        self.btn_acao.setStyleSheet("""
            QPushButton {
                background-color: #1a4a1a;
                color: #ffffff;
                padding: 16px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 6px;
                margin-top: 4px;
            }
            QPushButton:hover {
                background-color: #2a6a2a;
            }
            QPushButton:pressed {
                background-color: #0a3a0a;
            }
        """)
        self.btn_acao.clicked.connect(self.toggle_cliques)
        parent.addWidget(self.btn_acao)
    
    def conecta_sinais(self):
        """Conecta os sinais da lógica"""
        self.logic.click_executado.connect(self.on_click)
        self.logic.iniciou.connect(self.on_start)
        self.logic.parou.connect(self.on_stop)
        self.logic.erro.connect(self.on_error)
        self.logic.contador_atualizado.connect(self.on_count_update)
        self.logic.posicao_capturada.connect(self.on_posicao_capturada)
    
    def configura_hotkeys(self):
        """Configura os atalhos de teclado"""
        try:
            import keyboard
            keyboard.add_hotkey("f2", self.toggle_cliques, suppress=False)
            keyboard.add_hotkey("f3", self.capturar_posicao, suppress=False)
            keyboard.add_hotkey("esc", self.parar_cliques, suppress=False)
        except Exception as e:
            print(f"Erro ao configurar hotkeys: {e}")
    
    def atualizar_posicao(self):
        """Atualiza a posição do mouse"""
        x, y = self.logic.get_posicao_mouse()
        if x is not None and y is not None:
            self.pos_label.setText(f"X: {x} | Y: {y}")
    
    def capturar_posicao(self):
        """Captura a posição atual"""
        if self.logic.capturar_posicao():
            try:
                import winsound
                winsound.Beep(800, 100)
            except:
                pass
    
    def toggle_cliques(self):
        """Alterna entre iniciar e parar"""
        if self.logic.is_running():
            self.parar_cliques()
        else:
            self.iniciar_cliques()
    
    def iniciar_cliques(self):
        """Inicia os cliques"""
        intervalo = self.intervalo_spin.value()
        if self.logic.iniciar(intervalo):
            self.btn_acao.setText("⏹️ PARAR")
            self.btn_acao.setStyleSheet("""
                QPushButton {
                    background-color: #6a2a2a;
                    color: #ffffff;
                    padding: 16px;
                    font-size: 16px;
                    font-weight: bold;
                    border-radius: 6px;
                    margin-top: 4px;
                }
                QPushButton:hover {
                    background-color: #8a3a3a;
                }
                QPushButton:pressed {
                    background-color: #5a1a1a;
                }
            """)
            self.contador_moderno.update_style(True)
    
    def parar_cliques(self):
        """Para os cliques"""
        if self.logic.parar():
            self.btn_acao.setText("▶️ INICIAR")
            self.btn_acao.setStyleSheet("""
                QPushButton {
                    background-color: #1a4a1a;
                    color: #ffffff;
                    padding: 16px;
                    font-size: 16px;
                    font-weight: bold;
                    border-radius: 6px;
                    margin-top: 4px;
                }
                QPushButton:hover {
                    background-color: #2a6a2a;
                }
                QPushButton:pressed {
                    background-color: #0a3a0a;
                }
            """)
            self.contador_moderno.update_style(False)
    
    def reset_contador(self):
        """Reseta o contador"""
        self.logic.reset_contador()
    
    # Slots
    def on_click(self, contador):
        """Quando um clique é executado"""
        self.status_label.setText(f"🟢 Clique #{contador}")
        self.status_label.setStyleSheet("color: #88ff88; padding: 2px; font-size: 11px; background: transparent;")
    
    def on_start(self, intervalo):
        """Quando inicia"""
        self.status_label.setText(f"🟢 Clicando a cada {intervalo}s")
        self.status_label.setStyleSheet("color: #88ff88; padding: 2px; font-size: 11px; background: transparent;")
    
    def on_stop(self):
        """Quando para"""
        self.status_label.setText("⏸️ Parado")
        self.status_label.setStyleSheet("color: #ffff88; padding: 2px; font-size: 11px; background: transparent;")
    
    def on_error(self, erro):
        """Quando ocorre erro"""
        self.status_label.setText(f"❌ Erro")
        self.status_label.setStyleSheet("color: #ff8888; padding: 2px; font-size: 11px; background: transparent;")
    
    def on_count_update(self, contador):
        """Quando contador é atualizado"""
        self.contador_moderno.setText(str(contador))
    
    def on_posicao_capturada(self, x, y):
        """Quando posição é capturada"""
        self.capturado_label.setText(f"✅ {x}, {y}")
        self.capturado_label.setStyleSheet("color: #88ff88; font-size: 10px; background: transparent;")
        self.status_label.setText("✅ Posição capturada!")
        self.status_label.setStyleSheet("color: #88ff88; padding: 2px; font-size: 11px; background: transparent;")
    
    def closeEvent(self, event):
        """Quando a janela é fechada"""
        self.logic.parar()
        try:
            import keyboard
            keyboard.unhook_all()
        except:
            pass
        event.accept()