import PySimpleGUI as sg
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_icone = os.path.join(diretorio_atual, 'assets', 'tela_icon.ico')

sg.theme('BlueMono')

# Tela de relatórios
listadeCNH = ['A', 'B', 'C', 'D', 'E']
relatoriosVeiculos = [sg.Frame('Veiculos', layout=[
    [sg.Radio('Todos', group_id='veiculos', default=True, key='todosVeiculos'),
     sg.Radio('Nacionais', group_id='veiculos'), sg.Radio('Importados', group_id='veiculos')],
    [sg.Radio('Disponivel', group_id='veiculos'), sg.Radio('Locado', group_id='veiculos'),
     sg.Radio('Devolução atrasada', group_id='veiculos')],
    [sg.Radio('CNH Necessaria', group_id='veiculos', key='CNHNecessaria')],
    [sg.Button('Gerar', key='btnveiculos')]
], vertical_alignment='c', key='frameVeiculos', size=(330, 150))]
relatoriosVeiculos_popup = [
    [sg.Combo(['A', 'B', 'C', 'D', 'E'], default_value='A', key='combo')],
    [sg.Button('Gerar'), sg.Button('Cancelar')],
]

relatoriosClientes = [sg.Frame('Clientes', layout=[
    [sg.Radio('Todos', group_id='clientes', default=True, key='todosClientes'),
     sg.Radio('Locações com atraso', group_id='clientes')],
    [sg.Radio('Veiculo Especifico', group_id='clientes', key='clienteVeiculoAtrasado')],
    [sg.Button('Gerar', key='btnclientes')]
], size=(330, 120))]
# mudar esses input para combo com respectivos dados
relatoriosClientes_popup = [[sg.Text('Placa'), sg.InputText(key='placaVeiculo', size=(10, 1))],
                            [sg.Text('ou')],
                            [sg.Text('Codigo do Veiculo'), sg.InputText(key='codveiculo', size=(10, 1))],
                            [sg.Button('Gerar'), sg.Button('Cancelar')]]

relatoriosLocacoes = [sg.Frame('Locações', layout=[
    [sg.Radio('Todos', group_id='locacoes', default=True, key='todosLocacoes'),
     sg.Radio('Finalizadas', group_id='locacoes'), sg.Radio('Atrasadas', group_id='locacoes')],
    [sg.Radio('Cliente especifico', group_id='locacoes'), sg.Radio('Mês especifico', group_id='locacoes')],
    [sg.Radio('Não finalizadas', group_id='locacoes', key='NaoFinalizadas')],
    [sg.Button('Gerar', key='btnlocacoes')]
], size=(330, 150))]
relatoriosLocacoes_popup = [[sg.Radio('Todos', group_id='locacoes_popup', default=True, key='todosNaoFinalizados'),
                             sg.Radio('Veiculos Nacionais', group_id='locacoes_popup',
                                      key='todosNaoFinalizadosNacionais'),
                             sg.Radio('Veiculos Importados', group_id='locacoes_popup',
                                      key='todosNaoFinalizadosImportados')],
                            [sg.Button('Gerar'), sg.Button('Cancelar')]
                            ]

relatorioFuncionarios = [sg.Frame('Funcionarios', layout=[
    [sg.Radio('Todos', group_id='funcionarios', default=True, key='todosfuncionarios'),
     sg.Radio('Funcionario do mês', group_id='funcionarios', key='funcionarioMes')],
    [sg.Button('Gerar', key='btnFuncionario')]
], size=(330, 100))
                         ]

layout_TelaRelatorios = [
    [sg.Column(layout=[relatoriosVeiculos, relatoriosClientes, relatoriosLocacoes, relatorioFuncionarios]),
     sg.Column(layout=[[sg.Multiline(size=(400, 450), disabled=True)]])]
]

#Cadastro
cadastroDefault = \
[
                    [sg.Text('Seja bem vindo ao sistema de cadastro!')],
                    [sg.Text('Escolha uma das opções abaixo para começar:')],
                    [sg.Button('Funcionario', size=(20, 1), pad=(10, 10),key='btncadFuncionario')],
                    [sg.Button('Cliente', size=(20, 1), pad=(10, 10),key='btncadCliente')],
                    [sg.Button('Veiculo Nacional', size=(20, 1), pad=(10, 10),key='btncadVeiculoNacional')],
                    [sg.Button('Veiculo Importado', size=(20, 1), pad=(10, 10),key='btncadVeiculoImportado')],
]

