
"""
Exemplo de aplicação com Kivy
Framework para aplicações multitoque
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.metrics import dp

# Configurar a janela
Window.size = (400, 300)
Window.title = "Exemplo Kivy"

class ExemploKivy(App):
    """Classe principal da aplicação"""
    
    def build(self):
        """Método que constrói a interface"""
        # Layout principal
        layout = BoxLayout(
            orientation='vertical',
            spacing=dp(10),
            padding=dp(20)
        )
        
        # Título
        titulo = Label(
            text='[b][size=24]Exemplo Kivy[/size][/b]',
            markup=True,
            size_hint=(1, 0.3)
        )
        layout.add_widget(titulo)
        
        # Campo de entrada
        self.entrada = TextInput(
            text='',
            hint_text='Digite seu nome',
            multiline=False,
            size_hint=(1, 0.15),
            font_size=dp(16)
        )
        layout.add_widget(self.entrada)
        
        # Botão
        botao = Button(
            text='Clique aqui',
            size_hint=(1, 0.15),
            font_size=dp(16),
            background_normal='',
            background_color=(0.2, 0.7, 0.3, 1)
        )
        botao.bind(on_press=self.botao_clicado)
        layout.add_widget(botao)
        
        # Label para resultado
        self.resultado = Label(
            text='',
            size_hint=(1, 0.3),
            font_size=dp(14)
        )
        layout.add_widget(self.resultado)
        
        return layout
    
    def botao_clicado(self, instance):
        """Método chamado quando o botão é clicado"""
        nome = self.entrada.text
        
        if nome:
            mensagem = f"Olá, {nome}! Bem-vindo ao Kivy!"
            self.resultado.text = mensagem
            self.resultado.color = (0.2, 0.6, 0.2, 1)
            
            # Criar popup
            popup_layout = BoxLayout(
                orientation='vertical',
                padding=dp(20),
                spacing=dp(10)
            )
            popup_layout.add_widget(
                Label(text=f"Olá, {nome}!", font_size=dp(18))
            )
            
            btn_fechar = Button(
                text='Fechar',
                size_hint=(1, 0.3),
                background_color=(0.7, 0.1, 0.1, 1)
            )
            popup_layout.add_widget(btn_fechar)
            
            popup = Popup(
                title='Saudação',
                content=popup_layout,
                size_hint=(0.6, 0.4)
            )
            btn_fechar.bind(on_press=popup.dismiss)
            popup.open()
        else:
            self.resultado.text = "Por favor, digite seu nome!"
            self.resultado.color = (0.8, 0.2, 0.2, 1)

if __name__ == '__main__':
    ExemploKivy().run()
