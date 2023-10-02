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
        self._veiculos = self._conifguracao.recuperarTodosVeiculosNacionais()
        self._veiculos.extend(self._conifguracao.recuperarTodosVeiculosImportados())

    def ListarVeiculos(self):
        for i in self._veiculos:
            i.__str__()
    
    def ListarVeiculosNacionais(self):
        for i in self._veiculos:
            if i.getTipo() == "Nacional":
                i.__str__()
    
    def ListaVeiculosImportados(self):
        for i in self._veiculos:
            if i.getTipo() == "Importado":
                i.__str__()
    
    def ListasVeiulosDisponiveis(self):
        for i in self._veiculos:
            if i.getDisponivel() == True:
                i.__str__()
    
    def ListarVeiculosDisponiveisCategoria(self,categoria):
        for i in self._veiculos:
            if i.getDisponivel() == True and i.getCategoria() == categoria:
                i.__str__()
    
    def ListarVeiculosNãoDisponiveis(self):
        for i in self._veiculos:
            if i.getDisponivel() == False:
                i.__str__()
    
    def ListarVeiculosAtrasados(self):
        for i in self._locacoes:
            if i.getAtrasado() == True:
                i.__str__()
    def ListarClientesComLocacao(self):
        for i in self._locacoes:
            i.getCliente().__str__
    
    def ListarFuncionarios(self):
        for i in self._funcionarios:
            i.__str__
    
    def ListarFuncionarioDoMes(self):
        for i in self._funcionarios:
            if i.getFuncionarioDoMes() == True:
                i.__str__()
    def ListarClientes(self):
        for i in self._clientes:
            i.__str__()
    def ListarHistoricoLocacaoCliente(self,cliente):
        for i in self._locacoes:
            if i.getCliente() == cliente:
                i.__str__()
    def ListarTodasLocacoes(self):
        for i in self._locacoes:
            i.__str__()
    def ListarLocacaoMes(self,mes):
        for i in self._locacoes:
            if i.getMes() == mes:
                i.__str__()
    def ListarLocacaoMescomLucro(self,mes):
        for i in self._locacoes:
            if i.getMes() == mes:
                i.getLucro().__str__

    def ListarLocacoesFinalizadas(self):
        for i in self._locacoes:
            if i.getFinalizada() == True:
                i.__str__()
    def ListarLocacoesNaoFinalizadas(self):
        for i in self._locacoes:
            if i.getFinalizada() == False:
                i.__str__()
    def ListarLocacoesNaoFinalizadasNacional(self):
        for i in self._locacoes:
            if i.getFinalizada() == False and i.getVeiculo().getTipo() == "Nacional":
                i.__str__()
    def ListarLocacoesNaoFinalizadasImportado(self):
        for i in self._locacoes:
            if i.getFinalizada() == False and i.getVeiculo().getTipo() == "Importado":
                i.__str__()
    def ListarLocacoesAtrasadas(self):
        for i in self._locacoes:
            if i.getAtrasado() == True:
                i.__str__()
    def ListarTiposSeguros(self):
        for i in self._seguros:
            i.__str__()
    def RetornarVeiculoscomoObjeto(self):
        return self._veiculos

