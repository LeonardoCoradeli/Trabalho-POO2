import Banco_de_dados, Usuario, Locacoes, Veiculos

funcionario1 = Usuario.Funcionario("Ronas", '123', '1234', '20/10/2002', 'Rua. CLever', '696969', 'todos@email.com', 10, "2", "20/02/2010")
Banco_de_dados.BancodeDados.criarFuncionario(funcionario1)

Banco_de_dados.BancodeDados.atualizarFuncionario(0, nome='ROBERTO')
