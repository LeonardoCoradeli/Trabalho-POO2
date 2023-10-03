import PySimpleGUI as sg
import os
import Locadora, Banco_de_dados, Veiculos, Locacoes, Usuario

locadora = Locadora.Locadora("Teste","Teste","Teste","Teste")

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_icone = os.path.join(diretorio_atual, 'assets', 'tela_icon.ico')

sg.theme('BlueMono')

# Tela de relatórios
listadeCNH = ['A', 'B', 'C', 'D', 'E']
relatoriosVeiculos = \
[
                        sg.Frame('Veiculos', layout=[
                        [sg.Radio('Todos', group_id='veiculos', default=True, key='todosVeiculos'),
                         sg.Radio('Nacionais', group_id='veiculos'), sg.Radio('Importados', group_id='veiculos')],
                        [sg.Radio('Disponivel', group_id='veiculos'), sg.Radio('Locado', group_id='veiculos'),
                         sg.Radio('Devolução atrasada', group_id='veiculos')],
                        [sg.Radio('CNH Necessaria', group_id='veiculos', key='CNHNecessaria')],
                        [sg.Button('Gerar', key='btnveiculos')]], vertical_alignment='c', key='frameVeiculos', size=(330, 150))

]


relatoriosClientes = \
[
                        sg.Frame('Clientes', layout=[
                        [sg.Radio('Todos', group_id='clientes', default=True, key='todosClientes'),
                         sg.Radio('Locações com atraso', group_id='clientes')],
                        [sg.Radio('Veiculo Especifico', group_id='clientes', key='clienteVeiculoAtrasado')],
                        [sg.Button('Gerar', key='btnclientes')]], size=(330, 120))
]
# mudar esses input para combo com respectivos dados

relatoriosLocacoes = \
[
                        sg.Frame('Locações', layout=[
                        [sg.Radio('Todos', group_id='locacoes', default=True, key='todosLocacoes'),
                         sg.Radio('Finalizadas', group_id='locacoes'), sg.Radio('Atrasadas', group_id='locacoes')],
                        [sg.Radio('Cliente especifico', group_id='locacoes'), sg.Radio('Mês especifico', group_id='locacoes')],
                        [sg.Radio('Não finalizadas', group_id='locacoes', key='NaoFinalizadas')],
                        [sg.Button('Gerar', key='btnlocacoes')]], size=(330, 150))
]

relatorioFuncionarios = \
[
                        sg.Frame('Funcionarios', layout=[
                        [sg.Radio('Todos', group_id='funcionarios', default=True, key='todosfuncionarios'),
                         sg.Radio('Funcionario do mês', group_id='funcionarios', key='funcionarioMes')],
                        [sg.Button('Gerar', key='btnFuncionario')]], size=(330, 100))
]

layout_TelaRelatorios = [
    [sg.Column(layout=[relatoriosVeiculos, relatoriosClientes, relatoriosLocacoes, relatorioFuncionarios]),
     sg.Column(layout=[[sg.Multiline(size=(400, 450), disabled=True, key='textoRelatorios')]])]
]

#Cadastro
cadastroDefault = \
[
                    [sg.Text('Seja bem vindo ao sistema de cadastro!')],
                    [sg.Text('Escolha uma das opções abaixo para começar:')],
                    [sg.Button('Funcionario', size=(20, 1), pad=(10, 10),key='btncadFuncionario')],
                    [sg.Button('Cliente', size=(20, 1), pad=(10, 10),key='btncadCliente')],
                    [sg.Button('Veiculo Nacional', size=(20, 1), pad=(10, 10),key='btnCadVeiculoNacional')],
                    [sg.Button('Veiculo Importado', size=(20, 1), pad=(10, 10),key='btnCadVeiculoImportado')],
                    [sg.Button('Seguro', size=(20, 1), pad=(10, 10),key='btnCadSeguro')],
]

