
"""
Exemplo de aplicação com PyAutoGUI
Controle de mouse e teclado para automação
"""

import pyautogui
import time
import subprocess
import sys

def main():
    """Função principal"""
    print("=" * 50)
    print("Exemplo PyAutoGUI - Automação de Mouse e Teclado")
    print("=" * 50)
    print("\nEste programa vai demonstrar:")
    print("1. Obter informações da tela")
    print("2. Mover o mouse")
    print("3. Clicar")
    print("4. Digitar texto")
    print("5. Mostrar alertas")
    print("\nA demonstração começará em 3 segundos...")
    print("(Mova o mouse para o canto superior esquerdo para interromper)")
    
    time.sleep(3)
    
    try:
        # 1. Obter tamanho do monitor
        print("\n📌 Obtendo informações da tela...")
        largura, altura = pyautogui.size()
        print(f"   Monitor: {largura} x {altura} pixels")
        
        # 2. Obter posição atual do mouse
        print("\n📌 Posição atual do mouse...")
        x, y = pyautogui.position()
        print(f"   Mouse em: ({x}, {y})")
        
        # 3. Mover o mouse para uma posição específica
        print("\n📌 Movendo mouse para (100, 100)...")
        pyautogui.moveTo(100, 100, duration=1)
        time.sleep(0.5)
        
        # 4. Clicar
        print("\n📌 Clicando...")
        pyautogui.click()
        time.sleep(0.5)
        
        # 5. Mover relativo e clicar
        print("\n📌 Movendo 50 pixels para baixo e clicando...")
        pyautogui.moveRel(0, 50, duration=1)
        pyautogui.click()
        time.sleep(0.5)
        
        # 6. Duplo clique
        print("\n📌 Duplo clique...")
        pyautogui.doubleClick()
        time.sleep(0.5)
        
        # 7. Mover com interpolação/atenuação
        print("\n📌 Movimento suave por 2 segundos...")
        pyautogui.moveTo(300, 300, duration=2, tween=pyautogui.easeInOutQuad)
        time.sleep(0.5)
        
        # 8. Abrir o Bloco de Notas (no Windows)
        print("\n📌 Abrindo Bloco de Notas...")
        if sys.platform == "win32":
            subprocess.Popen(["notepad.exe"])
            time.sleep(2)
        else:
            print("   (Pulando - recurso específico do Windows)")
        
        # 9. Digitar texto
        print("\n📌 Digitando mensagem...")
        mensagem = "Esta é a mensagem para tela"
        pyautogui.write(mensagem, interval=0.1)
        time.sleep(0.5)
        
        # 10. Pressionar teclas
        print("\n📌 Pressionando Enter...")
        pyautogui.press('enter')
        time.sleep(0.5)
        
        # 11. Usar atalhos
        print("\n📌 Selecionando tudo (Ctrl+A)...")
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        
        # 12. Pressionar setas
        print("\n📌 Pressionando Shift + seta para esquerda...")
        pyautogui.keyDown('shift')
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.keyUp('shift')
        time.sleep(0.5)
        
        # 13. Copiar (Ctrl+C)
        print("\n📌 Copiando (Ctrl+C)...")
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        
        # 14. Mostrar alerta
        print("\n📌 Mostrando alerta...")
        pyautogui.alert(
            text='Demonstração concluída!',
            title='PyAutoGUI',
            button='OK'
        )
        
        print("\n✅ Demonstração finalizada com sucesso!")
        
    except pyautogui.FailSafeException:
        print("\n⚠️ Demonstração interrompida pelo usuário!")
    except Exception as e:
        print(f"\n❌ Erro: {e}")

def exemplos_adicionais():
    """Função com exemplos adicionais comentados"""
    
    # Exemplos de funções disponíveis no PyAutoGUI
    
    # # Posição do mouse
    # pyautogui.position()  # Obtém posição atual
    
    # # Movimentos
    # pyautogui.moveTo(100, 200)  # Move para coordenada absoluta
    # pyautogui.moveRel(50, 0)     # Move relativo
    
    # # Cliques
    # pyautogui.click()              # Clique simples
    # pyautogui.doubleClick()        # Duplo clique
    # pyautogui.rightClick()         # Clique direito
    # pyautogui.middleClick()        # Clique do meio
    
    # # Scroll
    # pyautogui.scroll(10)           # Rola para cima
    # pyautogui.scroll(-10)          # Rola para baixo
    
    # # Teclado
    # pyautogui.write('Hello world') # Digita texto
    # pyautogui.press('enter')       # Pressiona uma tecla
    # pyautogui.keyDown('shift')     # Segura uma tecla
    # pyautogui.keyUp('shift')       # Solta uma tecla
    # pyautogui.hotkey('ctrl', 'c')  # Atalho
    
    # # Alertas
    # pyautogui.alert('Mensagem')    # Alerta simples
    # pyautogui.confirm('Confirma?') # Caixa de confirmação
    # pyautogui.prompt('Digite:')    # Caixa de entrada
    
    pass

if __name__ == '__main__':
    main()
    # exemplos_adicionais()
