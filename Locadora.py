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

    def ListarVeiculos(self):
        for i in self._veiculos:
            print(i)
    
    def ListarVeiculosNacionais(self):
        for i in self._veiculos:
            if i.getTipo() == "Nacional":
                print(i)
    
    def ListaVeiculosImportados(self):
        for i in self._veiculos:
            if i.getTipo() == "Importado":
                print(i)
    
    def ListasVeiulosDisponiveis(self):
        for i in self._veiculos:
            if i.getDisponivel() == True:
                print(i)
    
    def ListarVeiculosDisponiveisCategoria(self,categoria):
        for i in self._veiculos:
            if i.getDisponivel() == True and i.getCategoria() == categoria:
                print(i)
    
    def ListarVeiculosNãoDisponiveis(self):
        for i in self._veiculos:
            if i.getDisponivel() == False:
                print(i)
    
    def ListarVeiculosAtrasados(self):
        for i in self._locacoes:
            if i.getAtrasado() == True:
                print(i)
    
    def ListarClientesComLocacao(self):
        for i in self._locacoes:
            print(i.getCliente())
    
    def ListarFuncionarios(self):
        for i in self._funcionarios:
            print(i)
    
    def ListarFuncionarioDoMes(self):
        for i in self._funcionarios:
            if i.getFuncionarioDoMes() == True:
                print(i)
    
    def ListarClientes(self):
        for i in self._clientes:
            print(i)
    
    def ListarHistoricoLocacaoCliente(self,cliente):
        for i in self._locacoes:
            if i.getCliente() == cliente:
                print(i)
    
    def ListarTodasLocacoes(self):
        for i in self._locacoes:
            print(i)
    
    def ListarLocacaoMes(self,mes):
        for i in self._locacoes:
            if i.getMes() == mes:
                print(i)

    def ListarLocacaoMescomLucro(self,mes):
        for i in self._locacoes:
            if i.getMes() == mes:
                print(i.getLucro())
    
    def ListarLocacoesFinalizadas(self):
        for i in self._locacoes:
            if i.getFinalizada() == True:
                print(i)
    
    def ListarLocacoesNaoFinalizadas(self):
        for i in self._locacoes:
            if i.getFinalizada() == False:
                print(i)
    
    def ListarLocacoesNaoFinalizadasNacional(self):
        for i in self._locacoes:
            if i.getFinalizada() == False and i.getVeiculo().getTipo() == "Nacional":
                print(i)
    
    def ListarLocacoesNaoFinalizadasImportado(self):
        for i in self._locacoes:
            if i.getFinalizada() == False and i.getVeiculo().getTipo() == "Importado":
                print(i)

    def ListarLocacoesAtrasadas(self):
        for i in self._locacoes:
            if i.getAtrasado() == True:
                print(i)
    
    def ListarTiposSeguros(self):
        for i in self._seguros:
            print(i)
    
    def RetornarVeiculoscomoObjeto(self):
        return self._veiculos