def getNomeClientes():
    clientes = Banco_de_dados.BancodeDados.recuperarTodosClientes()
    aux = []
    for cliente in clientes:
        aux.append(cliente.nome)
    return aux


def getNomeFuncionarios():
    funcionarios = Banco_de_dados.BancodeDados.recuperarTodosFuncionarios()
    aux = []
    for funcionario in funcionarios:
        aux.append(funcionario.nome)
    return aux


def getNomeVeiculos():
    veiculosNacionais = Banco_de_dados.BancodeDados.recuperarNumeroVeiculosNacionais()
    veiculosImportados = Banco_de_dados.BancodeDados.recuperarNumeroVeiculosImportados()
    aux = []
    if veiculosNacionais != None:
        for veiculo in veiculosNacionais:
            aux.append(veiculo.nome)
    if veiculosImportados != None:
        for veiculo in veiculosImportados:
            aux.append(veiculo.nome)
    return aux


def getNomeSeguros():
    seguros = Banco_de_dados.BancodeDados.recuperarTodosSeguros()
    aux = []
    for seguro in seguros:
        aux.append(seguro.nome)
    return aux


locacaoLayout = [
                    [sg.Text('Locação')],
                    [sg.Text('Cliente:'), sg.Text('Funcionario:', pad=(100, 0))],
                    [sg.Combo([getNomeClientes()], default_value='', key='comboCliente'), sg.Combo([getNomeFuncionarios()], default_value='', key='comboFuncionario', pad=(40, 0))],
                    [sg.Text('Seguros:'), sg.Text('Veiculos:', pad=(100, 0))],
                    [sg.Combo([getNomeSeguros()], default_value='', key='comboSeguros'), sg.Combo([getNomeVeiculos()], default_value='', key='comboVeiculos', pad=(40, 0))],
                    [sg.Button('Salvar', key='btnAddLocacao', size=(20, 1), pad=(0, 20))],
]



menuLayout = [['Cadastro', ['Funcionario', 'Cliente', 'Veiculo Nacional', 'Veiculo Importado']]]

layout = [
    [sg.Text('CADASTRO')],
    cadastroDefault]


layoutvazio = [[]]

def createWindow(type):
    if type == 'cadastrarFuncionario':
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
        return sg.Window('Cadastro de Funcionário', cadastroFuncionario, size=(400, 350), element_justification='c')
    elif type == 'cadastrarCliente':
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
        return sg.Window('Cadastro de Cliente', cadastroCliente, size=(400, 350), element_justification='c')
    elif type == 'cadastrarVeiculoNacional':
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
        return sg.Window('Cadastro de Veiculo Nacional', cadastroVeiculoNacional, size=(400, 350), element_justification='c')
    elif type == 'cadastrarVeiculoImportado':
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
        return sg.Window('Cadastro de Veiculo Importado', cadastroVeiculoImportado, size=(400, 350), element_justification='c')
    elif type == 'cadastrarSeguro':
        cadastroSeguro = \
            [
                [sg.Text('Nome:'), sg.InputText(size=(20, 1), key='nome')],
                [sg.Text('Tipo:'), sg.InputText(size=(20, 1), key='tipo')],
                [sg.Text('Descrição:'), sg.InputText(size=(20, 1), key='descricao')],
                [sg.Text('Valor:'), sg.InputText(size=(20, 1), key='valor')],
                [sg.Button('Salvar', key='salvarSeguro', size=(20, 1), pad=(0, 20))],
            ]
        return sg.Window('Cadastro de Seguro', cadastroSeguro, size=(400, 350), element_justification='c')
    elif type == 'relatorioVeiculos':
        relatoriosVeiculos_popup = \
            [
                [sg.Combo(['A', 'B', 'C', 'D', 'E'], default_value='A', key='combo')],
                [sg.Button('Gerar'), sg.Button('Cancelar')],
            ]
        return sg.Window('Relatório de Veiculos', relatoriosVeiculos_popup, size=(150, 80), element_justification='c')
    elif type == 'relatorioClientes':
        relatoriosClientes_popup = \
            [
                [sg.Text('Placa'), sg.InputText(key='placaVeiculo', size=(10, 1))],
                [sg.Text('ou')],
                [sg.Text('Codigo do Veiculo'), sg.InputText(key='codveiculo', size=(10, 1))],
                [sg.Button('Gerar'), sg.Button('Cancelar')]
            ]
        return sg.Window('Relatório de Clientes', relatoriosClientes_popup, size=(150, 80), element_justification='c')
    elif type == 'relatorioLocacoes':
        relatoriosLocacoes_popup = \
            [
                [sg.Radio('Todos', group_id='locacoes_popup', default=True, key='todosNaoFinalizados'),
                 sg.Radio('Veiculos Nacionais', group_id='locacoes_popup', key='todosNaoFinalizadosNacionais'),
                 sg.Radio('Veiculos Importados', group_id='locacoes_popup', key='todosNaoFinalizadosImportados')],
                [sg.Button('Gerar'), sg.Button('Cancelar')]

            ]
        return sg.Window('Relatório de Locações', relatoriosLocacoes_popup, size=(150, 80), element_justification='c')


