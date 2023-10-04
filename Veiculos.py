from abc import ABC, abstractmethod
#Classe veiculos e seus atributos

class Veiculo(ABC):
    def __init__(self,codigoVeiculo,nomeModelo,montadora,anoFabricacao,anoModelo,placa,categoria,valorFipe,valorDiaria,categoriaCNHNecessaria,alugado):
        self._codigoVeiculo = codigoVeiculo
        self._nomeModelo = nomeModelo
        self._montadora = montadora
        self._anoFabricacao = anoFabricacao
        self._anoModelo = anoModelo
        self._placa = placa
        self._categoria = categoria
        self._valorFipe = valorFipe
        self._valorDiaria = valorDiaria
        self._categoriaCNHNecessaria = categoriaCNHNecessaria
        self._alugado = alugado

    def __str__(self):
        return  f"-----------------------------------------\n"\
                f"Código do Veículo: {self._codigoVeiculo}\n" \
                f"Nome do Modelo: {self._nomeModelo}\n" \
                f"Montadora: {self._montadora}\n" \
                f"Ano de Fabricação: {self._anoFabricacao}\n" \
                f"Ano do Modelo: {self._anoModelo}\n" \
                f"Placa: {self._placa}\n" \
                f"Categoria: {self._categoria}\n" \
                f"Valor FIPE: R${self._valorFipe:.2f}\n" \
                f"Valor da Diária: R${self._valorDiaria:.2f}\n" \
                f"Categoria CNH Necessária: {self._categoriaCNHNecessaria}\n" \
                f"Alugado: {'Sim' if self._alugado else 'Não'}\n" \
                f"-----------------------------------------\n"


    @property
    def codigoVeiculo(self):
        return self._codigoVeiculo
        
    @property
    def nomeModelo(self):
        return self._nomeModelo
    
    @nomeModelo.setter
    def nomeModelo(self,nomeModelo):
        self._nomeModelo = nomeModelo
        
    @property
    def montadora(self):
        return self._montadora
        
    @montadora.setter
    def montadora(self,montadora):
        self._montadora = montadora
    
    @property
    def anoFabricacao(self):
        return self._anoFabricacao
    
    @anoFabricacao.setter
    def anoFabricacao(self,anoFabricacao):
        self._anoFabricacao = anoFabricacao
    
    @property
    def anoModelo(self):
        return self._anoModelo
    
    @anoModelo.setter
    def anoModelo(self,anoModelo):
        self._anoModelo = anoModelo
    
    @property 
    def placa(self):
        return self._placa
        
    @placa.setter
    def placa(self,placa):
        self._placa = placa 
    
    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self,categoria):
        self._categoria = categoria
    
    @property
    def valorFipe(self):
        return self._valorFipe
    
    @valorFipe.setter
    def valorFipe(self,valorFipe):
        self._valorFipe = valorFipe
        
    @property
    def valorDiaria(self):
        return self._valorDiaria
    
    @valorDiaria.setter
    def valorDiaria(self,valorDiaria):
        self._valorDiaria = valorDiaria
    
    @property 
    def categoriaCNHNecessaria(self):
        return self._categoriaCNHNecessaria
    
    @categoriaCNHNecessaria.setter
    def categoriaCNHNecessaria(self,categoriaCNHNecessaria):
         self._categoriaCNHNecessaria = categoriaCNHNecessaria
    
    @property
    def alugado(self):
        return self._alugado
    
    @alugado.setter
    def alugado(self,alugado):
        self._alugado = alugado
    
    @abstractmethod
    def calcularValorMedia(self):
        pass
    
    def estaAlugado(self):
        if self._alugado:
            return True
        return False
            
    def alugar(self):
        if self.estaAlugado():
            return False
        return True
    
    def devolver(self):
        if self.estaAlugado():
            return False
        return "O veiculo não foi alugado ainda"
    
    def __str__(self):
        return  f"-----------------------------------------\n"\
                f"Codigo Veiculo: {self._codigoVeiculo}\n" \
                f"Modelo: {self._nomeModelo}\n" \
                f"Montadora: {self._montadora}\n" \
                f"Ano Fabricação: {self._anoFabricacao}\n" \
                f"Ano do Modelo: {self._anoModelo}\n" \
                f"Placa: {self._placa}\n" \
                f"Categoria: {self._categoria}\n" \
                f"Valor do Fipe: {self._valorFipe}\n" \
                f"Valor da Diaria: {self._valorDiaria}\n" \
                f"Categoria da CNH necessaria: {self._categoriaCNHNecessaria}\n" \
                f"Alugado: {'Sim' if self._alugado else 'Não'}\n" \
                f"-----------------------------------------\n"
        
