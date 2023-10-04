import Banco_de_dados
import PySimpleGUI as sg
def telaInicial():
    locadora = Banco_de_dados.BancodeDados.recuperarLocadora()
    if locadora == None or locadora == '':
        layout_TelaInicial = \
            [
                [sg.Text('Nome da Locadora:'), sg.InputText(key='nomeLocadora'), sg.Text('Endereço:'),
                 sg.InputText(key='endereco')],
                [sg.Text('Website:'), sg.InputText(key='website'), sg.Text('Rede Social:'),
                 sg.InputText(key='redeSocial')],
                [sg.Button('Salvar', key='btnSalvar')]
            ]
        window = sg.Window('Primeiro uso', layout_TelaInicial, finalize=True, icon=tela.caminho_icone, no_titlebar=True,
                           grab_anywhere=False, modal=True)

        event, values = window.read()
        while True:
            if event == sg.WIN_CLOSED:
                window.close()
                break
            if event == 'btnSalvar':
                if values['nomeLocadora'] != '' and values['endereco'] != '' and values['website'] != '' and values[
                    'redeSocial'] != '':
                    self.locadora.configuracao.criarLocadora(values['nomeLocadora'], values['endereco'],
                                                             values['website'], values['redeSocial'])
                    return [values['nomeLocadora'], values['endereco'], values['website'], values['redeSocial']]
                    window.close()
                    break
                else:
                    popup = sg.popup_error('Todos os campos devem ser preenchidos!')
    else:
        return [locadora.nome, locadora.endereco, locadora.website, locadora.redeSocial]