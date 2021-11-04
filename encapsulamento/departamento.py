class Departamento:
    def __init__(self, nome, codigo):
        self.__nome = nome
        self.__codigo = codigo

    def get_nome(self):
        return self.__nome

    def get_codigo(self):
        return self.__codigo

    def set_nome(self, nome):
        if nome is not None and len(nome) > 0:
            self.__nome = nome
        else:
            print("Nao eh aceito nome None ou em branco")

    def set_codigo(self, codigo):
        if codigo >= 0:
            self.__codigo = codigo
        else:
            print("Soh eh aceito valores de codigo maiores que 0")

    def __str__(self):
        return f"Departamento {self.get_nome()} (codigo {self.get_codigo()})"
