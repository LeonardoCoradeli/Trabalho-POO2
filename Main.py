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
layout_TelaCadastro = \
[
                    [sg.Column(layout=[
                            [sg.Button('Funcionario', size=(15, 1),key='btncadFuncionario',font=('Verdana', 15))],
                            [sg.Text('',size=(15,1))],
                            [sg.Button('Cliente', size=(15, 1),key='btncadCliente',font=('Verdana', 15))],
                            [sg.Text('',size=(15,1))],
                            [sg.Button('Veiculo Nacional', size=(15, 1), key='btnCadVeiculoNacional',font=('Verdana', 15))],
                            [sg.Text('',size=(15,1))],
                            [sg.Button('Veiculo Importado', size=(15, 1), key='btnCadVeiculoImportado',font=('Verdana', 15))],
                            [sg.Text('',size=(15,1))],
                            [sg.Button('Seguro', size=(15, 1),key='btnCadSeguro',font=('Verdana', 15))]
                    ]),
                    sg.Frame('',layout=[[]],size=(450, 500),key='lugarAparacerCadastro')]
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


layout_TelaSobre = [
    [sg.Text('',size=(10,15))],
    [sg.Frame('', layout=[
        [sg.Column(layout=[
            [sg.Text('Nome: ',font=('Verdana',16,'bold')),sg.Text(f'{locadora.nome}',font=('Verdana',16))],
            [sg.Text('Endereço: ',font=('Verdana',16,'bold')),sg.Text(f'{locadora.endereco}',font=('Verdana',16))]
        ]),
        sg.Column(layout=[
            [sg.Text('Website: ',font=('Verdana',16,'bold')),sg.Text(f'{locadora.website}',font=('Verdana',16))],
            [sg.Text('Rede Social: ',font=('Verdana',16,'bold')),sg.Text(f'{locadora.redeSocial}',font=('Verdana',16))]
    ])]])]]

layoutvazio = [[]]



layout_TelaBusca = []
def createWindow(type):
    frame_element = window.Element('lugarAparacerCadastro')
    frame_size = frame_element.Widget.winfo_reqwidth()-15, frame_element.Widget.winfo_reqheight()-15
    popup_location = (125,0)


    if type == 'cadastrarFuncionario':
        cadastroFuncionario = \
            [
                [sg.Column(layout=[
                    [sg.Text('Nome:',font=('Verdana',10,'bold'))],
                    [sg.Text('CPF:',font=('Verdana',10,'bold'))],
                    [sg.Text('RG:',font=('Verdana',10,'bold'))],
                    [sg.Text('Data de Nascimento:',font=('Verdana',10,'bold'))],
                    [sg.Text('Endereço:',font=('Verdana',10,'bold'))],
                    [sg.Text('E-mail:',font=('Verdana',10,'bold'))],
                    [sg.Text('CEP:',font=('Verdana',10,'bold'))],
                    [sg.Text('Salario:',font=('Verdana',10,'bold'))],
                    [sg.Text('Pis:',font=('Verdana',10,'bold'))],
                    [sg.Text('Data de Admissão:',font=('Verdana',10,'bold'))],
                ],element_justification='l'),
                sg.Column(layout=[
                    [sg.InputText(size=(20, 1), key='nome')],
                    [sg.InputText(size=(20, 1), key='cpf')],
                    [sg.InputText(size=(20, 1), key='rg')],
                    [sg.InputText(size=(20, 1), key='dataNascimento')],
                    [sg.InputText(size=(20, 1), key='endereco')],
                    [sg.InputText(size=(20, 1), key='email')],
                    [sg.InputText(size=(20, 1), key='cep')],
                    [sg.InputText(size=(20, 1), key='salario')],
                    [sg.InputText(size=(20, 1), key='pis')],
                    [sg.InputText(size=(20, 1), key='dataAdmissao')]
                ],element_justification='l')],
                [sg.Text('Não é possivel fechar o programa enquanto cadastra!', text_color='red')],
                [sg.Button('Salvar', key='salvarFuncionario', size=(15, 1)),sg.Button('Cancelar', key='cancelar', size=(15, 1))],
            ]
        return sg.Window('Cadastro de Funcionário',cadastroFuncionario,finalize=True, size=frame_size, relative_location=popup_location, element_justification='c',no_titlebar=True,grab_anywhere=False,modal=True)
    elif type == 'cadastrarCliente':
        cadastroCliente = \
            [
                [sg.Column(layout=[
                    [sg.Text('Nome:',font=('Verdana',10,'bold'))],
                    [sg.Text('CPF:',font=('Verdana',10,'bold'))],
                    [sg.Text('RG:',font=('Verdana',10,'bold'))],
                    [sg.Text('Data de Nascimento:',font=('Verdana',10,'bold'))],
                    [sg.Text('Endereço:',font=('Verdana',10,'bold'))],
                    [sg.Text('E-mail:',font=('Verdana',10,'bold'))],
                    [sg.Text('CEP:',font=('Verdana',10,'bold'))],
                    [sg.Text('Categoria da CNH:',font=('Verdana',10,'bold'))],
                    [sg.Text('Número da CNH:',font=('Verdana',10,'bold'))],
                    [sg.Text('Data de Validade da CNH:',font=('Verdana',10,'bold'))],
                    [sg.Text('Cliente Ouro:',font=('Verdana',10,'bold'))],
                ],element_justification='l'),
                sg.Column(layout=[
                    [sg.InputText(size=(20, 1), key='nome')],
                    [sg.InputText(size=(20, 1), key='cpf')],
                    [sg.InputText(size=(20, 1), key='rg')],
                    [sg.InputText(size=(20, 1), key='dataNascimento')],
                    [sg.InputText(size=(20, 1), key='endereco')],
                    [sg.InputText(size=(20, 1), key='email')],
                    [sg.InputText(size=(20, 1), key='cep')],
                    [sg.InputText(size=(20, 1), key='categoriaCNH')],
                    [sg.InputText(size=(20, 1), key='numeroCNH')],
                    [sg.InputText(size=(20, 1), key='dataValidadeCNH')],
                    [sg.InputText(size=(20, 1), key='clienteOuro')]
                ],element_justification='l')],
                [sg.Text('Não é possivel fechar o programa enquanto cadastra!', text_color='red')],
                [sg.Button('Salvar', key='salvarCliente', size=(20, 1)),sg.Button('Cancelar', key='cancelar', size=(15, 1))],
            ]
        return sg.Window('Cadastro de Cliente', cadastroCliente,finalize=True, size=frame_size, relative_location=popup_location, element_justification='c',no_titlebar=True,grab_anywhere=False,modal=True)
    elif type == 'cadastrarVeiculoNacional':
        cadastroVeiculoNacional = \
            [
                [sg.Column(layout=[
                    [sg.Text('Nome do Modelo:',font=('Verdana',10,'bold'))],
                    [sg.Text('Montadora:',font=('Verdana',10,'bold'))],
                    [sg.Text('Ano de Fabricação:',font=('Verdana',10,'bold'))],
                    [sg.Text('Ano do Modelo:',font=('Verdana',10,'bold'))],
                    [sg.Text('Placa:',font=('Verdana',10,'bold'))],
                    [sg.Text('Categoria:',font=('Verdana',10,'bold'))],
                    [sg.Text('Valor Fipe:',font=('Verdana',10,'bold'))],
                    [sg.Text('Valor da Diária:',font=('Verdana',10,'bold'))],
                    [sg.Text('Categoria da CNH:',font=('Verdana',10,'bold'))],
                    [sg.Text('Taxa do Imposto Estadual:',font=('Verdana',10,'bold'))],
                ],element_justification='l'),
                sg.Column(layout=[
                    [sg.InputText(size=(20, 1), key='nomeModelo')],
                    [sg.InputText(size=(20, 1), key='montadora')],
                    [sg.InputText(size=(20, 1), key='anoFabricacao')],
                    [sg.InputText(size=(20, 1), key='anoModelo')],
                    [sg.InputText(size=(20, 1), key='placa')],
                    [sg.InputText(size=(20, 1), key='categoria')],
                    [sg.InputText(size=(20, 1), key='valorFipe')],
                    [sg.InputText(size=(20, 1), key='valorDiaria')],
                    [sg.Combo(['A','B','C','D','E'],size=(20, 1), key='categoriaCNH')],
                    [sg.InputText(size=(20, 1), key='taxaImpostoEstadual')]
                ],element_justification='l')],
                [sg.Text('Não é possivel fechar o programa enquanto cadastra!', text_color='red')],
                [sg.Button('Salvar', key='salvarVeiculoNacional', size=(20, 1)),sg.Button('Cancelar', key='cancelar', size=(15, 1))],
            ]
        return sg.Window('Cadastro de Veiculo Nacional', cadastroVeiculoNacional, finalize=True, size=frame_size, relative_location=popup_location, element_justification='c',no_titlebar=True,grab_anywhere=False,modal=True)
    elif type == 'cadastrarVeiculoImportado':
        cadastroVeiculoImportado = \
            [
                [sg.Column(layout=[
                    [sg.Text('Nome do Modelo:',font=('Verdana',10,'bold'))],
                    [sg.Text('Montadora:',font=('Verdana',10,'bold'))],
                    [sg.Text('Ano de Fabricação:',font=('Verdana',10,'bold'))],
                    [sg.Text('Ano do Modelo:',font=('Verdana',10,'bold'))],
                    [sg.Text('Placa:',font=('Verdana',10,'bold'))],
                    [sg.Text('Categoria:',font=('Verdana',10,'bold'))],
                    [sg.Text('Valor Fipe:',font=('Verdana',10,'bold'))],
                    [sg.Text('Valor da Diária:',font=('Verdana',10,'bold'))],
                ],element_justification='l'),
                sg.Column(layout=[
                    [sg.InputText(size=(20, 1), key='nomeModelo')],
                    [sg.InputText(size=(20, 1), key='montadora')],
                    [sg.InputText(size=(20, 1), key='anoFabricacao')],
                    [sg.InputText(size=(20, 1), key='anoModelo')],
                    [sg.InputText(size=(20, 1), key='placa')],
                    [sg.InputText(size=(20, 1), key='categoria')],
                    [sg.InputText(size=(20, 1), key='valorFipe')],
                    [sg.InputText(size=(20, 1), key='valorDiaria')]
                ],element_justification='l')],
                [sg.Text('Não é possivel fechar o programa enquanto cadastra!', text_color='red')],
                [sg.Button('Salvar', key='salvarVeiculoImportado', size=(20, 1)),sg.Button('Cancelar', key='cancelar', size=(15, 1))],
            ]
        return sg.Window('Cadastro de Veiculo Importado', cadastroVeiculoImportado, finalize=True, size=frame_size, relative_location=popup_location, element_justification='c',no_titlebar=True,grab_anywhere=False,modal=True)
    elif type == 'cadastrarSeguro':
        cadastroSeguro = \
            [
                [sg.Column(layout=[
                    [sg.Text('Nome:',font=('Verdana',10,'bold'))],
                    [sg.Text('Tipo:',font=('Verdana',10,'bold'))],
                    [sg.Text('Descrição:',font=('Verdana',10,'bold'))],
                    [sg.Text('Valor:',font=('Verdana',10,'bold'))]
                ],element_justification='l'),
                sg.Column(layout=[
                    [sg.InputText(size=(20, 1), key='nome')],
                    [sg.InputText(size=(20, 1), key='tipo')],
                    [sg.InputText(size=(20, 1), key='descricao')],
                    [sg.InputText(size=(20, 1), key='valor')]
                ])],
                [sg.Text('Não é possivel fechar o programa enquanto cadastra!', text_color='red')],
                [sg.Button('Salvar', key='salvarSeguro', size=(20, 1)),sg.Button('Cancelar', key='cancelar', size=(15, 1))],
            ]
        return sg.Window('Cadastro de Seguro', cadastroSeguro, finalize=True, size=frame_size, relative_location=popup_location, element_justification='c',no_titlebar=True,grab_anywhere=False,modal=True)
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

buscaVeiculos = \
[
                        sg.Frame('Veiculos', layout=[
                        [sg.Radio('Todos', group_id='veiculos', default=True, key='todosVeiculos'),
                         sg.Radio('Nacionais', group_id='veiculos'), sg.Radio('Importados', group_id='veiculos')],
                        [sg.Radio('Disponivel', group_id='veiculos'), sg.Radio('Locado', group_id='veiculos'),
                         sg.Radio('Devolução atrasada', group_id='veiculos')],
                        [sg.Radio('CNH Necessaria', group_id='veiculos', key='CNHNecessaria')],
                        [sg.Button('Gerar', key='btnveiculos')]], vertical_alignment='c', key='frameVeiculos', size=(330, 150))

]


buscaClientes = \
[
                        sg.Frame('Clientes', layout=[
                        [sg.Radio('Todos', group_id='clientes', default=True, key='todosClientes'),
                         sg.Radio('Locações com atraso', group_id='clientes')],
                        [sg.Radio('Veiculo Especifico', group_id='clientes', key='clienteVeiculoAtrasado')],
                        [sg.Button('Gerar', key='btnclientes')]], size=(330, 120))
]
# mudar esses input para combo com respectivos dados

buscaLocacoes = \
[
                        sg.Frame('Locações', layout=[
                        [sg.Radio('Todos', group_id='locacoes', default=True, key='todosLocacoes'),
                         sg.Radio('Finalizadas', group_id='locacoes'), sg.Radio('Atrasadas', group_id='locacoes')],
                        [sg.Radio('Cliente especifico', group_id='locacoes'), sg.Radio('Mês especifico', group_id='locacoes')],
                        [sg.Radio('Não finalizadas', group_id='locacoes', key='NaoFinalizadas')],
                        [sg.Button('Gerar', key='btnlocacoes')]], size=(330, 150))
]

buscaFuncionarios = \
[
                        sg.Frame('Funcionarios', layout=[
                        [sg.Radio('Todos', group_id='funcionarios', default=True, key='todosfuncionarios'),
                         sg.Radio('Funcionario do mês', group_id='funcionarios', key='funcionarioMes')],
                        [sg.Button('Gerar', key='btnFuncionario')]], size=(330, 100))
]

layout_TelaBusca = [
    [sg.Column(layout=[relatoriosVeiculos, relatoriosClientes, relatoriosLocacoes, relatorioFuncionarios]),
     sg.Column(layout=[[sg.Multiline(size=(350, 450), disabled=True, key='textoBusca')]])]
]

layout_Geral = [[sg.TabGroup([[
    sg.Tab('Locação', locacaoLayout),
    sg.Tab('Relatórios', layout_TelaRelatorios),
    sg.Tab('Busca', layoutvazio),
    sg.Tab('Cadastro', layout_TelaCadastro,tooltip='Cadastro no sistema', element_justification='c'),
    sg.Tab('Sobre', layout_TelaSobre, tooltip='Sobre o sistema', element_justification='c')
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
            if popup_event == 'cancelar':
                popup_window.close()
                break
            if popup_event == 'salvarFuncionario':
                if popup_values['nome'] != '' and popup_values['cpf'] != '' and popup_values['rg'] != '' and popup_values['dataNascimento'] != '' and popup_values['endereco'] != '' and popup_values['email'] != '' and popup_values['cep'] != '' and popup_values['salario'] != '' and popup_values['pis'] != '' and popup_values['dataAdmissao'] != '':
                    funcionario = Usuario.Funcionario(popup_values['nome'], popup_values['cpf'], popup_values['rg'], popup_values['dataNascimento'], popup_values['endereco'], popup_values['email'], popup_values['cep'], popup_values['salario'], popup_values['pis'], popup_values['dataAdmissao'])
                    Banco_de_dados.BancodeDados.criarFuncionario(funcionario)
                     #Salvar localmente
                else:
                    sg.popup_error("Todos os campos devem ser preenchidos!")

    if event == 'btncadCliente':
        popup_window = createWindow('cadastrarCliente')
        while True:
            popup_event, popup_values = popup_window.read()
            if popup_event == 'cancelar':
                popup_window.close()
                break
            if popup_event == 'salvarCliente':
                if popup_values['nome'] != '' and popup_values['cpf'] != '' and popup_values['rg'] != '' and popup_values['dataNascimento'] != '' and popup_values['endereco'] != '' and popup_values['email'] != '' and popup_values['cep'] != '' and popup_values['categoriaCNH'] != '' and popup_values['numeroCNH'] != '' and popup_values['dataValidadeCNH'] != '' and popup_values['clienteOuro'] != '':
                    cliente = Usuario.Cliente(popup_values['nome'], popup_values['cpf'], popup_values['rg'], popup_values['dataNascimento'], popup_values['endereco'], popup_values['email'], popup_values['cep'], popup_values['categoriaCNH'], popup_values['numeroCNH'], popup_values['dataValidadeCNH'], popup_values['clienteOuro'])
                    locadora.configuracao.criarCliente(cliente)
                    # Salvar localmente
                    pass
                else:
                    sg.popup_error("Todos os campos devem ser preenchidos!")
    if event == 'btnCadVeiculoNacional':
        popup_window = createWindow('cadastrarVeiculoNacional')
        while True:
            popup_event, popup_values = popup_window.read()
            if popup_event == 'cancelar':
                popup_window.close()
                break
            if popup_event == 'salvarVeiculoNacional':

                if popup_values['nomeModelo'] != '' and popup_values['montadora'] != '' and popup_values['anoFabricacao'] != '' and popup_values['anoModelo'] != '' and popup_values['placa'] != '' and popup_values['categoria'] != '' and popup_values['valorFipe'] != '' and popup_values['valorDiaria'] != '' and popup_values['categoriaCNH'] != '' and popup_values['taxaImpostoEstadual'] != '':
                    veiculoNacional = Veiculos.VeiculoNacional(popup_values['nomeModelo'], popup_values['montadora'], popup_values['anoFabricacao'], popup_values['anoModelo'], popup_values['placa'], popup_values['categoria'], popup_values['valorFipe'], popup_values['valorDiaria'], popup_values['categoriaCNH'], popup_values['taxaImpostoEstadual'])
                    locadora.configuracao.criarVeiculoNacional(veiculoNacional)
                    locadora.veiculos(veiculoNacional)
                    # Salvar localmente
                    pass
                else:
                    sg.popup_error("Todos os campos devem ser preenchidos!")
    if event == 'btnCadVeiculoImportado':
        popup_window = createWindow('cadastrarVeiculoImportado')
        while True:
            popup_event, popup_values = popup_window.read()
            if popup_event == 'cancelar':
                popup_window.close()
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
            if popup_event == 'cancelar':
                popup_window.close()
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
