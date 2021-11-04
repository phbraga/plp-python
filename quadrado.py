class Quadrado(object):

    def __init__(self, lado):
        self.lado = lado

    def __str__(self):
        return f"Quadrado de lado {self.lado}"

    def area(self):
        return self.lado ** 2

    def comprimento(self):
        return self.lado * 4
