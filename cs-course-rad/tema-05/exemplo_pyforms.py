
"""
Exemplo de aplicação com Pyforms
Framework para Desktop GUI, Terminal e Web
"""

import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlLabel

class ExemploSimples(BaseWidget):
    """Classe principal da aplicação Pyforms"""
    
    def __init__(self):
        super(ExemploSimples, self).__init__('Exemplo Pyforms')
        
        # Título
        self.titulo = ControlLabel(
            "<h2>Exemplo de aplicação Pyforms</h2>"
        )
        
        # Primeira caixa de texto
        self.controle_texto1 = ControlText(
            "Controle de texto 1",
            default="Texto padrão 1"
        )
        
        # Segunda caixa de texto
        self.controle_texto2 = ControlText(
            "Controle de texto 2",
            default="Texto padrão 2"
        )
        
        # Terceira caixa de texto
        self.controle_texto3 = ControlText(
            "Controle de texto 3",
            default="Texto padrão 3"
        )
        
        # Botão
        self.controle_botao = ControlButton(
            "Controle de botão - Clique aqui"
        )
        
        # Configurar evento do botão
        self.controle_botao.value = self.botao_clicado
        
        # Organizar os controles na janela
        self.formset = [
            ('_titulo'),
            ('_controle_texto1'),
            ('_controle_texto2'),
            ('_controle_texto3'),
            ('_controle_botao')
        ]
    
    def botao_clicado(self):
        """Método chamado quando o botão é clicado"""
        texto1 = self.controle_texto1.value
        texto2 = self.controle_texto2.value
        texto3 = self.controle_texto3.value
        
        print("Botão clicado!")
        print(f"Texto 1: {texto1}")
        print(f"Texto 2: {texto2}")
        print(f"Texto 3: {texto3}")
        
        # Atualizar os textos
        self.controle_texto1.value = "Botão foi clicado!"
        self.controle_texto2.value = f"Último clique: {texto1}"
        self.controle_texto3.value = "Pyforms é poderoso!"

if __name__ == '__main__':
    # Executar a aplicação
    pyforms.start_app(ExemploSimples, geometry=(300, 300, 500, 300))
