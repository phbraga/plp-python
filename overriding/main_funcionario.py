from funcionario import Funcionario, Gerente, Programador

funcionario = Funcionario("Lenildo", 4000)
gerente = Gerente("Sharles", 7000)
programador = Programador("Silas", 6800)

print(funcionario)
print(gerente)
print(programador)

funcionario.aumenta_salario()
gerente.aumenta_salario()
programador.aumenta_salario()

print(funcionario)
print(gerente)
print(programador)