cadastroFuncionario = \
[
                        [sg.Text('Nome:'), sg.InputText(size=(20, 1), key='nome')],
                        [sg.Text('CPF:'), sg.InputText(size=(20, 1), key='cpf')],
                        [sg.Text('RG:'), sg.InputText(size=(20, 1), key='rg')],
                        [sg.Text('Data de Nascimento:'), sg.InputText(size=(20, 1), key='dataNascimento')],
                        [sg.Text('Endereço:'), sg.InputText(size=(20, 1), key='endereco')],
                        [sg.Text('E-mail:'), sg.InputText(size=(20, 1), key='email')],
                        [sg.Text('CEP:'), sg.InputText(size=(20, 1), key='cep')],
                        [sg.Text('Salario:'), sg.InputText(size=(20, 1), key='salario')],
                        [sg.Text('Pis:'), sg.InputText(size=(20, 1), key='pis')],
                        [sg.Text('Data de Admissão:'), sg.InputText(size=(20, 1), key='dataAdmissao')],
                        [sg.Button('Salvar', key='salvarFuncionario', size=(20, 1), pad=(0, 20))],
]

cadastroCliente = \
[
                    [sg.Text('Nome:'), sg.InputText(size=(20, 1), key='nome')],
                    [sg.Text('CPF:'), sg.InputText(size=(20, 1), key='cpf')],
                    [sg.Text('RG:'), sg.InputText(size=(20, 1), key='rg')],
                    [sg.Text('Data de Nascimento:'), sg.InputText(size=(20, 1), key='dataNascimento')],
                    [sg.Text('Endereço:'), sg.InputText(size=(20, 1), key='endereco')],
                    [sg.Text('E-mail:'), sg.InputText(size=(20, 1), key='email')],
                    [sg.Text('CEP:'), sg.InputText(size=(20, 1), key='cep')],
                    [sg.Text('Categoria da CNH:'), sg.InputText(size=(20, 1), key='categoriaCNH')],
                    [sg.Text('Número da CNH:'), sg.InputText(size=(20, 1), key='numeroCNH')],
                    [sg.Text('Data de Validade da CNH:'), sg.InputText(size=(20, 1), key='dataValidadeCNH')],
                    [sg.Text('Cliente Ouro:'), sg.InputText(size=(20, 1), key='clienteOuro')],
                    [sg.Button('Salvar', key='salvarCliente', size=(20, 1), pad=(0, 20))],
]

cadastroVeiculoNacional = \
[
                            [sg.Text('Nome do Modelo:'), sg.InputText(size=(20, 1), key='nomeModelo')],
                            [sg.Text('Montadora:'), sg.InputText(size=(20, 1), key='montadora')],
                            [sg.Text('Ano de Fabricação:'), sg.InputText(size=(20, 1), key='anoFabricacao')],
                            [sg.Text('Ano do Modelo:'), sg.InputText(size=(20, 1), key='anoModelo')],
                            [sg.Text('Placa:'), sg.InputText(size=(20, 1), key='placa')],
                            [sg.Text('Categoria:'), sg.InputText(size=(20, 1), key='categoria')],
                            [sg.Text('Valor Fipe:'), sg.InputText(size=(20, 1), key='valorFipe')],
                            [sg.Text('Valor da Diária:'), sg.InputText(size=(20, 1), key='valorDiaria')],
                            [sg.Text('Categoria da CNH:'), sg.InputText(size=(20, 1), key='categoriaCNH')],
                            [sg.Text('Taxa do Imposto Estadual:'), sg.InputText(size=(20, 1), key='taxaImpostoEstadual')],
                            [sg.Button('Salvar', key='salvarVeiculoNacional', size=(20, 1), pad=(0, 20))],
]

cadastroVeiculoImportado = \
[
                            [sg.Text('Nome do Modelo:'), sg.InputText(size=(20, 1), key='nomeModelo')],
                            [sg.Text('Montadora:'), sg.InputText(size=(20, 1), key='montadora')],
                            [sg.Text('Ano de Fabricação:'), sg.InputText(size=(20, 1), key='anoFabricacao')],
                            [sg.Text('Ano do Modelo:'), sg.InputText(size=(20, 1), key='anoModelo')],
                            [sg.Text('Placa:'), sg.InputText(size=(20, 1), key='placa')],
                            [sg.Text('Categoria:'), sg.InputText(size=(20, 1), key='categoria')],
                            [sg.Text('Valor Fipe:'), sg.InputText(size=(20, 1), key='valorFipe')],
                            [sg.Text('Valor da Diária:'), sg.InputText(size=(20, 1), key='valorDiaria')],
                            [sg.Text('Categoria da CNH:'), sg.InputText(size=(20, 1), key='categoriaCNH')],
                            [sg.Text('Taxa do Imposto Estadual:'), sg.InputText(size=(20, 1), key='taxaImpostoEstadual')],
                            [sg.Text('Taxa do Imposto Federal:'), sg.InputText(size=(20, 1), key='taxaImpostoFeredal')],
                            [sg.Button('Salvar', key='salvarVeiculoImportado', size=(20, 1), pad=(0, 20))],
]

