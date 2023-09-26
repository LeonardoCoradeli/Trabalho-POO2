import Banco_de_dados
import Usuario
import Locacoes
import Usuario
import Veiculos
class Locadora:
    def __init__(self,nome,endereco,website,redeSocial):
        self._nome = nome
        self._endereco = endereco
        self._website = website
        self._redeSocial = redeSocial
        self._conifguracao = Banco_de_dados.BancodeDados()
        self._locacoes = self._conifguracao.recuperarTodasLocacoes()
        self._clientes = self._conifguracao.recuperarTodosClientes()
        self._funcionarios = self._conifguracao.recuperarTodosFuncionarios()
        self._seguros = self._conifguracao.recuperarTodosSeguros()
        self._veiculos = self._conifguracao.recuperarTodosVeiculosNacionais()+self._conifguracao.recuperarTodosVeiculosImportados()



