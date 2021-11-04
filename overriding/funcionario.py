class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumenta_salario(self):
        self.salario *= 1.05

    def __str__(self):
        return f"Funcionario {self.nome}, Salario {self.salario}"


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def aumenta_salario(self):
        self.salario *= 1.1

    def __str__(self):
        return f"Gerente {self.nome}, Salario {self.salario}"


class Programador(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def aumenta_salario(self):
        self.salario *= 1.2

    def __str__(self):
        return f"Programador {self.nome}, Salario {self.salario}"
