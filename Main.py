import Banco_de_dados, Usuario, Locacoes


locacao1 = Locacoes.Locacao(0, 1, "07/09/2023", "11/09/2023", 100.00, "Credito", "Nenhum", True)
funcionario1 = Usuario.Funcionario("João Silva", "123.456.789-00", "12345-6", "01/01/1990", "Rua das Flores, 123", "12345-678", "joao@email.com", 3500.0, "12345678901", "15/03/2015")
funcionario2 = Usuario.Funcionario("Maria Souza", "987.654.321-00", "54321-0", "15/05/1985", "Avenida Principal, 456", "98765-432", "maria@email.com", 4200.0, "98765432109", "10/07/2018")
funcionario3 = Usuario.Funcionario("Carlos Oliveira", "111.222.333-44", "78901-2", "20/11/1978", "Praça Central, 789", "11111-222", "carlos@email.com", 5000.0, "11122233344", "03/02/2021")


Banco_de_dados.BancodeDados.criarFuncionario(funcionario1)
Banco_de_dados.BancodeDados.criarFuncionario(funcionario2)
Banco_de_dados.BancodeDados.criarFuncionario(funcionario3)

Banco_de_dados.BancodeDados.criarLocacao(locacao1)
locacaoAux = Banco_de_dados.BancodeDados.recuperarLocacao(0)

print(locacaoAux)
