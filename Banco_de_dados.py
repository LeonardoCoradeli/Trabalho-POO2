import requests
import json
import Locacoes
import Usuario
import Veiculos
from datetime import datetime

class BancodeDados:
    URLBanco = 'https://trabalho-pratico-c3891-default-rtdb.firebaseio.com/'
    URLTClientes = 'Clientes'
    URLTFuncionarios = 'Funcionarios'
    URLTabelaLocacoes = 'Locações'
    URLTVeiculosNacionais = 'Veiculos_nacionais'
    URLTVeiculosInternacionais = 'Veiculos_internacionais'
    URLTSeguros = 'Seguros'
    URLTNumeros = 'Numero'
    URLTLocadora = 'Locadora'
    URLTPagamento = 'Pagamento'

    #Enviar e receber dados
    @staticmethod
    def criarFuncionario(funcionario):
        funcionario_dic = funcionario.__dict__
        funcionario_dic['_dataNascimento'] = funcionario_dic['_dataNascimento'].strftime("%d/%m/%Y")
        funcionario_dic['_dataAdmissao'] = funcionario_dic['_dataAdmissao'].strftime("%d/%m/%Y")
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{funcionario_dic['_codigoUsuario']}.json",data=json.dumps(funcionario_dic))

    @staticmethod
    def recuperarFuncionario(codFuncioanrio):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{codFuncioanrio}/.json")
        funcionario_dict = response.json()
        funcionario = Usuario.Funcionario('', '', '', '1/1/2023', '', '', '', 0, '', '1/1/2023')
        funcionario.__dict__.update(funcionario_dict)
        return funcionario


    @staticmethod
    def criarLocacao(locacao):
        locacao_dict = locacao.__dict__
        dataLocacao = locacao_dict["_dataLocacao"].strftime("%d/%m/%Y")
        dataDevolucao = locacao_dict["_dataDevolucao"].strftime("%d/%m/%Y")
        locacao_dict["_dataLocacao"] = dataLocacao
        locacao_dict["_dataDevolucao"] = dataDevolucao
        if locacao_dict['_segurosContratados'] != None:
            listaSeguros = locacao_dict['_segurosContratados']
            locacao_dict['_segurosContratados'] = listaSeguros.__dict__  ##[c.__dict__ for c in listaSeguros]
        else:
            locacao_dict = ''
        locacao_dict['_veiculo'] = locacao_dict['_veiculo'].__dict__
        locacao_dict['_codCliente'] = locacao_dict['_codCliente'].__dict__
        locacao_dict['_codFuncionario'] = locacao_dict['_codFuncionario'].__dict__
        pagamento = locacao_dict['_formaPagamento']
        locacao_dict['_formaPagamento'] = pagamento.__dict__
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{locacao_dict['_codLocacao']}.json",data=json.dumps(locacao_dict))

    @staticmethod
    def recuperarLocacao(codLocacao):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{codLocacao}.json")
        locacao_dict = response.json()
        if locacao_dict['_segurosContratados'] != None:
            listaSeguros = locacao_dict['_segurosContratados']
            seguros = []
            for c in listaSeguros:
                seguro = Locacoes.Seguro('', '', '', 0)
                seguro.__dict__.update(c)
                seguros.append(seguro)
            locacao_dict['_segurosContratados'] = seguros
        pag = locacao_dict['_formaPagamento']
        pagamento = Locacoes.Cartao('','','',0,0) if locacao_dict['_formaPagamento']['_tipo'] == 'cartao' else Locacoes.Dinheiro('',0)
        pagamento.__dict__.update(pag)
        locacao_dict['_formaPagamento'] = pagamento
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
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTClientes}/{cliente_dict['_codigoUsuario']}.json",data=json.dumps(cliente_dict))


    @staticmethod
    def recuperarCliente(codCliente):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTClientes}/{codCliente}/.json")
        cliente_dict = response.json()
        cliente = Usuario.Cliente('','','','1/1/2023','','','','','','1/1/2023',False,1)
        cliente.__dict__.update(cliente_dict)
        return cliente

    @staticmethod
    def criarVeiculoNacional(veiculo):
        veiculo_dict = veiculo.__dict__
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosNacionais}/{veiculo_dict['_codigoVeiculo']}.json",
                         data=json.dumps(veiculo_dict))

    @staticmethod
    def recuperarVeiculoNacional(codVeiculo):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosNacionais}/{codVeiculo}/.json")
        veiculo_dict = response.json()
        veiculo = Veiculos.VeiculoNacional('','',0,0,'','',0,0,'',False,0)
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
        veiculo = Veiculos.VeiculoImportado('','',0,0,'','',0,0,'',False,0,0)
        veiculo.__dict__.update(veiculo_dict)
        return veiculo

    @staticmethod
    def criarSeguro(seguro):
        seguro_dict = seguro.__dict__
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{seguro_dict['_codigoSeguro']}/.json", data=json.dumps(seguro_dict))

    @staticmethod
    def recuperarSeguro(codSeguro):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{codSeguro}/.json")
        seguro_dict = response.json()
        seguro = Locacoes.Seguro('','','',0)
        seguro.__dict__.update(seguro_dict)
        return seguro

    @staticmethod
    def criarPagamento(pagamento):
        pagamento_dict = pagamento.__dict__
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTPagamento}/{pagamento_dict['_codigoPagamento']}/.json", data=json.dumps(pagamento_dict))

    @staticmethod
    def recuperarPagamento(codPagamento):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTPagamento}/{codPagamento}/.json")
        pagamento_dict = response.json()
        pagamento = Locacoes.Cartao('','','',0,0) if pagamento_dict['_tipo'] == 'cartao' else Locacoes.Dinheiro('',0)
        pagamento.__dict__.update(pagamento_dict)
        return pagamento
    #quando for fazer passar os argumentos fazer um dicionario com os nomes dos campos  valores atualizar(cod...,**dicionario)

    @staticmethod
    def atualizarFuncionario(codFuncionario,**kwargs):
        funcionario = {
        }

        campos = {
        'nome': '_nome',
        'cpf': '_cpf',
        'rg': '_rg',
        'dataNascimento': '_dataNascimento',
        'endereco': '_endereco',
        'cep': '_cep',
        'email': '_email',
        'salario': '_salario',
        'pis': '_pis',
        'dataAdmissao': '_dataAdmissao'
        }

        for campo, chave in campos.items():
            if campo in kwargs:
                funcionario[chave] = kwargs[campo]
            else:
                funcionario[chave] = ''

        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{codFuncionario}/.json")
        funcionarioData = response.json()

        for campo, valor in funcionario.items():
            if valor == '' and campo in funcionarioData:
                funcionario[campo] = funcionarioData[campo]

        print(funcionario)
        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{codFuncionario}.json",data=json.dumps(funcionario))

    @staticmethod
    def atualizarLocacao(codLocacao, **kwargs):
        locacao ={}

        campos = {
            'dataLocacao': '_dataLocacao',
            'dataDevolucao': '_dataDevolucao',
            'valorTotal': '_valorTotal',
            'veiculo': '_veiculos',
            'cliente': '_cliente',
            'funcionario': '_funcionario',
            'segurosContradados': '_segurosContratados',
            'formaPagamento': '_formaPagamento'
        }

        for campo, chave in campos.items():
            if campo in kwargs:
                locacao[chave] = kwargs[campo]
            else:
                locacao[chave] = ''

        if locacao['_segurosContratados'] != '':
            seg = []
            for c in locacao['_segurosContratados']:
                seguro = Locacoes.Seguro('', '', '', 0)
                seguro.__dict__.update(c)
                seg.append(seguro)
            locacao['_seguros'] = seg
        
        if locacao['_formaPagamento'] != '':
            formaPagamento_dict = locacao['_formapagamento'].__dict__
            locacao['_formapagamento'] = formaPagamento_dict

        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{codLocacao}/.json")
        locacaoData = response.json()

        for campo, valor in locacao.items():
            if valor == '' and campo in locacaoData:
                locacao[campo] = locacaoData[campo]
        
        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{codLocacao}.json",
                       data=json.dumps(locacao))



    @staticmethod
    def atualizarCliente(codCliente, **kwargs):
        cliente = {}

        campos = {
            'nome': '_nome',
            'cpf': '_cpf',
            'rg': '_rg',
            'dataNascimento':'_dataNascimento',
            'endereco': '_endereco',
            'cep': '_cep',
            'email': '_email',
            'validadeCNH': '_validadeCNH',
            'categoriaCNH': '_categoriaCNH'
            }

        for campo, chave in campos.items():
            if campo in kwargs:
                cliente[chave] = kwargs[campo]

        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTClientes}/{codCliente}/.json")
        clienteData = response.json()


        for campo, valor in cliente.items():
            if valor == '' and campo in clienteData:
                cliente[campo] = clienteData[campo]

        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTClientes}/{codCliente}.json",
                       data=json.dumps(cliente))

    @staticmethod
    def atualizarVeiculoNacional(codVeiculo, **kwargs):
        veiculo = {}

        campos = {
            'marca': '_marca',
            'modelo': '_modelo',
            'anoFabricacao': '_anoFabricacao',
            'anoModelo': '_anoModelo',
            'placa': '_placa',
            'cor': '_cor',
            'valorDiaria': '_valorDiaria',
            'valorKmRodado': '_valorKmRodado',
            'categoria':'_categoria',
            'disponivel': '_disponivel',
            'quilometragem': '_quilometragem',
            'capacidadeTanque': '_capacidadeTanque'
        }

        for campo, chave in campos.items():
            if campo in kwargs:
                veiculo[chave] = kwargs[campo]
        
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosNacionais}/{codVeiculo}/.json")
        veiculoData = response.json()


        for campo, valor in veiculo.items():
            if valor == '' and campo in veiculoData:
                veiculo[campo] = veiculoData[campo]

        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosNacionais}/{codVeiculo}.json",data=json.dumps(veiculo))

    @staticmethod
    def atualizarVeiculoImportado(codVeiculo, **kwargs):
        veiculo ={}

        campos = {
            'marca': '_marca',
            'modelo': '_modelo',
            'anoFabricacao': '_anoFabricacao',
            'anoModelo': '_anoModelo',
            'placa': '_placa',
            'cor': '_cor',
            'valorDiaria': '_valorDiaria',
            'valorKmRodado': '_valorKmRodado',
            'categoria': '_categoria',
            'disponivel': '_disponivel',
            'quilometragem': '_quilometragem',
            'capacidadeTanque': '_capacidadeTanque',
            'impostoImportacao': '_impostoImportacao'
        }

        for campo, chave in campos.items():
            if campo in kwargs:
                veiculo[chave] = kwargs[campo]
        
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosInternacionais}/{codVeiculo}/.json")
        veiculoData = response.json()


        for campo, valor in veiculo.items():
            if valor == '' and campo in veiculoData:
                veiculo[campo] = veiculoData[campo]

        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosInternacionais}/{codVeiculo}.json",data=json.dumps(veiculo))

    @staticmethod
    def atualizarSeguro(codSeguro, **kwargs):

        seguro ={}

        campos = {
            'descricao': '_descricao',
            'cobertura': '_cobertura',
            'valorFranquia': '_valorFranquia',
            'valorMensal': '_valorMensal'
        }

        for campo, chave in campos.items():
            if campo in kwargs:
                seguro[chave] = kwargs[campo]
        
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{codSeguro}/.json")
        seguroData = response.json()


        for campo, valor in seguro.items():
            if valor == '' and campo in seguroData:
                seguro[campo] = seguroData[campo]

        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{codSeguro}.json", data=json.dumps(seguro))

    #Excluir dados do banco de dados
    @staticmethod
    def excluirFuncionario(codFuncionario):
        requests.delete(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{codFuncionario}.json")

    @staticmethod
    def excluirCliente(codCliente):
        requests.delete(f"{BancodeDados.URLBanco}{BancodeDados.URLTClientes}/{codCliente}.json")

    @staticmethod
    def excluirLocacao(codLocacao):
        requests.delete(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{codLocacao}.json")

    @staticmethod
    def excluirSeguro(codSeguro):
        requests.delete(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{codSeguro}.json")

    @staticmethod
    def excluirVeiculoNacional(codVeiculo):
        requests.delete(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosNacionais}/{codVeiculo}.json")

    @staticmethod
    def excluirVeiculoInternacional(codVeiculo):
        requests.delete(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosInternacionais}/{codVeiculo}.json")
    
    #puxar dados
    @staticmethod
    def recuperarTodosClientes():
        response = requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTClientes}.json')
        clientes_list = response.json()
        clientes = []
        for cliente in clientes_list:
            c = Usuario.Cliente('', '', '', '1/1/2023', '', '', '', '', '', '1/1/2023', False, 1)
            c.__dict__.update(cliente)
            clientes.append(c)
        return clientes

    @staticmethod
    def recuperarTodosFuncionarios():
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}.json")
        funcionario_list = response.json()
        funcionarios = []
        for funcionario in funcionario_list:
            if funcionario != None:
                f = Usuario.Funcionario('', '', '', '1/1/2023', '', '', '', 0, '', '1/1/2023')
                f.__dict__.update(funcionario)
                funcionarios.append(f)
        return funcionarios

    @staticmethod
    def recuperarTodasLocacoes():
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}.json")
        locacoes_list = response.json()
        locacoes = []
        for locacao in locacoes_list:
            if locacao['_segurosContratados'] != None:
                listaSeguros = locacao['_segurosContratados']
                seguros = []
                for c in listaSeguros:
                    seguro = Locacoes.Seguro('', '', '', 0)
                    seguro.__dict__.update(c)
                    seguros.append(seguro)
                locacao['_segurosContratados'] = seguros
            pag = locacao['_formaPagamento']
            pagamento = Locacoes.Cartao('', '', '', 0, 0) if locacao['_formaPagamento']['_tipo'] == 'cartao' else Locacoes.Dinheiro('', 0)
            pagamento.__dict__.update(pag)
            locacao['_formaPagamento'] = pagamento
            datalocacao = locacao['_dataLocacao']
            dataDevolucao = locacao['_dataDevolucao']
            locacao['_dataLocacao'] = datetime.strptime(str(datalocacao), "%d/%m/%Y")
            locacao['_dataDevolucao'] = datetime.strptime(str(dataDevolucao), "%d/%m/%Y")
            cliente = locacao['_codCliente']
            c = Usuario.Cliente('', '', '', '1/1/2023', '', '', '', '', '', '1/1/2023', False, 0)
            c.__dict__.update(cliente)
            locacao['_codCliente'] = c
            funcionario = locacao['_codFuncionario']
            f = Usuario.Funcionario('', '', '', '1/1/2023', '', '', '', 0, '', '1/1/2023')
            f.__dict__.update(funcionario)
            locacao['_codFuncionario'] = f
            veiculo = locacao['_veiculo']
            v = Veiculos.VeiculoNacional('', '', 0, 0, '', '', 0, 0, '', False, 0)
            v.__dict__.update(veiculo)
            locacao['_veiculo'] = v
            l = Locacoes.Locacao('', '', '', '1/1/2023','1/1/2023', 0, '', '', '', 1)
            l.__dict__.update(locacao)
            locacoes.append(l)

        return locacoes

    @staticmethod
    def recuperarTodosVeiculosNacionais():
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosNacionais}.json")
        veiculo_list = response.json()
        veiculos = []
        for veiculo in veiculo_list:
            v = Veiculos.VeiculoNacional('','',0,0,'','',0,0,'',False,0)
            v.__dict__.update(veiculo)
            veiculos.append(v)

        return veiculos

    @staticmethod
    def recuperarTodosVeiculosImportados():
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosInternacionais}.json")
        veiculo_list = response.json()
        veiculos = []
        for veiculo in veiculo_list:
            v = Veiculos.VeiculoImportado('', '', 0, 0, '', '', 0, 0, '', False, 0,0)
            v.__dict__.update(veiculo)
            veiculos.append(v)

        return veiculos

    @staticmethod
    def recuperarTodosSeguros():
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}.json")
        seguro_list = response.json()
        seguros = []
        for seguro in seguro_list:
            s = Locacoes.Seguro('', '', '', 0)
            s.__dict__.update(seguro)
            seguros.append(s)

        return seguros

    #recuperar numero de cada tipo
    @staticmethod
    def recuperarNumeroClientes():
        response = requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Clientes.json')
        numero = response.json()
        return numero

    @staticmethod
    def recuperarNumeroFuncionarios():
        response = requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Funcionarios.json')
        numero = response.json()
        return numero

    @staticmethod
    def recuperarNumeroLocacoes():
        response = requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Locacoes.json')
        numero = response.json()
        return numero

    @staticmethod
    def recuperarNumeroSeguros():
        response = requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Seguros.json')
        numero = response.json()
        return numero

    @staticmethod
    def recuperarNumeroVeiculosNacionais():
        response = requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Veiculos_nacionais.json')
        numero = response.json()
        return numero

    @staticmethod
    def recuperarNumeroVeiculosImportados():
        response = requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Veiculos_internacionais.json')
        numero = response.json()
        return numero

    #Salvar cada numero
    @staticmethod
    def salvarNumeroClientes(numero):
        requests.put(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Clientes.json',data=json.dumps(numero))

    @staticmethod
    def salvarNumeroFuncionarios(numero):
        requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Funcionarios.json',data=json.dumps(numero))


    @staticmethod
    def salvarNumeroLocacoes(numero):
        requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Locacoes.json',data=json.dumps(numero))

    @staticmethod
    def salvarNumeroSeguros(numero):
        requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Seguros.json',data=json.dumps(numero))

    @staticmethod
    def salvarNumeroVeiculosNacionais(numero):
        requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Veiculos_nacionais.json',data=json.dumps(numero))

    @staticmethod
    def salvarNumeroVeiculosImportados(numero):
        requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTNumeros}/Veiculos_internacionais.json',data=json.dumps(numero))



    #salvar a propia locadora em si
    @staticmethod
    def criarLocadora(locadora):#dicionario com nome,endereço,website e rede social
        response = requests.put(f'{BancodeDados.URLBanco}{BancodeDados.URLTLocadora}.json',data=json.dumps(locadora))

    @staticmethod
    def recuperarLocadora():
        response = requests.get(f'{BancodeDados.URLBanco}{BancodeDados.URLTLocadora}.json')
        locadora = response.json()
        return locadora

