import PySimpleGUI as sg

sg.theme('BlueMono')

relatorios = [[sg.Text('Relatórios')],
              [sg.Checkbox('Testando')],
              [sg.Button('Teste')]
              ]

layout_TelaRelatorios = [[
    sg.Frame('',layout=relatorios,size=(120,100),vertical_alignment='c'),sg.Multiline()
                        ]]

layout_Geral = [[layout_TelaRelatorios]]

window = sg.Window('Window Title',layout_Geral,size=(500,500))

event, values = window.read()
window.close()

