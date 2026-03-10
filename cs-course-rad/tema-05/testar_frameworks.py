
"""
Script para testar se os frameworks estão instalados corretamente
"""

import sys
import importlib

def testar_framework(nome, modulo):
    """Testa se um framework está instalado"""
    try:
        importlib.import_module(modulo)
        return True
    except ImportError:
        return False

def main():
    """Função principal"""
    print("=" * 60)
    print("VERIFICANDO FRAMEWORKS GUI INSTALADOS")
    print("=" * 60)
    
    frameworks = [
        ("Tkinter", "tkinter"),
        ("Flexx", "flexx"),
        ("CEF Python", "cefpython3"),
        ("Kivy", "kivy"),
        ("Pyforms", "pyforms"),
        ("PyQt5", "PyQt5"),
        ("wxPython", "wx"),
        ("PyAutoGUI", "pyautogui"),
        ("PySimpleGUI", "PySimpleGUI"),
    ]
    
    print(f"\nPython: {sys.version}\n")
    print("Status dos frameworks:\n")
    
    for nome, modulo in frameworks:
        if testar_framework(nome, modulo):
            print(f"✅ {nome:15} - INSTALADO")
        else:
            print(f"❌ {nome:15} - NÃO INSTALADO")
    
    print("\n" + "=" * 60)
    print("\nComandos de instalação:")
    print("-" * 40)
    print("pip install tkinter")
    print("pip install flexx")
    print("pip install cefpython3")
    print("pip install kivy")
    print("pip install pyforms")
    print("pip install PyQt5")
    print("pip install wxPython")
    print("pip install pyautogui")
    print("pip install PySimpleGUI")
    print("=" * 60)

if __name__ == "__main__":
    main()
