
class Item(object):

    def __init__(self, produto, qtd):
        self.__produto = produto
        self.__qtd = qtd

    def calcula_preco(self):
        return self.get_qtd() * self.get_produto().get_preco()

    def get_produto(self):
        return self.__produto

    def get_qtd(self):
        return self.__qtd

    def set_produto(self, produto):
        self.__produto = produto

    def set_qtd(self, qtd):
        self.__qtd = qtd

    def __str__(self):
        return f"{self.get_qtd()} unidade(s) de {self.get_produto().get_descricao()}"