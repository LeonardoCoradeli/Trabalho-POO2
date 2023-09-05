import abc from ABC, abstractmethod

#Classe veiculos e seus atributos

class Veiculo(ABC):
    def __init__(self,nomeModelo,montadora,anoFabricacao,anoModelo,placa,categoria,valorFipe,valorDiaria,categoriaCNHNecessaria,alugado):
        self._codigoVeiculo = None
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
    
    @anoFabricacao.setter(self,anoFabricacao):
        self._anoFabricacao = anoFabricacao
    
    @property
    def anoModelo(self):
        return self._anoModelo
    
    @anoModelo.setter(self,anoModelo):
        self._anoModelo = anoModelo
    
    @property 
    def placa(self):
        return self._placa
        
    @placa.setter(self,placa):
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
    
    @abstratcmethod
    def calcularValorMedia(self):
        pass
    
    def bool estaAlugado(self):
        if self._alugado = True:
            return True
        if self._alugado = False:
            return False
            
    def alugar(self):
        if estaAlugado = False:
            self._alugado = True
        if estaAlugado = True:
            return "Já está alugado"
    
    def devolver(self):
        if estaAlugado = True:
            self._alugado = False
        if estaAlugado = False:
            return "O veiculo não foi alugado ainda"
    
    def __str__(self):
        return  f"Codigo Veiculo: {self._codigoVeiculo}\n" \
                f"Modelo: {self._nomeModelo}\n" \
                f"Montadora: {self._montadora}\n" \
                f"Ano Fabricação: {self._anoFabricacao}\n" \
                f"Ano do Modelo: {self._anoModelo}\n" \
                f"Placa: {self._placa}\n" \
                f"Categoria: {self._categoria}\n" \
                f"Valor do Fipe: {self._valorFipe}\n" \
                f"Valor da Diaria: {self._valorDiaria}\n" \
                f"Categoria da CNH necessaria: {self._categoriaCNHNecessaria}\n" \
                f"Alugado: {'Sim' if self._alugado else 'Não'}\n"
        
class VeiculoNacional(Veiculo):
    def __init__(self,nomeModelo,montadora,anoFabricacao,anoModelo,placa,categoria,valorFipe,valorDiaria,categoriaCNHNecessaria,alugado,taxaImpostoEstadual):
        super().__init__(nomeModelo,montadora,anoFabricacao,anoModelo,placa,categoria,valorFipe,valorDiaria,categoriaCNHNecessaria,alugado)
        self._taxaImpostoEstadual = taxaImpostoEstadual
    
    @property
    def taxaImpostoEstadual(self):
        return self._taxaImpostoEstadual
    
    @taxaImpostoEstadual.setter
    def taxaImpostoEstadual(self,taxaImpostoEstadual):
        self._taxaImpostoEstadual = taxaImpostoEstadual
    
    def calcularValorDiaria(self):
        return self._valorDiaria+self._valorDiaria*self._taxaImpostoEstadual
    
    def __str__(self):
        f"{super().__str__}\n" \
        f"Taxa de Imposto Estadual: {self._taxaImpostoEstadual}\n"
        
class VeiculoImportado(Veiculo):
    def __init__(self,nomeModelo,montadora,anoFabricacao,anoModelo,placa,categoria,valorFipe,valorDiaria,categoriaCNHNecessaria,alugado,taxaImpostoEstadual,taxaImpostoFederal):
    
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
    
    def calcularValorDiaria(self):
        return self._valorDiaria+self._valorDiaria*self._taxaImpostoEstadual+self._valorDiaria*self._taxaImpostoFederal
        
    def __str__(self):
        f"{super().__str__}\n" \
        f"Taxa de Imposto Estadual: {self._taxaImpostoEstadual}\n" \
        f"Taxa de Imposto Federal: {self._taxaImpostoFederal}\n" \
