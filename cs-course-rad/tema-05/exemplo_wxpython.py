
"""
Exemplo de aplicação com wxPython
Kit de ferramentas GUI com widgets nativos
"""

import wx

class ExemploFrame(wx.Frame):
    """Classe principal da janela"""
    
    def __init__(self):
        super().__init__(
            None,
            title="Exemplo wxPython",
            size=(500, 350)
        )
        
        # Configurar ícone (opcional)
        self.SetIcon(wx.Icon())
        
        # Criar painel principal
        panel = wx.Panel(self)
        
        # Criar sizer vertical
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Título
        titulo = wx.StaticText(
            panel,
            label="Exemplo de aplicação wxPython",
            style=wx.ALIGN_CENTER
        )
        fonte_titulo = wx.Font(
            16,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD
        )
        titulo.SetFont(fonte_titulo)
        titulo.SetForegroundColour(wx.Colour(44, 62, 80))
        vbox.Add(titulo, 0, wx.EXPAND | wx.ALL, 20)
        
        # Linha separadora
        line = wx.StaticLine(panel, style=wx.LI_HORIZONTAL)
        vbox.Add(line, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)
        
        # Subtítulo
        subtitulo = wx.StaticText(
            panel,
            label="Widgets nativos do sistema operacional",
            style=wx.ALIGN_CENTER
        )
        fonte_sub = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        subtitulo.SetFont(fonte_sub)
        subtitulo.SetForegroundColour(wx.Colour(127, 140, 141))
        vbox.Add(subtitulo, 0, wx.EXPAND | wx.ALL, 10)
        
        # Espaçador
        vbox.Add((-1, 20))
        
        # Criar sizer horizontal para entrada
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        # Label
        label = wx.StaticText(panel, label="Digite algo:")
        fonte_label = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        label.SetFont(fonte_label)
        hbox.Add(label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)
        
        # Caixa de texto
        self.texto = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.texto.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.texto.SetMinSize((200, -1))
        hbox.Add(self.texto, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)
        
        vbox.Add(hbox, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 30)
        
        # Botão
        self.botao = wx.Button(panel, label="Pressione esse componente!")
        fonte_botao = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.botao.SetFont(fonte_botao)
        self.botao.SetForegroundColour(wx.Colour(255, 255, 255))
        self.botao.SetBackgroundColour(wx.Colour(39, 174, 96))
        self.botao.Bind(wx.EVT_BUTTON, self.on_botao)
        vbox.Add(self.botao, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        
        # Label para resultado
        self.resultado = wx.StaticText(panel, label="")
        fonte_resultado = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL)
        self.resultado.SetFont(fonte_resultado)
        self.resultado.SetForegroundColour(wx.Colour(41, 128, 185))
        vbox.Add(self.resultado, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        
        # Espaçador
        vbox.Add((-1, 20))
        
        # Informação
        info = wx.StaticText(
            panel,
            label="Aplicação desenvolvida com wxPython - Widgets nativos",
            style=wx.ALIGN_CENTER
        )
        fonte_info = wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_LIGHT)
        info.SetFont(fonte_info)
        info.SetForegroundColour(wx.Colour(189, 195, 199))
        vbox.Add(info, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        
        # Configurar sizer do painel
        panel.SetSizer(vbox)
        
        # Centralizar a janela
        self.Centre()
    
    def on_botao(self, event):
        """Evento do botão"""
        texto = self.texto.GetValue()
        
        if texto:
            mensagem = f"Você digitou: {texto}"
            self.resultado.SetLabel(mensagem)
            wx.MessageBox(mensagem, "Mensagem", wx.OK | wx.ICON_INFORMATION)
        else:
            self.resultado.SetLabel("Por favor, digite algo!")
            wx.MessageBox("Digite algo no campo de texto!", "Aviso", wx.OK | wx.ICON_WARNING)

class ExemploApp(wx.App):
    """Classe da aplicação"""
    
    def OnInit(self):
        """Inicialização da aplicação"""
        frame = ExemploFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = ExemploApp()
    app.MainLoop()
