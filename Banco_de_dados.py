import requests
import json

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
        response = requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{funcionario_dic['_codigoUsuario']}.json",data=json.dumps(funcionario_dic))
        if response.status_code == 200:
            print("Enviado com sucesso!\n")
        else:
            print("Não enviado!\n")

    @staticmethod
    def recuperarFuncionario(codigoUsuario):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{codigoUsuario}.json")

        if response.status_code == 200:
            data = response.json()
            if data:
                print(data)
            else:
                print("Funcionário não encontrado no banco de dados.")
        else:
            print("Erro ao recuperar informações do funcionário.")

    @staticmethod
    def criarLocacao(locacao):
        locacao_dic = locacao.__dict__
        dataLocacao = locacao_dic["_dataLocacao"].strftime("%d/%m/%Y")
        dataDevolucao = locacao_dic["_dataDevolucao"].strftime("%d/%m/%Y")
        locacao_dic["_dataLocacao"] = dataLocacao
        locacao_dic["_dataDevolucao"] = dataDevolucao
        response = requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{locacao_dic['_codLocacao']}.json",data=json.dumps(locacao_dic))
        if response.status_code == 200:
            print("Enviado com sucesso")
        else:
            print("Não foi possível enviar")


    @staticmethod
    def recuperarLocacao(codLocacao):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{codLocacao}.json")


        if response.status_code == 200:
            data = response.json()
            if data:
                print(data)
            else:
                print("Locacao não encontrada no banco de dados.")
        else:
            print("Erro ao recuperar informações da locacao.")