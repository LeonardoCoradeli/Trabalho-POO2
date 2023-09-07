import requests
import json
from Usuario import Funcionario
#import firebase_admin
#from firebase_admin import credentials

#caminho = r'C:\Users\Hmmm1\Documents\GitHub\Trabalho-POO2\trabalho-pratico-c3891-firebase-adminsdk-9byvx-9a726626f4.json'
#cred = credentials.Certificate(caminho)
#firebase_admin.initialize_app(cred)


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
        response = requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{funcionario_dic['_codigoUsuario']}.json",
                                data=json.dumps(funcionario_dic))
        if response.status_code == 200:
            print("Enviado com sucesso!\n")
        else:
            print("Não enviado!\n")

    @staticmethod
    def pegarFuncionario(id):
        response = requests.get(
            f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{id}/.json")
        if response.status_code == 200:
            print("Recebido com sucesso!\n")
        else:
            print("Não recebido!\n")
        funcionario_dict = response.json()
        funcionario = Funcionario('','','','','','','',0,'','',0)
        funcionario.__dict__.update(funcionario_dict)
        return funcionario