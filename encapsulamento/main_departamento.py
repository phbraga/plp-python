from encapsulamento.departamento import Departamento

departamento = Departamento("Computacao", 0)

print(departamento.get_nome())
print(departamento)

# testando alteracao invalida
departamento.set_nome(None)
print(departamento)

departamento.set_nome("Ciencias da Computacao")
print(departamento)