layout_Geral = [[sg.TabGroup([[
    sg.Tab('Locação', locacaoLayout),
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
        if values['todosVeiculos']:
            window['todosVeiculos'].update(value=locadora.ListarVeiculos())
        if values['CNHNecessaria']:
            popup_window = createWindow('relatorioVeiculos')

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
            popup_window = createWindow('relatorioClientes')

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
                    popup_window.hide()
    if event == 'btnlocacoes':
        if values['NaoFinalizadas']:
            popup_window = createWindow('relatorioLocacoes')

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
    if event == 'btncadFuncionario':
        popup_window = createWindow('cadastrarFuncionario')
        while True:
            popup_event, popup_values = popup_window.read()
            if popup_event in (sg.WINDOW_CLOSED, 'Cancelar'):
                break
            if popup_event == 'salvarFuncionario':
                if popup_values['nome'] != '' and popup_values['cpf'] != '' and popup_values['rg'] != '' and popup_values['dataNascimento'] != '' and popup_values['endereco'] != '' and popup_values['email'] != '' and popup_values['cep'] != '' and popup_values['salario'] != '' and popup_values['pis'] != '' and popup_values['dataAdmissao'] != '':
                    funcionario = Usuario.Funcionario(popup_values['nome'], popup_values['cpf'], popup_values['rg'], popup_values['dataNascimento'], popup_values['endereco'], popup_values['email'], popup_values['cep'], popup_values['salario'], popup_values['pis'], popup_values['dataAdmissao'])
                    Banco_de_dados.BancodeDados.criarFuncionario(funcionario)
                    # Salvar localmente
                else:
                    sg.popup_error("Todos os campos devem ser preenchidos!")

    if event == 'btncadCliente':
        popup_window = createWindow('cadastrarCliente')
        while True:
            popup_event, popup_values = popup_window.read()
            if popup_event in (sg.WINDOW_CLOSED, 'Cancelar'):
                break
            if popup_event == 'salvarCliente':
                if popup_values['nome'] != '' and popup_values['cpf'] != '' and popup_values['rg'] != '' and popup_values['dataNascimento'] != '' and popup_values['endereco'] != '' and popup_values['email'] != '' and popup_values['cep'] != '' and popup_values['categoriaCNH'] != '' and popup_values['numeroCNH'] != '' and popup_values['dataValidadeCNH'] != '' and popup_values['clienteOuro'] != '':
                    cliente = Usuario.Cliente(popup_values['nome'], popup_values['cpf'], popup_values['rg'], popup_values['dataNascimento'], popup_values['endereco'], popup_values['email'], popup_values['cep'], popup_values['categoriaCNH'], popup_values['numeroCNH'], popup_values['dataValidadeCNH'], popup_values['clienteOuro'])
                    Banco_de_dados.BancodeDados.criarCliente(cliente)
                    # Salvar localmente
                    pass
                else:
                    sg.popup_error("Todos os campos devem ser preenchidos!")
    if event == 'btnCadVeiculoNacional':
        popup_window = createWindow('cadastrarVeiculoNacional')
        while True:
            popup_event, popup_values = popup_window.read()
            if popup_event in (sg.WINDOW_CLOSED, 'Cancelar'):
                break
            if popup_event == 'salvarVeiculoNacional':
                if popup_values['nomeModelo'] != '' and popup_values['montadora'] != '' and popup_values['anoFabricacao'] != '' and popup_values['anoModelo'] != '' and popup_values['placa'] != '' and popup_values['categoria'] != '' and popup_values['valorFipe'] != '' and popup_values['valorDiaria'] != '' and popup_values['categoriaCNH'] != '' and popup_values['taxaImpostoEstadual'] != '':
                    veiculoNacional = Veiculos.VeiculoNacional(popup_values['nomeModelo'], popup_values['montadora'], popup_values['anoFabricacao'], popup_values['anoModelo'], popup_values['placa'], popup_values['categoria'], popup_values['valorFipe'], popup_values['valorDiaria'], popup_values['categoriaCNH'], popup_values['taxaImpostoEstadual'])
                    Banco_de_dados.BancodeDados.criarVeiculoNacional(veiculoNacional)
                    # Salvar localmente
                    pass
                else:
                    sg.popup_error("Todos os campos devem ser preenchidos!")
    if event == 'btnCadVeiculoImportado':
        popup_window = createWindow('cadastrarVeiculoImportado')
        while True:
            popup_event, popup_values = popup_window.read()
            if popup_event in (sg.WINDOW_CLOSED, 'Cancelar'):
                break
            if popup_event == 'salvarVeiculoImportado':
                if popup_values['nomeModelo'] != '' and popup_values['montadora'] != '' and popup_values['anoFabricacao'] != '' and popup_values['anoModelo'] != '' and popup_values['placa'] != '' and popup_values['categoria'] != '' and popup_values['valorFipe'] != '' and popup_values['valorDiaria'] != '' and popup_values['categoriaCNH'] != '' and popup_values['taxaImpostoEstadual'] != '' and popup_values['taxaImpostoFeredal'] != '':
                    veiculoImportado = Veiculos.VeiculoImportado(popup_values['nomeModelo'], popup_values['montadora'], popup_values['anoFabricacao'], popup_values['anoModelo'], popup_values['placa'], popup_values['categoria'], popup_values['valorFipe'], popup_values['valorDiaria'], popup_values['categoriaCNH'], popup_values['taxaImpostoEstadual'], popup_values['taxaImpostoFeredal'])
                    Banco_de_dados.BancodeDados.criarVeiculoImportado(veiculoImportado)
                    # Salvar localmente
                    pass
                else:
                    sg.popup_error("Todos os campos devem ser preenchidos!")
    if event == 'btnCadSeguro':
        popup_window = createWindow('cadastrarSeguro')
        while True:
            popup_event, popup_values = popup_window.read()
            if popup_event in (sg.WINDOW_CLOSED, 'Cancelar'):
                break
            if popup_event == 'salvarSeguro':
                if popup_values['nome'] != '' and popup_values['tipo'] != '' and popup_values['descricao'] != '' and popup_values['valor'] != '':
                    seguro = Locacoes.Seguro(popup_values['nome'], popup_values['tipo'], popup_values['descricao'], popup_values['valor'])
                    Banco_de_dados.BancodeDados.criarSeguro(seguro)
                    # Salvar localmente
                    pass
                else:
                    sg.popup_error("Todos os campos devem ser preenchidos!")
window.close()
