import GUI
import Locadora
from Banco_de_dados import BancodeDados
from Locacoes import Locacao,Seguro
from Usuario import Cliente, Funcionario
from Veiculos import VeiculoNacional, VeiculoImportado
from Tela_inicial import telaInicial

if __name__ == '__main__':
    #Abre uma tela na primeira vez
    dados = telaInicial()
    locadora = Locadora.Locadora(dados[0], dados[1], dados[2], dados[3])


    #Abre a tela principal
    tela = GUI.tela(locadora)

    #Roda a tela principal
    tela.rodando()

