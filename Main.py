import GUI
import Locadora
from Banco_de_dados import BancodeDados
from Locacoes import Locacao,Seguro
from Usuario import Cliente, Funcionario
from Veiculos import VeiculoNacional, VeiculoImportado

if __name__ == '__main__':
    #Abre uma tela na primeira vez
    dados = GUI.tela.telaInicial()
    locadora = Locadora.Locadora(dados[0], dados[1], dados[2], dados[3])

    #Recupera os dados do banco de dados sobre o numero de itens
    Locacao.setEstatico_codigoLocacao(BancodeDados.recuperarNumeroLocacoes())
    VeiculoNacional.setEstatico_codigoVeiculo(BancodeDados.recuperarNumeroVeiculosNacionais())
    VeiculoImportado.setEstatico_codigoVeiculo(BancodeDados.recuperarNumeroVeiculosImportados())
    Cliente.setEstatico_codigoCliente(BancodeDados.recuperarNumeroClientes())
    Funcionario.setEstatico_codigoFuncionario(BancodeDados.recuperarNumeroFuncionarios())
    Seguro.setEstatico_codigoSeguro(BancodeDados.recuperarNumeroSeguros())

    #Abre a tela principal
    tela = GUI.tela(locadora)

    #Roda a tela principal
    tela.rodando()

    #Salva o numero de itens no Banco de Dados, os itens em si ja foram salvos no momento da criação
    BancodeDados.salvarNumeroLocacoes(Locacao.getEstatico_codigoLocacao())
    BancodeDados.salvarNumeroVeiculosNacionais(VeiculoNacional.getEstatico_codigoVeiculo())
    BancodeDados.salvarNumeroVeiculosImportados(VeiculoImportado.getEstatico_codigoVeiculo())
    BancodeDados.salvarNumeroClientes(Cliente.getEstatico_codigoCliente())
    BancodeDados.salvarNumeroFuncionarios(Funcionario.getEstatico_codigoFuncionario())
    BancodeDados.salvarNumeroSeguros(Seguro.getEstatico_codigoSeguro())
