from abc import ABC, abstractmethod
from datetime import datetime


class Usuario(ABC):
    def __init__(self, codigoUsuario,nome, cpf, rg, dataNascimento, endereco, cep, email):
        self._codigoUsuario = codigoUsuario
        self._nome = nome
        self._cpf = cpf
        self._rg = rg
        self._dataNascimento = datetime.strptime(dataNascimento, "%d/%m/%Y")
        self._endereco = endereco
        self._cep = cep
        self._email = email

    def __str__(self):
        return f"Código do Usuário: {self._codigoUsuario}\n" \
               f"Nome: {self._nome}\n" \
               f"CPF: {self._cpf}\n" \
               f"RG: {self._rg}\n" \
               f"Data de Nascimento: {self._dataNascimento}\n" \
               f"Endereço: {self._endereco}\n" \
               f"CEP: {self._cep}\n" \
               f"Email: {self._email}"

    @property
    def codigoUsuario(self):
        return self._codigoUsuario

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def rg(self):
        return self._rg

    @property
    def dataNascimento(self):
        return self._dataNascimento

    @property
    def endereco(self):
        return self._endereco

    @property
    def cep(self):
        return self._cep

    @property
    def email(self):
        return self._email

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @rg.setter
    def rg(self, rg):
        self._rg = rg

    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self._dataNascimento = dataNascimento

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @cep.setter
    def cep(self, cep):
        self._cep = cep

    @email.setter
    def email(self, email):
        self._email = email


class Cliente(Usuario):
    Estatico_codigoCliente = 0
    def __init__(self, nome, cpf, rg, dataNascimento, endereco, cep, email, categoriaCNH, numeroCNH, validadeCNH, clienteOuro,codigoUsuario=None):
        if codigoUsuario == None:
            super().__init__(Cliente.Estatico_codigoCliente,nome, cpf, rg, dataNascimento, endereco, cep, email)
            self._categoriaCNH = categoriaCNH
            self._numeroCNH = numeroCNH
            self._validadeCNH = datetime.strptime(validadeCNH, "%d/%m/%Y")
            self._clienteOuro = clienteOuro
            Cliente.Estatico_codigoCliente +=1
        else:
            super().__init__(codigoUsuario, nome, cpf, rg, dataNascimento, endereco, cep, email)
            self._categoriaCNH = categoriaCNH
            self._numeroCNH = numeroCNH
            self._validadeCNH = datetime.strptime(validadeCNH, "%d/%m/%Y")
            self._clienteOuro = clienteOuro

    def __str__(self):
        usuarioStr = super().__str__()
        return f"{usuarioStr}\n" \
               f"Categoria da CNH: {self._categoriaCNH}\n" \
               f"Número da CNH: {self._numeroCNH}\n" \
               f"Validade da CNH: {self._validadeCNH}\n" \
               f"Cliente Ouro: {self._clienteOuro}"
    @property
    def categoriaCNH(self):
        return self._categoriaCNH

    @property
    def numeroCNH(self):
        return self._numeroCNH

    @property
    def validadeCNH(self):
        return self._validadeCNH

    @property
    def clienteOuro(self):
        return self._clienteOuro

    @categoriaCNH.setter
    def categoriaCNH(self, categoriaCNH):
        self._categoriaCNH = categoriaCNH

    @numeroCNH.setter
    def numeroCNH(self, numeroCNH):
        self._numeroCNH = numeroCNH

    @validadeCNH.setter
    def validadeCNH(self, validadeCNH):
        self._validadeCNH = validadeCNH

    @clienteOuro.setter
    def clienteOuro(self, clienteOuro):
        self._clienteOuro = clienteOuro


    def setEstatico_codigoFuncionari(self, numero):
        self.Estatico_codigoCliente = numero


    def getEstatico_codigoCliente(self):
        return self.Estatico_codigoCliente



class Funcionario(Usuario):
    Estatico_codigoFuncionario = 0
    def __init__(self, nome, cpf, rg, dataNascimento, endereco, cep, email, salario, pis, dataAdmissao,codigoUsuario=None):
        if codigoUsuario == None:
            super().__init__(Funcionario.Estatico_codigoFuncionario,nome, cpf, rg, dataNascimento, endereco, cep, email)
            self._salario = float(salario)
            self._pis = pis
            self._dataAdmissao = datetime.strptime(dataAdmissao, "%d/%m/%Y")
            Funcionario.Estatico_codigoFuncionario +=1
        else:
            super().__init__(codigoUsuario, nome, cpf, rg, dataNascimento, endereco, cep,email)
            self._salario = float(salario)
            self._pis = pis
            self._dataAdmissao = datetime.strptime(dataAdmissao, "%d/%m/%Y")

    def __str__(self):
        usuarioStr = super().__str__()
        return f"{usuarioStr}\n"\
               f"Salário: {self._salario}\n" \
               f"PIS: {self._pis}\n" \
               f"Data de Admissão: {self._dataAdmissao}"

    @property
    def salario(self):
        return self._salario

    @property
    def pis(self):
        return self._pis

    @property
    def dataAdmissao(self):
        return self._dataAdmissao

    @salario.setter
    def salario(self, salario):
        self._salario = float(salario)

    @pis.setter
    def pis(self, pis):
        self._pis = pis

    @dataAdmissao.setter
    def dataAdmissao(self, data):
        self._dataAdmissao = data


    def setEstatico_codigoFuncionari(self, numero):
        self.Estatico_codigoFuncionario = numero


    def getEstatico_codigoFuncionario(self):
        return self.Estatico_codigoFuncionario
