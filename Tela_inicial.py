import Banco_de_dados
import PySimpleGUI as sg
def telaInicial():
    locadora = Banco_de_dados.BancodeDados.recuperarLocadora()
    if locadora == None or locadora == '':
        layout_TelaInicial = \
            [
                [sg.Column(layout=[
                    [sg.Text('Nome da Locadora:')],
                    [sg.Text('Endereço:')],
                    [sg.Text('Website:')],
                    [sg.Text('Rede Social:')]
                ]),
                sg.Column(layout=[
                    [sg.InputText(key='nomeLocadora')],
                    [sg.InputText(key='endereco')],
                    [sg.InputText(key='website')],
                    [sg.InputText(key='redeSocial')]
                    ])
                ],
                [sg.Button('Salvar', key='btnSalvar')]
            ]
        window = sg.Window('Primeiro uso', layout_TelaInicial, finalize=True, no_titlebar=True,
                           grab_anywhere=False, modal=True)

        event, values = window.read()
        while True:
            if event == sg.WIN_CLOSED:
                window.close()
                break
            if event == 'btnSalvar':
                if values['nomeLocadora'] != '' and values['endereco'] != '' and values['website'] != '' and values[
                    'redeSocial'] != '':
                    Banco_de_dados.BancodeDados.criarLocadora({'_nome':values['nomeLocadora'],'_endereco': values['endereco'],
                                                             '_website':values['website'],'_redeSocial': values['redeSocial']})
                    window.close()
                    return [values['nomeLocadora'], values['endereco'], values['website'], values['redeSocial']]
                    break
                else:
                    popup = sg.popup_error('Todos os campos devem ser preenchidos!')
    else:
        return [locadora['_nome'], locadora['_endereco'], locadora['_website'], locadora['_redeSocial']]