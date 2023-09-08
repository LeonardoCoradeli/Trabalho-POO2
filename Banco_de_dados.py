import requests
import json
import Locacoes
import Usuario


class BancodeDados:
    URLBanco = 'https://trabalho-pratico-c3891-default-rtdb.firebaseio.com/'
    URLTClientes = 'Clientes'
    URLTFuncionarios = 'Funcionarios'
    URLTabelaLocacoes = 'Locações'
    URLTVeiculosNacionais = 'Veiculos_nacionais'
    URLTVeiculosInternacionais = 'Veiculos_internacionais'
    URLTSeguros = 'Seguros'

    @staticmethod
    def criarFuncionario(funcionario):
        funcionario_dic = funcionario.__dict__
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{funcionario_dic['_codigoUsuario']}.json",data=json.dumps(funcionario_dic))

    @staticmethod
    def recuperarFuncionario(codFuncioanrio):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{codFuncioanrio}/.json")
        funcionario_dict = response.json()
        funcionario = Usuario.Funcionario('', '', '', '', '', '', '', 0, '', '')
        funcionario.__dict__.update(funcionario_dict)
        return funcionario


    @staticmethod
    def criarLocacao(locacao):
        locacao_dic = locacao.__dict__
        dataLocacao = locacao_dic["_dataLocacao"].strftime("%d/%m/%Y")
        dataDevolucao = locacao_dic["_dataDevolucao"].strftime("%d/%m/%Y")
        locacao_dic["_dataLocacao"] = dataLocacao
        locacao_dic["_dataDevolucao"] = dataDevolucao
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{locacao_dic['_codLocacao']}.json",data=json.dumps(locacao_dic))

    @staticmethod
    def recuperarLocacao(codLocacao):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{codLocacao}.json")
        locacao_dict = response.json()
        locacao = Locacoes.Locacao('', '', '1/1/2023', '1/1/2023', 0, '', '', '', 1)
        locacao.__dict__.update(locacao_dict)
        return locacao

    @staticmethod
    def criarCliente(cliente):
        cliente_dict = cliente.__dict__
        dataNascimento = cliente_dict["_dataNascimento"].strftime("%d/%m/%Y")
        dataVencimentoCNH = cliente_dict["_validadeCNH"].strftime("%d/%m/%Y")
        cliente_dict["_dataNascimento"] = dataNascimento
        cliente_dict["_validadeCNH"] = dataVencimentoCNH
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{cliente_dict['_codigoUsuario']}.json",
                     data=json.dumps(cliente_dict))

    @staticmethod
    def recuperarCliente(codCliente):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{codCliente}/.json")
        funcionario_dict = response.json()
        funcionario = Usuario.Cliente('','','','1/1/2023','','','','','','1/1/2023',False,1)
        funcionario.__dict__.update(funcionario_dict)
        return funcionario