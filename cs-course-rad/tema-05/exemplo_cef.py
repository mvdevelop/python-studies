
"""
Exemplo de aplicação com CEF Python
Integração com Google Chrome/HTML5
"""

from cefpython3 import cefpython as cef
import platform
import sys

def main():
    """Função principal"""
    # Configurações para diferentes sistemas operacionais
    check_versions()
    sys.excepthook = cef.ExceptHook  # Para capturar exceções
    
    # Configurações do CEF
    settings = {
        "multi_threaded_message_loop": False,
        "window_title": "Exemplo CEF Python - Olá, Mundo!",
    }
    
    # Inicializar o CEF
    cef.Initialize(settings)
    
    # Criar a janela do navegador
    window_info = cef.WindowInfo()
    window_info.SetAsPopup("Exemplo CEF Python", width=800, height=600)
    
    # HTML personalizado
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                max-width: 600px;
                margin: 50px auto;
                text-align: center;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2em;
                line-height: 1.6;
            }
            button {
                background: white;
                color: #764ba2;
                border: none;
                padding: 15px 30px;
                font-size: 1.1em;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 20px;
            }
            button:hover {
                transform: scale(1.05);
                transition: 0.3s;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Olá, mundo!</h1>
            <p>Este é o primeiro exemplo do CEF Python.</p>
            <p>Uma aplicação GUI com integração ao Chrome/HTML5.</p>
            <button onclick="alert('Botão clicado!')">
                Clique aqui
            </button>
        </div>
    </body>
    </html>
    """
    
    # Criar o navegador com o HTML personalizado
    browser = cef.CreateBrowserSync(window_info, url="about:blank")
    browser.SetClientHandler(LoadHandler())
    browser.LoadUrl("data:text/html," + html_code.replace(" ", "%20").replace("\n", ""))
    
    # Loop de mensagens
    cef.MessageLoop()
    
    # Finalizar
    cef.Shutdown()

def check_versions():
    """Verificar versões e sistema operacional"""
    ver = cef.GetVersion()
    print("CEF Python {ver}".format(ver=ver["version"]))
    print("Chromium {ver}".format(ver=ver["chrome_version"]))
    print("CFFI {ver}".format(ver=ver["cffi_version"]))
    print("Python {ver}".format(ver=platform.python_version()))
    print("Sistema: {system}".format(system=platform.system()))

class LoadHandler(object):
    """Handler para eventos de carregamento"""
    
    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Chamado quando o estado de carregamento muda"""
        if not is_loading:
            print("Página carregada com sucesso!")

if __name__ == '__main__':
    main()