class VeiculoNacional(Veiculo):
    codigo_veiculo_Estatico = 0
    def __init__(self,nomeModelo,montadora,anoFabricacao,anoModelo,placa,categoria,valorFipe,valorDiaria,categoriaCNHNecessaria,alugado,taxaImpostoEstadual,codigoVeiculo = None):
        if codigoVeiculo == None:
            super().__init__(VeiculoNacional.codigo_veiculo_Estatico,nomeModelo,montadora,anoFabricacao,anoModelo,placa,categoria,valorFipe,valorDiaria,categoriaCNHNecessaria,alugado)
            self._taxaImpostoEstadual = taxaImpostoEstadual
        else:
            super().__init__(codigoVeiculo, nomeModelo, montadora, anoFabricacao, anoModelo,placa, categoria, valorFipe, valorDiaria, categoriaCNHNecessaria, alugado)
            self._taxaImpostoEstadual = taxaImpostoEstadual
    
    @property
    def taxaImpostoEstadual(self):
        return self._taxaImpostoEstadual
    
    @taxaImpostoEstadual.setter
    def taxaImpostoEstadual(self,taxaImpostoEstadual):
        self._taxaImpostoEstadual = taxaImpostoEstadual

    def calcularValorMedia(self):
        return
    def calcularValorDiaria(self):
        return self._valorDiaria+self._valorDiaria*self._taxaImpostoEstadual

    def __str__(self):
        return  f"-----------------------------------------\n"\
                f"Código do Veículo: {self._codigoVeiculo}\n" \
                f"Nome do Modelo: {self._nomeModelo}\n" \
                f"Montadora: {self._montadora}\n" \
                f"Ano de Fabricação: {self._anoFabricacao}\n" \
                f"Ano do Modelo: {self._anoModelo}\n" \
                f"Placa: {self._placa}\n" \
                f"Categoria: {self._categoria}\n" \
                f"Valor FIPE: R${self._valorFipe:.2f}\n" \
                f"Valor da Diária: R${self._valorDiaria:.2f}\n" \
                f"Categoria CNH Necessária: {self._categoriaCNHNecessaria}\n" \
                f"Alugado: {'Sim' if self._alugado else 'Não'}\n" \
                f"Taxa de Imposto Estadual: {self._taxaImpostoEstadual}%\n" \
                f"-----------------------------------------\n"


    def setCodigoVeiculo(self, numero):
        self.codigo_veiculo_Estatico = numero


    def getCodigoVeiculo(self):
        return self.codigo_veiculo_Estatico
        
class VeiculoImportado(Veiculo):
    codigo_veiculo_Estatico = 0
    def __init__(self,nomeModelo,montadora,anoFabricacao,anoModelo,placa,categoria,valorFipe,valorDiaria,categoriaCNHNecessaria,alugado,taxaImpostoEstadual,taxaImpostoFederal,codigoVeiculo=None):
        if codigoVeiculo == None:
            super().__init__(VeiculoImportado.codigo_veiculo_Estatico,nomeModelo, montadora, anoFabricacao, anoModelo, placa, categoria, valorFipe, valorDiaria,categoriaCNHNecessaria, alugado)
            self._taxaImpostoEstadual = taxaImpostoEstadual
            self._taxaImpostoFederal = taxaImpostoFederal
        else:
            super().__init__(codigoVeiculo, nomeModelo, montadora, anoFabricacao, anoModelo,
                             placa, categoria, valorFipe, valorDiaria, categoriaCNHNecessaria,alugado)
            self._taxaImpostoEstadual = taxaImpostoEstadual
            self._taxaImpostoFederal = taxaImpostoFederal

    @property
    def taxaImpostoEstadual(self):
        return self._taxaImpostoEstadual
    
    @taxaImpostoEstadual.setter
    def taxaImpostoEstadual(self,taxaImpostoEstadual):
        self._taxaImpostoEstadual = taxaImpostoEstadual
    
    @property
    def taxaImpostoFederal(self):
        return self._taxaImpostoFederal
    
    @taxaImpostoFederal.setter
    def taxaImpostoFederal(self,taxaImpostoFederal):
        self._taxaImpostoFederal = taxaImpostoFederal

    def calcularValorMedia(self):
        return

    def calcularValorDiaria(self):
        return self._valorDiaria+self._valorDiaria*self._taxaImpostoEstadual+self._valorDiaria*self._taxaImpostoFederal

    def __str__(self):
        return  f"-----------------------------------------\n"\
                f"Código do Veículo: {self._codigoVeiculo}\n" \
                f"Nome do Modelo: {self._nomeModelo}\n" \
                f"Montadora: {self._montadora}\n" \
                f"Ano de Fabricação: {self._anoFabricacao}\n" \
                f"Ano do Modelo: {self._anoModelo}\n" \
                f"Placa: {self._placa}\n" \
                f"Categoria: {self._categoria}\n" \
                f"Valor FIPE: R${self._valorFipe:.2f}\n" \
                f"Valor da Diária: R${self._valorDiaria:.2f}\n" \
                f"Categoria CNH Necessária: {self._categoriaCNHNecessaria}\n" \
                f"Alugado: {'Sim' if self._alugado else 'Não'}\n" \
                f"Taxa de Imposto Estadual: {self._taxaImpostoEstadual}%\n" \
                f"Taxa de Imposto Federal: {self._taxaImpostoFederal}%\n" \
                f"-----------------------------------------\n"


    def setCodigoVeiculo(self,numero):
        self.codigo_veiculo_Estatico = numero


    def getCodigoVeiculo(self):
        return self.codigo_veiculo_Estatico