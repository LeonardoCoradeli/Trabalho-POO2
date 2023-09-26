import PySimpleGUI as sg
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_icone = os.path.join(diretorio_atual, 'assets', 'tela_icon.ico')

sg.theme('BlueMono')
listadeCNH = ['A','B','C','D','E']
relatoriosVeiculos =[sg.Frame('Veiculos',layout=[
                    [sg.Radio('Todos', group_id='veiculos', default=True,key='todosVeiculos'), sg.Radio('Nacionais', group_id='veiculos'),sg.Radio('Importados', group_id='veiculos')],
                    [sg.Radio('Disponivel', group_id='veiculos'),sg.Radio('Locado', group_id='veiculos'),sg.Radio('Devolução atrasada', group_id='veiculos')],
                    [sg.Radio('CNH Necessaria', group_id='veiculos',key='CNHNecessaria')],
                    [sg.Button('Gerar',key='btnveiculos')]
                    ],vertical_alignment='c',key='frameVeiculos',size=(330,150))]
relatoriosVeiculos_popup = [
                            [sg.Combo(['A', 'B', 'C', 'D', 'E'], default_value='A', key='combo')],
                            [sg.Button('Gerar'),sg.Button('Cancelar')],
                            ]

relatoriosClientes =[sg.Frame('Clientes',layout=[
                    [sg.Radio('Todos', group_id='clientes', default=True,key='todosClientes'), sg.Radio('Locações com atraso', group_id='clientes')],
                    [sg.Radio('Veiculo Especifico', group_id='clientes',key='clienteVeiculoAtrasado')],
                    [sg.Button('Gerar',key='btnclientes')]
                ],size=(330,120))]
#mudar esses input para combo com respectivos dados
relatoriosClientes_popup = [[sg.Text('Placa'),sg.InputText(key='placaVeiculo',size=(10,1))],
                            [sg.Text('Codigo do Veiculo'),sg.InputText(key='codveiculo',size=(10,1))],
                            [sg.Button('Gerar'),sg.Button('Cancelar')]]

relatoriosLocacoes =[sg.Frame('Locações',layout=[
                    [sg.Radio('Todos', group_id='locacoes', default=True,key='todosLocacoes'),sg.Radio('Finalizadas', group_id='locacoes'),sg.Radio('Atrasadas', group_id='locacoes')],
                    [sg.Radio('Cliente especifico', group_id='locacoes'),sg.Radio('Mês especifico', group_id='locacoes')],
                    [sg.Radio('Não finalizadas',group_id='locacoes')],
                    [sg.Button('Gerar',key='btnlocacoes')]
                    ],size=(330,150))]

layout_TelaRelatorios = [
    [sg.Column(layout=[relatoriosVeiculos,relatoriosClientes,relatoriosLocacoes]),sg.Column(layout=[[sg.Multiline(size=(400,450),disabled=True)]])]
]

layoutvazio = [[]]


layout_Geral = [[sg.TabGroup([[
                    sg.Tab('Locação',layoutvazio),
                    sg.Tab('Relatórios',layout_TelaRelatorios),
                    sg.Tab('Busca',layoutvazio),
                    sg.Tab('Cadastro',layoutvazio),
]],size=(900,600))]]

window = sg.Window('Locadora de Veículos',layout_Geral,finalize=True)

window.set_icon(caminho_icone)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Cancelar'):
        break
    if event == 'btnveiculos':
        if values['CNHNecessaria']:
            popup_window = sg.Window(title='CNH', layout=relatoriosVeiculos_popup, modal=True,size=(150,80))

            while True:
                popup_event, popup_values = popup_window.read()

                if popup_event == sg.WIN_CLOSED:
                    break
                elif popup_event == 'Cancelar':
                    window['todosVeiculos'].update(True)
                    popup_window.close()
                elif popup_event == 'Gerar':
                    window['todosVeiculos'].update(True)
                    sg.popup('Trabalhando nisso.')
                    popup_window.close()
    if event == 'btnclientes':
        if values['clienteVeiculoAtrasado']:
            popup_window = sg.Window('Atrasado', relatoriosClientes_popup, modal=True)

            while True:
                popup_event, popup_values = popup_window.read()

                if popup_event == sg.WIN_CLOSED:
                    break
                elif popup_event == 'Cancelar':
                    window['todosClientes'].update(True)
                    popup_window.close()
                elif popup_event == 'Gerar':
                    sg.popup('Trabalhando nisso.')
                    window['todosClientes'].update(True)
                    popup_window.close()


window.close()

