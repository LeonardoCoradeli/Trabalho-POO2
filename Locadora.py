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


    def CadastrarFuncionario(self,funcionario):
        self._configuracao.criarFuncionario(funcionario)
        self._funcionarios.append(funcionario)

    def CadastrarCliente(self,cliente):
        self._configuracao.criarCliente(cliente)
        self._clientes.append(cliente)

    def CadastrarVeiculo(self,veiculo):
        if isinstance(veiculo, Veiculos.VeiculoNacional):
            self._configuracao.criarVeiculoNacional(veiculo)
        else:
            self._configuracao.criarVeiculoImportado(veiculo)
        self._veiculos.append(veiculo)

    def CadastrarSeguro(self,seguro):
        self._configuracao.criarSeguro(seguro)
        self._seguros.append(seguro)

    def CadastrarLocacao(self,locacao):
        self._configuracao.criarLocacao(locacao)
        self._locacoes.append(locacao)

    def ListarVeiculos(self):
        veiculos = []
        for i in self._veiculos:
            veiculos.append(str(i))
        return ''.join(veiculos)

    
    def ListarVeiculosNacionais(self):
        veiculos = []
        for i in self._veiculos:
            if isinstance(i,Veiculos.VeiculoNacional):
                veiculos.append(str(i))
        return ''.join(veiculos)
    
    def ListarVeiculosImportados(self):
        veiculos = []
        for i in self._veiculos:
            if isinstance(i,Veiculos.VeiculoImportado):
                veiculos.append(str(i))
        return ''.join(veiculos)
    
    def ListarVeiulosDisponiveis(self):
        veiculos = []
        for i in self._veiculos:
            if not i.alugado:
                veiculos.append(str(i))
        return ''.join(veiculos)
    
    def ListarVeiculosDisponiveisCategoria(self,categoria):
        veiculos = []
        for i in self._veiculos:
            if not i.alugado and i.categoria == categoria:
                veiculos.append(str(i))
        return ''.join(veiculos)
    
    def ListarVeiculosNãoDisponiveis(self):
        veiculos = []
        for i in self._veiculos:
            if not i.alugado == False:
                veiculos.append(str(i))
        return ''.join(veiculos)
    
    def ListarVeiculosAtrasados(self):
        veiculos = []
        for i in self._locacoes:
            if i.verificarAtrasado():
                veiculos.append(str(i))
        return ''.join(veiculos)
    def ListarClientesComLocacao(self):
        indices = []
        clientes = []
        for i in self._locacoes:
            indices.append(i.codCliente)

        for j in self._clientes:
            if j.codigoUsuario in indices:
                clientes.append(str(j))
        return ''.join(clientes)
    
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

    def buscarVeiculo(self,cod=None,placa=None):
        veiculos = []
        if not placa is None:
            for i in self._veiculos:
                if placa in i.placa:
                    veiculos.append(str(i))
        elif not cod is None:
            for i in self._veiculos:
                if cod == i.codigoVeiculo:
                    veiculos.append(str(i))
        return ''.join(veiculos)

    def buscarCliente(self,cod=None,nome=None,cpf=None):
        clientes = []
        if not nome is None:
            for i in self._clientes:
                if nome in i.nome:
                    clientes.append(str(i))
        elif not cod is None:
            for i in self._clientes:
                if cod == i.codigoUsuario:
                    clientes.append(str(i))
        elif not cpf is None:
            for i in self._clientes:
                if cpf in i.cpf:
                    clientes.append(str(i))
        return ''.join(clientes)

    def buscarFuncionario(self,cod=None,nome=None,cpf=None):
        funcionarios = []
        if not nome is None:
            for i in self._funcionarios:
                if nome in i.nome:
                    funcionarios.append(str(i))
        elif not cod is None:
            for i in self._funcionarios:
                if cod == i.codigoUsuario:
                    funcionarios.append(str(i))
        elif not cpf is None:
            for i in self._funcionarios:
                if cpf in i.cpf:
                    funcionarios.append(str(i))
        return ''.join(funcionarios)

    def buscarLocacao(self,cod=None):
        locacoes = []
        if not cod is None:
            for i in self._locacoes:
                if cod == i.codLocacao:
                    locacoes.append(str(i))
        return ''.join(locacoes)