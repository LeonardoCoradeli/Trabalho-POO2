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
    
    def ListarFuncionarioDoMes(self,mes):
        locacoes_por_funcionario = {}
        for i in self._locacoes:
            if i.dataLocacao.month == mes:
                funcionario = i.funcionario
                valor_locacao = i.valorLocacao


                if funcionario in locacoes_por_funcionario:
                    locacoes_por_funcionario[funcionario] += valor_locacao
                else:
                    locacoes_por_funcionario[funcionario] = valor_locacao

        funcionario_do_mes = max(locacoes_por_funcionario, key=locacoes_por_funcionario.get)
        valor_mais_alto = locacoes_por_funcionario[funcionario_do_mes]

        return f'O funcionário do mês é: {funcionario_do_mes} faturando: {valor_mais_alto}'

    def ListarClientes(self):
        for i in self._clientes:
            str(i)
    def ListarHistoricoLocacaoCliente(self,cliente):
        for i in self._locacoes:
            if i.getCliente() == cliente:
                str(i)
    def ListarTodasLocacoes(self):
        for i in self._locacoes:
            str(i)
    def ListarLocacaoMes(self,mes):
        for i in self._locacoes:
            if i.getMes() == mes:
                str(i)
    def ListarLocacaoMescomLucro(self,mes):
        valor = 0.0
        for i in self._locacoes:
            if i.getMes() == mes:
                valor += i.valorTotal()
        return f'Lucro do mês {mes}: {str(valor)}'

    def ListarLocacoesFinalizadas(self):
        for i in self._locacoes:
            if i.getFinalizada() == True:
                str(i)
    def ListarLocacoesNaoFinalizadas(self):
        locacoes = []
        for i in self._locacoes:
            if i.getFinalizada() == False:
                locacoes.append(str(locacoes))
        return ''.join(locacoes)

    def ListarLocacoesNaoFinalizadasNacional(self):
        locacoes = []
        for i in self._locacoes:
            if i.getFinalizada() == False and i.getVeiculo().getTipo() == "Nacional":
                locacoes.append(str(i))
        return ''.join(locacoes)
    def ListarLocacoesNaoFinalizadasImportado(self):
        locacoes = []
        for i in self._locacoes:
            if i.getFinalizada() == False and i.getVeiculo().getTipo() == "Importado":
                locacoes.append(str(i))
        return ''.join(locacoes)
    def ListarLocacoesAtrasadas(self):
        locacoes =[]
        for i in self._locacoes:
            if i.getAtrasado() == True:
                locacoes.append(str(i))
        return ''.join(locacoes)

    def ListarTiposSeguros(self):
        seguros = []
        for i in self._seguros:
            seguros.append(str(i))
        return ''.join(seguros)
    def RetornarVeiculoscomoObjeto(self):
        return self._veiculos

