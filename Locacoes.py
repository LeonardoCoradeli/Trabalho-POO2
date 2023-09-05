from abc import ABC, abstractmethod
from datetime import datetime

#Classe seguro e seus atributos
class Seguro():
    estatico_codigoSeguro = 0
    def __init__(self,nome,tipo,descricao,valor):
        self._codigoSeguro = Seguro.estatico_codigoSeguro
        self._nome = nome
        self._tipo = tipo
        self._descricao = descricao
        self._valor = valor
        Seguro.estatico_codigoSeguro+=1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def tipo(self, nome):
        self._nome = nome

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

#Classe abstrata pagamento
class Pagamento(ABC):
    def __init__(self,tipo):
        self._tipo = tipo

    def __str__(self):
        return  f"Tipo de pagamento: {self._tipo}\n"

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

class Dinheiro(Pagamento):
    def __init__(self,tipo,qtdDeCelulas):
        super().__init__(tipo)
        self._qtdDeCedulas = qtdDeCelulas

    def __str__(self):
        return  f"{super().__str__}" \
                f"Quantidade de cédulas: {self._qtdDeCedulas}\n" \

    @property
    def qtdDeCelulas(self):
        return self._qtdDeCedulas

    @qtdDeCelulas.setter
    def qtdDeCelulas(self, qtdDeCelulas):
        self._qtdDeCelulas = qtdDeCelulas

class Cartao(Pagamento):
    def __init__(self,tipo,nome,bandeira,numero,cvv):
        super().__init__(tipo)
        self._nome = nome
        self._bandeira = bandeira
        self._numero = numero
        self._cvv = cvv

    def __str__(self):
        return  f"{super().__str__}" \
                f"Nome do cartão: {self._nome}\n" \
                f"Bandeira: {self._bandeira}\n" \
                f"Número: {self._numero}\n" \
                f"CVV: {self._cvv}\n"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def bandeira(self):
        return self._bandeira

    @bandeira.setter
    def bandeira(self, bandeira):
        self._bandeira = bandeira

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        self._cvv = cvv

class Locacao():
    estatico_codigoLocacao = 0
    def __init__(self,codCliente,codFuncionario,dataLocacao,dataDevolucao,valorBase,formaPagamento,segurosContratados,
                 finalizada):
        self._codLocacao = Locacao.estatico_codigoLocacao
        self._codCliente = codCliente
        self._codFuncionario = codFuncionario
        self._dataLocacao = datetime.strptime(dataLocacao, "%d/%m/%Y")
        self._dataDevolucao = datetime.strptime(dataDevolucao, "%d/%m/%Y")
        self._valorTotal = float(valorBase)
        self._formapagamento = formaPagamento
        self._segurosContratados = segurosContratados
        self._finalizada = finalizada
        Locacao.estatico_codigoLocacao+=1

    def __str__(self):
        return f"Código de Locação: {self._codLocacao}\n" \
               f"Código de Cliente: {self._codCliente}\n" \
               f"Código de Funcionário: {self._codFuncionario}\n" \
               f"Data de Locação: {self._dataLocacao}\n" \
               f"Data de Devolução: {self._dataDevolucao}\n" \
               f"Valor Total: R${self._valorTotal:.2f}\n" \
               f"Forma de Pagamento: {self._formapagamento}\n" \
               f"Seguros Contratados: {', '.join(self._segurosContratados)}\n" \
               f"Finalizada: {'Sim' if self._finalizada else 'Não'}"

    @property
    def codCliente(self):
        return self._codLocacao

    @codCliente.setter
    def codigoCliente(self, codigoCliente):
        self._codigoCliente = codigoCliente

    @property
    def codFuncionario(self):
        return self._codFuncionario

    @codFuncionario.setter
    def codFuncionario(self, codFuncionario):
        self._codFuncionario = codFuncionario

    @property
    def dataLocacao(self):
        return self._dataLocacao

    @dataLocacao.setter
    def dataLocacao(self, dataLocacao):
        self._dataLocacao = dataLocacao

    @property
    def dataDevolucao(self):
        return self._dataDevolucao

    @dataDevolucao.setter
    def dataDevolucao(self, dataDevolucao):
        self._dataDevolucao = dataDevolucao

    @property
    def valorTotal(self):
        return self._valorTotal

    @valorTotal.setter
    def valorTotal(self, valorTotal):
        self._valorTotal = float(valorTotal)

    @property
    def formaPagamento(self):
        return self._formapagamento

    @formaPagamento.setter
    def formaPagamento(self, formaPagamento):
        self._formapagamento = formaPagamento

    @property
    def segurosContratados(self):
        return self._segurosContratados

    @segurosContratados.setter
    def segurosContratados(self, segurosContratados):
        self._segurosContratados = segurosContratados

    @property
    def finalizada(self):
        return self._finalizada

    @finalizada.setter
    def finalizada(self, finalizada):
        self._finalizada = finalizada

    def calcularValorTotal(self):
        for seguro in self._segurosContratados:
            self._valorTotal+=seguro
        return self._valorTotal

    def possuiSeguro(self):
        if self._segurosContratados:
            return True
        else:
            return False

    def verificarAtrasado(self):
        data_atual = datetime.now()
        if self._dataDevolucao < data_atual and not self._finalizada:
            return True
        else:
            return False