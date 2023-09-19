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
        if locacao_dict['_segurosContratados'] != None:
            listaSeguros = locacao_dict['_segurosContratados']
            locacao_dict['_segurosContratados'] = [c.__dict__ for c in listaSeguros]
        else:
            locacao_dict = ''
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

    #Alterar dados → somente o primeiro,segundo,terceiro, quarto esta correto para testar
    #quando for fazer passar os argumentos fazer um dicionario com os nomes dos campos  valores atualizar(cod...,**dicionario)

    @staticmethod
    def atualizarFuncionario(codFuncionario,**kwargs):
        funcionario = {
        }

        #Para usar a função escreva cpf=********** por exemplo 
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
        print(funcionarioData)

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
            'seguros': '_seguros',
            'formaPagamento': '_formaPagamento'
        }

        for campo, chave in campos.items():
            if campo in kwargs:
                locacao[chave] = kwargs[campo]

        seg = []
        for c in locacao['_seguros']:
            seguro = Locacoes.Seguro('', '', '', 0)
            seguro.__dict__.update(c)
            seg.append(seguro)
        locacao['_seguros'] = seg
        formaPagamento_dict = locacao['_formapagamento'].__dict__
        locacao['_formapagamento'] = formaPagamento_dict

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

        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosNacionais}/{codVeiculo}.json",
                       data=json.dumps(veiculo))

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

        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosInternacionais}/{codVeiculo}.json",
                       data=json.dumps(veiculo))

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

        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{codSeguro}.json", data=json.dumps(seguro))
