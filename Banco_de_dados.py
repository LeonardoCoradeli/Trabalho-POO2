import requests
import json
import Locacoes
import Usuario
import Veiculos


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
        locacao_dict = locacao.__dict__
        dataLocacao = locacao_dict["_dataLocacao"].strftime("%d/%m/%Y")
        dataDevolucao = locacao_dict["_dataDevolucao"].strftime("%d/%m/%Y")
        locacao_dict["_dataLocacao"] = dataLocacao
        locacao_dict["_dataDevolucao"] = dataDevolucao
        listaSeguros = locacao_dict['_seguros']
        locacao_dict['_seguros'] = [c.__dict__ for c in listaSeguros]
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{locacao_dict['_codLocacao']}.json",data=json.dumps(locacao_dict))

    @staticmethod
    def recuperarLocacao(codLocacao):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{codLocacao}.json")
        locacao_dict = response.json()
        if locacao_dict['_seguros'] != None:
            listaSeguros = locacao_dict['_seguros']
            seguros = []
            for c in listaSeguros:
                seguro = Locacoes.Seguro('', '', '', 0)
                seguro.__dict__.update(c)
                seguros.append(seguro)
            locacao_dict['_seguros'] = seguros
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
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTClientes}/{codCliente}/.json")
        funcionario_dict = response.json()
        funcionario = Usuario.Cliente('','','','1/1/2023','','','','','','1/1/2023',False,1)
        funcionario.__dict__.update(funcionario_dict)
        return funcionario

    @staticmethod
    def criarVeiculoNacional(veiculo):
        veiculo_dict = veiculo.__dict__
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosNacionais}/{veiculo_dict['_codigoVeiculo']}.json",
                         data=json.dumps(veiculo_dict))

    @staticmethod
    def recuperarVeiculoNacional(codVeiculo):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosNacionais}/{codVeiculo}/.json")
        veiculo_dict = response.json()
        veiculo = Veiculos.VeiculoNacional('','',0,0,'','',0,0,'',False,0,0)
        veiculo.__dict__.update(veiculo_dict)
        return veiculo

    @staticmethod
    def criarVeiculoImportado(veiculo):
        veiculo_dict = veiculo.__dict__
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosInternacionais}/{veiculo_dict['_codigoVeiculo']}.json",
                     data=json.dumps(veiculo_dict))

    @staticmethod
    def recuperarVeiculoImportado(codVeiculo):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosInternacionais}/{codVeiculo}/.json")
        veiculo_dict = response.json()
        veiculo = Veiculos.VeiculoImportado('','',0,0,'','',0,0,'',False,0,0,0)
        veiculo.__dict__.update(veiculo_dict)
        return veiculo

    @staticmethod
    def criarSeguro(seguro):
        seguro_dict = seguro.__dict__
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{seguro_dict['_codigoSeguro']}/.json")

    @staticmethod
    def recuperarSeguro(codSeguro):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{codSeguro}/.json")
        seguro_dict = response.json()
        seguro = Locacoes.Seguro('','','',0,0)
        seguro.__dict__.update(seguro_dict)
        return seguro