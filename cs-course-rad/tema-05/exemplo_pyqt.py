
"""
Exemplo de aplicação com PyQt
Framework completo para desenvolvimento GUI
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QMessageBox, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class ExemploPyQt(QMainWindow):
    """Classe principal da aplicação PyQt"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Inicializar a interface do usuário"""
        # Configurar a janela principal
        self.setWindowTitle("Exemplo PyQt")
        self.setGeometry(300, 300, 500, 300)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout_principal = QVBoxLayout(central_widget)
        layout_principal.setSpacing(20)
        layout_principal.setContentsMargins(30, 30, 30, 30)
        
        # Título
        titulo = QLabel("Exemplo de aplicação PyQt")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Arial", 18, QFont.Bold))
        titulo.setStyleSheet("color: #2c3e50; margin: 10px;")
        layout_principal.addWidget(titulo)
        
        # Linha separadora
        linha = QFrame()
        linha.setFrameShape(QFrame.HLine)
        linha.setFrameShadow(QFrame.Sunken)
        linha.setStyleSheet("background-color: #bdc3c7;")
        layout_principal.addWidget(linha)
        
        # Subtítulo
        subtitulo = QLabel("Framework completo para GUI")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setFont(QFont("Arial", 12))
        subtitulo.setStyleSheet("color: #7f8c8d; margin-bottom: 20px;")
        layout_principal.addWidget(subtitulo)
        
        # Layout para entrada
        layout_entrada = QHBoxLayout()
        
        # Label
        label_nome = QLabel("Digite seu nome:")
        label_nome.setFont(QFont("Arial", 11))
        label_nome.setStyleSheet("color: #34495e;")
        layout_entrada.addWidget(label_nome)
        
        # Campo de entrada
        self.entrada_nome = QLineEdit()
        self.entrada_nome.setPlaceholderText("Seu nome aqui...")
        self.entrada_nome.setFont(QFont("Arial", 11))
        self.entrada_nome.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                background: white;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
        """)
        layout_entrada.addWidget(self.entrada_nome)
        
        layout_principal.addLayout(layout_entrada)
        
        # Botão
        botao = QPushButton("Clique aqui")
        botao.setFont(QFont("Arial", 12, QFont.Bold))
        botao.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
            QPushButton:pressed {
                background-color: #229954;
            }
        """)
        botao.clicked.connect(self.botao_clicado)
        layout_principal.addWidget(botao)
        
        # Espaçador
        layout_principal.addStretch()
        
        # Mensagem no centro da janela
        self.mensagem = QLabel("")
        self.mensagem.setAlignment(Qt.AlignCenter)
        self.mensagem.setFont(QFont("Arial", 14, QFont.Bold))
        self.mensagem.setStyleSheet("color: #2980b9; margin: 20px;")
        layout_principal.addWidget(self.mensagem)
    
    def botao_clicado(self):
        """Método chamado quando o botão é clicado"""
        nome = self.entrada_nome.text()
        
        if nome:
            mensagem = f"Olá, {nome}! Bem-vindo ao PyQt!"
            self.mensagem.setText(mensagem)
            QMessageBox.information(self, "Saudação", mensagem)
        else:
            self.mensagem.setText("Por favor, digite seu nome!")
            QMessageBox.warning(self, "Atenção", "Digite seu nome!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Configurar o estilo da aplicação
    app.setStyle('Fusion')
    
    # Criar e mostrar a janela
    janela = ExemploPyQt()
    janela.show()
    
    # Executar a aplicação
    sys.exit(app.exec_())
