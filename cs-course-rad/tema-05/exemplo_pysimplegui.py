
"""
Exemplo de aplicação com PySimpleGUI
Framework simples e portável
"""

import PySimpleGUI as sg

def criar_janela():
    """Função para criar a interface"""
    
    # Definir o tema
    sg.theme('GreenTan')
    
    # Layout da janela
    layout = [
        [sg.Text('Exemplo PySimpleGUI', font=('Arial', 18, 'bold'))],
        [sg.Text('Framework simples e portável', font=('Arial', 10))],
        [sg.HorizontalSeparator()],
        [sg.Text('Label 1:', size=(10, 1)), sg.InputText(key='-INPUT1-', size=(30, 1))],
        [sg.Text('Label 2:', size=(10, 1)), sg.InputText(key='-INPUT2-', size=(30, 1))],
        [sg.HorizontalSeparator()],
        [sg.Button('Botão 1', size=(10, 1)), sg.Button('Botão 2', size=(10, 1)), sg.Button('Sair', size=(10, 1))],
        [sg.Output(size=(50, 5), key='-OUTPUT-')]
    ]
    
    # Criar a janela
    return sg.Window(
        'Exemplo PySimpleGUI',
        layout,
        finalize=True,
        resizable=True,
        element_justification='center'
    )

def main():
    """Função principal"""
    
    print("=" * 50)
    print("Exemplo PySimpleGUI - Iniciando aplicação")
    print("=" * 50)
    print("\nInteraja com a janela que será aberta...")
    
    # Criar a janela
    janela = criar_janela()
    
    # Loop de eventos
    while True:
        event, values = janela.read()
        
        # Verificar se a janela foi fechada
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        
        # Botão 1
        elif event == 'Botão 1':
            print(f"\n✅ Botão 1 clicado!")
            texto1 = values['-INPUT1-']
            texto2 = values['-INPUT2-']
            
            if texto1 and texto2:
                print(f"   Input 1: {texto1}")
                print(f"   Input 2: {texto2}")
                print(f"   Mensagem: Olá, {texto1} e {texto2}!")
                
                # Popup de confirmação
                sg.popup_ok(
                    f'Olá, {texto1} e {texto2}!',
                    title='Saudação',
                    keep_on_top=True
                )
            else:
                print("   ⚠️ Por favor, preencha ambos os campos!")
                sg.popup_error(
                    'Preencha ambos os campos!',
                    title='Erro',
                    keep_on_top=True
                )
        
        # Botão 2
        elif event == 'Botão 2':
            print(f"\n✅ Botão 2 clicado!")
            
            # Pegar valores atuais
            texto1 = values['-INPUT1-'] or 'vazio'
            texto2 = values['-INPUT2-'] or 'vazio'
            
            print(f"   Valores atuais:")
            print(f"     Input 1: {texto1}")
            print(f"     Input 2: {texto2}")
            
            # Perguntar se quer limpar
            resposta = sg.popup_yes_no(
                'Deseja limpar os campos?',
                title='Confirmação',
                keep_on_top=True
            )
            
            if resposta == 'Yes':
                janela['-INPUT1-'].update('')
                janela['-INPUT2-'].update('')
                print("   🧹 Campos limpos!")
                sg.popup_notify('Campos limpos!', title='Info')
            else:
                print("   Operação cancelada")
    
    # Fechar a janela
    janela.close()
    print("\n👋 Aplicação encerrada!")

def exemplo_alternativo():
    """Exemplo alternativo mais compacto"""
    
    # Layout mais simples
    layout = [
        [sg.Text('Calculadora Simples', font=('Arial', 14))],
        [sg.InputText(size=(10, 1), key='-NUM1-'), sg.Text('+'), 
         sg.InputText(size=(10, 1), key='-NUM2-'), sg.Text('='), 
         sg.Text('', size=(10, 1), key='-RESULTADO-')],
        [sg.Button('Calcular'), sg.Button('Limpar'), sg.Button('Fechar')]
    ]
    
    janela = sg.Window('Calculadora PySimpleGUI', layout)
    
    while True:
        event, values = janela.read()
        
        if event in (sg.WIN_CLOSED, 'Fechar'):
            break
        
        if event == 'Limpar':
            janela['-NUM1-'].update('')
            janela['-NUM2-'].update('')
            janela['-RESULTADO-'].update('')
        
        if event == 'Calcular':
            try:
                num1 = float(values['-NUM1-'])
                num2 = float(values['-NUM2-'])
                resultado = num1 + num2
                janela['-RESULTADO-'].update(f'{resultado}')
                sg.popup_quick_message(f'Resultado: {resultado}', auto_close_duration=2)
            except ValueError:
                sg.popup_error('Digite números válidos!')
    
    janela.close()

if __name__ == '__main__':
    # Executar o exemplo principal
    main()
    
    # Descomente a linha abaixo para testar o exemplo alternativo
    # exemplo_alternativo()
