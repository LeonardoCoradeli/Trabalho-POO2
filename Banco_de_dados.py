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
        listaSeguros = locacao_dict['_seguros']
        locacao_dict['_seguros'] = [c.__dict__ for c in listaSeguros]
        pagamento = locacao_dict['_formapagamento'].__dict__
        locacao_dict['_formapagamento'] = pagamento
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{locacao_dict['_codLocacao']}.json",data=json.dumps(locacao_dict))

    @staticmethod
    def recuperarLocacao(codLocacao):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{codLocacao}.json")
        locacao_dict = response.json()
        if locacao_dict['_seguros'] != None:
            listaSeguros = locacao_dict['_seguros']
            seguros = []
            for c in listaSeguros:
                seguro = Locacoes.Seguro('', '', '', 0)
                seguro.__dict__.update(c)
                seguros.append(seguro)
            locacao_dict['_seguros'] = seguros
        pag = locacao_dict['_formapagamento']
        pagamento = Locacoes.Cartao('','','',0,0) if locacao_dict['_formapagamento']['tipo'] == 'cartão' else Locacoes.Dinheiro('',0)
        pagamento.__dict__.update(pag)
        locacao_dict['_formapagamento'] = pagamento
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
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{cliente_dict['_codigoUsuario']}.json",
                     data=json.dumps(cliente_dict))

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
        veiculo = Veiculos.VeiculoNacional('','',0,0,'','',0,0,'',False,0,0)
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
        veiculo = Veiculos.VeiculoImportado('','',0,0,'','',0,0,'',False,0,0,0)
        veiculo.__dict__.update(veiculo_dict)
        return veiculo

    @staticmethod
    def criarSeguro(seguro):
        seguro_dict = seguro.__dict__
        requests.put(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{seguro_dict['_codigoSeguro']}/.json")

    @staticmethod
    def recuperarSeguro(codSeguro):
        response = requests.get(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{codSeguro}/.json")
        seguro_dict = response.json()
        seguro = Locacoes.Seguro('','','',0,0)
        seguro.__dict__.update(seguro_dict)
        return seguro

    #Alterar dados → somente o primeiro esta correto para testar
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

        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTFuncionarios}/{codFuncionario}.json",data=json.dumps(funcionario))

    @staticmethod
    def atualizarLocacao(codLocacao, dataLocacao=None, dataDevolucao=None, valorTotal=None, veiculo=None, cliente=None,
                         funcionario=None, seguros=[], formaPagamento=None):
        locacao = {
            '_dataLocacao': dataLocacao if dataLocacao is not None else None,
            '_dataDevolucao': dataDevolucao if dataDevolucao is not None else None,
            '_valorTotal': float(valorTotal) if valorTotal is not None else None,
            '_veiculo': veiculo if veiculo is not None else None,
            '_cliente': cliente if cliente is not None else None,
            '_funcionario': funcionario if funcionario is not None else None,
            '_seguros': seguros if seguros is not [] else [],
            '_formapagamento': formaPagamento if formaPagamento is not None else None
        }
        seg = []
        for c in seguros:
            seguro = Locacoes.Seguro('', '', '', 0)
            seguro.__dict__.update(c)
            seg.append(seguro)
        locacao['_seguros'] = seguros
        formaPagamento_dict = formaPagamento.__dict__
        locacao['_formapagamento'] = formaPagamento_dict
        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTabelaLocacoes}/{codLocacao}.json",
                       data=json.dumps(locacao))

    @staticmethod
    def atualizarCliente(codCliente, nome=None, cpf=None, rg=None, dataNascimento=None, endereco=None, cep=None,
                         email=None, validadeCNH=None, categoriaCNH=None):
        cliente = {
            '_nome': nome if nome is not None else None,
            '_cpf': cpf if cpf is not None else None,
            '_rg': rg if rg is not None else None,
            '_dataNascimento': dataNascimento if dataNascimento is not None else None,
            '_endereco': endereco if endereco is not None else None,
            '_cep': cep if cep is not None else None,
            '_email': email if email is not None else None,
            '_validadeCNH': validadeCNH if validadeCNH is not None else None,
            '_categoriaCNH': categoriaCNH if categoriaCNH is not None else None,
        }
        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTClientes}/{codCliente}.json",
                       data=json.dumps(cliente))

    @staticmethod
    def atualizarVeiculoNacional(codVeiculo, marca=None, modelo=None, anoFabricacao=None, anoModelo=None, placa=None,
                                 cor=None, valorDiaria=None, valorKmRodado=None, categoria=None, disponivel=None,
                                 quilometragem=None, capacidadeTanque=None):
        veiculo = {
            '_marca': marca if marca is not None else None,
            '_modelo': modelo if modelo is not None else None,
            '_anoFabricacao': anoFabricacao if anoFabricacao is not None else None,
            '_anoModelo': anoModelo if anoModelo is not None else None,
            '_placa': placa if placa is not None else None,
            '_cor': cor if cor is not None else None,
            '_valorDiaria': float(valorDiaria) if valorDiaria is not None else None,
            '_valorKmRodado': float(valorKmRodado) if valorKmRodado is not None else None,
            '_categoria': categoria if categoria is not None else None,
            '_disponivel': disponivel if disponivel is not None else None,
            '_quilometragem': float(quilometragem) if quilometragem is not None else None,
            '_capacidadeTanque': float(capacidadeTanque) if capacidadeTanque is not None else None
        }
        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosNacionais}/{codVeiculo}.json",
                       data=json.dumps(veiculo))

    @staticmethod
    def atualizarVeiculoImportado(codVeiculo, marca=None, modelo=None, anoFabricacao=None, anoModelo=None, placa=None,
                                  cor=None, valorDiaria=None, valorKmRodado=None, categoria=None, disponivel=None,
                                  quilometragem=None, capacidadeTanque=None, impostoImportacao=None):
        veiculo = {
            '_marca': marca if marca is not None else None,
            '_modelo': modelo if modelo is not None else None,
            '_anoFabricacao': anoFabricacao if anoFabricacao is not None else None,
            '_anoModelo': anoModelo if anoModelo is not None else None,
            '_placa': placa if placa is not None else None,
            '_cor': cor if cor is not None else None,
            '_valorDiaria': float(valorDiaria) if valorDiaria is not None else None,
            '_valorKmRodado': float(valorKmRodado) if valorKmRodado is not None else None,
            '_categoria': categoria if categoria is not None else None,
            '_disponivel': disponivel if disponivel is not None else None,
            '_quilometragem': float(quilometragem) if quilometragem is not None else None,
            '_capacidadeTanque': float(capacidadeTanque) if capacidadeTanque is not None else None,
            '_impostoImportacao': float(impostoImportacao) if impostoImportacao is not None else None
        }
        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTVeiculosInternacionais}/{codVeiculo}.json",
                       data=json.dumps(veiculo))

    @staticmethod
    def atualizarSeguro(codSeguro, descricao=None, cobertura=None, valorFranquia=None, valorMensal=None):
        seguro = {
            '_descricao': descricao if descricao is not None else None,
            '_cobertura': cobertura if cobertura is not None else None,
            '_valorFranquia': float(valorFranquia) if valorFranquia is not None else None,
            '_valorMensal': float(valorMensal) if valorMensal is not None else None
        }
        requests.patch(f"{BancodeDados.URLBanco}{BancodeDados.URLTSeguros}/{codSeguro}.json", data=json.dumps(seguro))