menuLayout = [['Cadastro', ['Funcionario', 'Cliente', 'Veiculo Nacional', 'Veiculo Importado']]]

layout = [
    [sg.Text('CADASTRO')],
    [cadastroDefault]]


layoutvazio = [[]]



layout_Geral = [[sg.TabGroup([[
    sg.Tab('Locação', layoutvazio),
    sg.Tab('Relatórios', layout_TelaRelatorios),
    sg.Tab('Busca', layoutvazio),
    sg.Tab('Cadastro', cadastroDefault),
]], size=(900, 600))]]

window = sg.Window('Locadora de Veículos', layout_Geral, finalize=True)

window.set_icon(caminho_icone)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Cancelar'):
        break
    if event == 'btnveiculos':
        if values['CNHNecessaria']:
            popup_window = sg.Window(title='CNH', layout=relatoriosVeiculos_popup, modal=True, size=(150, 80))

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
    if event == 'btnlocacoes':
        if values['NaoFinalizadas']:
            popup_window = sg.Window('Não finalizadas', relatoriosLocacoes_popup, modal=True)

            while True:
                popup_event, popup_values = popup_window.read()

                if popup_event == sg.WIN_CLOSED:
                    break
                elif popup_event == 'Cancelar':
                    window['todosLocacoes'].update(True)
                    popup_window.close()
                elif popup_event == 'Gerar':
                    sg.popup('Trabalhando nisso.')
                    window['todosLocacoes'].update(True)
                    popup_window.close()
    if event == 'cadFuncionario':
        window = sg.Window('Cadastro de Funcionário', cadastroFuncionario, size=(400, 330), element_justification='c')
    if event == 'cadCliente':
        window = sg.Window('Cadastro de Cliente', cadastroCliente, size=(400, 350), element_justification='c')
    if event == 'cadVeiculoNacional':
        window = sg.Window('Cadastro de Veiculo Nacional', cadastroVeiculoNacional, size=(400, 350),
                           element_justification='c')
    if event == 'cadVeiculoImportado':
        window = sg.Window('Cadastro de Veiculo Importado', cadastroVeiculoImportado, size=(400, 350),
                           element_justification='c')

    if event == 'salvarFuncionario':
        if window.Title == 'Cadastro de Funcionário':
            if values['nome'] != '' and values['cpf'] != '' and values['rg'] != '' and values[
                'dataNascimento'] != '' and values['endereco'] != '' and values['email'] != '' and values[
                'cep'] != '' and values['salario'] != '' and values['pis'] != '' and values['dataAdmissao'] != '':
                ## Salvar no banco
                pass
            else:
                sg.popup_error("Todos os campos devem ser preenchidos!")

    if event == 'salvarCliente':
        if window.Title == 'Cadastro de Cliente':
            if values['nome'] != '' and values['cpf'] != '' and values['rg'] != '' and values[
                'dataNascimento'] != '' and values['endereco'] != '' and values['email'] != '' and values[
                'cep'] != '' and values['categoriaCNH'] != '' and values['numeroCNH'] != '' and values[
                'dataValidadeCNH'] != '' and values['clienteOuro'] != '':
                ## Salvar no banco
                pass
            else:
                sg.popup_error("Todos os campos devem ser preenchidos!")

    if event == 'salvarVeiculoNacional':
        if window.Title == 'Cadastro de Veiculo Nacional':
            if values['nomeModelo'] != '' and values['montadora'] != '' and values['anoFabricacao'] != '' and values[
                'anoModelo'] != '' and values['placa'] != '' and values['categoria'] != '' and values[
                'valorFipe'] != '' and values['valorDiaria'] != '' and values['categoriaCNH'] != '' and values[
                'taxaImpostoEstadual'] != '':
                ## Salvar no banco
                pass
            else:
                sg.popup_error("Todos os campos devem ser preenchidos!")

    if event == 'salvarVeiculoImportado':
        if window.Title == 'Cadastro de Veiculo Importado':
            if values['nomeModelo'] != '' and values['montadora'] != '' and values['anoFabricacao'] != '' and values[
                'anoModelo'] != '' and values['placa'] != '' and values['categoria'] != '' and values[
                'valorFipe'] != '' and values['valorDiaria'] != '' and values['categoriaCNH'] != '' and values[
                'taxaImpostoEstadual'] != '' and values['taxaImpostoFeredal'] != '':
                ## Salvar no banco
                pass
            else:
                sg.popup_error("Todos os campos devem ser preenchidos!")

window.close()
