
"""
Exemplo de aplicação com Flexx
Framework que usa tecnologia web para renderização
"""

from flexx import app, event, ui

class ExemploFlexx(ui.Widget):
    """Aplicação exemplo usando Flexx"""
    
    def init(self):
        """Método de inicialização"""
        with ui.VBox():
            ui.Label(
                text='<h1 style="color: #4CAF50;">Exemplo Flexx</h1>',
                wrap=False
            )
            ui.Label(
                text='<p style="font-size: 16px;">Framework com tecnologia web</p>',
                wrap=False
            )
            
            # Campo de entrada
            self.entrada = ui.LineEdit(placeholder_text="Digite algo...")
            
            # Botão
            self.botao = ui.Button(text='Clique aqui')
            
            # Label para resultado
            self.resultado = ui.Label(wrap=False)
    
    @event.reaction('botao.pointer_click')
    def _botao_clicado(self, *events):
        """Reação ao clique do botão"""
        texto = self.entrada.text
        if texto:
            self.resultado.set_text(
                f'<p style="color: #2196F3;">Você digitou: <b>{texto}</b></p>'
            )
        else:
            self.resultado.set_text(
                '<p style="color: #f44336;">Por favor, digite algo!</p>'
            )

if __name__ == '__main__':
    # Criar e iniciar a aplicação
    a = app.launch(ExemploFlexx, 'app')  # 'app' para desktop
    app.run()
