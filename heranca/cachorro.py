
class Cachorro (object):
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f"{self.nome}: Au au")

    def domir(self):
        print(f"{self.nome}: zzZZzzzZZZ")

    def comer(self):
        print(f"{self.nome}: Comendo....")

    def __str__(self):
        return f"<Cachorro> nome: {self.nome}, raca: {self.raca}, acoes: latir, dormir e comer"


class CachorroAdestrado (Cachorro):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def deitar(self):
        print(f"{self.nome}: Deitado!")

    def rolar(self):
        print(f"{self.nome}: Rolando!")

    def fingir_de_morto(self):
        print(f"{self.nome}: Morto!")

    def __str__(self):
        return f"{super().__str__()} | Ah, e eu sou adestrado! Sei deitar, rolar e fingir de morto"
