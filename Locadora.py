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
        self._configuracao = Banco_de_dados.BancodeDados()
        self._locacoes = self._configuracao.recuperarTodasLocacoes()
        self._clientes = self._configuracao.recuperarTodosClientes()
        self._funcionarios = self._configuracao.recuperarTodosFuncionarios()
        self._seguros = self._configuracao.recuperarTodosSeguros()
        self._veiculos = self._configuracao.recuperarTodosVeiculosNacionais()
        self._veiculos.extend(self._configuracao.recuperarTodosVeiculosImportados())

    #getter e setters
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self,endereco):
        self._endereco = endereco

    @property
    def website(self):
        return self._website

    @website.setter
    def website(self,website):
        self._website = website

    @property
    def redeSocial(self):
        return self._redeSocial

    @redeSocial.setter
    def redeSocial(self,redeSocial):
        self._redeSocial = redeSocial

    @property
    def configuracao(self):
        return self._configuracao

    @property
    def locacoes(self):
        return self._locacoes

    @locacoes.setter
    def locacoes(self,locacao):
        self._locacoes.append(locacao)

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self,cliente):
        self._clientes.append(cliente)

    @property
    def funcionarios(self):
        return self._funcionarios

    @funcionarios.setter
    def funcionarios(self,funcionario):
        self._funcionarios.append(funcionario)

    @property
    def seguros(self):
        return self._seguros

    @seguros.setter
    def seguros(self,seguro):
        self._seguros.append(seguro)

    @property
    def veiculos(self):
        return self._veiculos

    @veiculos.setter
    def veiculos(self,veiculo):
        self._veiculos.append(veiculo)
    
    def ListarVeiculos(self):
        veiculos = []
        for i in self._veiculos:
            veiculos.append(str(i))
        return ''.join(veiculos)

    
    def ListarVeiculosNacionais(self):
        veiculos = []
        for i in self._veiculos:
            if i.getTipo() == "Nacional":
                veiculos.append(str(i))
        return ''.join(veiculos)
    
    def ListaVeiculosImportados(self):
        veiculos = []
        for i in self._veiculos:
            if i.getTipo() == "Importado":
                veiculos.append(str(i))
        return ''.join(veiculos)
    
    def ListasVeiulosDisponiveis(self):
        veiculos = []
        for i in self._veiculos:
            if i.getDisponivel() == True:
                veiculos.append(str(i))
        return ''.join(veiculos)
    
    def ListarVeiculosDisponiveisCategoria(self,categoria):
        veiculos = []
        for i in self._veiculos:
            if i.getDisponivel() == True and i.getCategoria() == categoria:
                veiculos.append(str(i))
        return ''.join(veiculos)
    
    def ListarVeiculosNãoDisponiveis(self):
        veiculos = []
        for i in self._veiculos:
            if i.getDisponivel() == False:
                veiculos.append(str(i))
        return ''.join(veiculos)
    
    def ListarVeiculosAtrasados(self):
        veiculos = []
        for i in self._locacoes:
            if i.getAtrasado() == True:
                veiculos.append(str(i))
        return ''.join(veiculos)
    def ListarClientesComLocacao(self):
        for i in self._locacoes:
            i.getCliente().__str__
    
    def ListarFuncionarios(self):
        funcionarios = []
        for i in self._funcionarios:
            funcionarios.append(str(i))
        return ''.join(funcionarios)
    
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
        locacoes = []
        for i in self._clientes:
            locacoes.append(str(i))
        return ''.join(locacoes)
    def ListarHistoricoLocacaoCliente(self,cliente):
        locacoes = []
        for i in self._locacoes:
            if i.getCliente() == cliente:
                locacoes.append(str(i))
        return ''.join(locacoes)
    def ListarTodasLocacoes(self):
        locacoes = []
        for i in self._locacoes:
            locacoes.append(str(i))
        return ''.join(locacoes)
    def ListarLocacaoMes(self,mes):
        locacoes = []
        for i in self._locacoes:
            if i.getMes() == mes:
                locacoes.append(str(i))
        return ''.join(locacoes)
    def ListarLocacaoMescomLucro(self,mes):
        valor = 0.0
        for i in self._locacoes:
            if i.getMes() == mes:
                valor += i.valorTotal()
        return f'Lucro do mês {mes}: {str(valor)}'

    def ListarLocacoesFinalizadas(self):
        locacoes = []
        for i in self._locacoes:
            if i.getFinalizada() == True:
                locacoes.append(str(i))
        return ''.join(locacoes)
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

