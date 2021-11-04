class Produto(object):

    def __init__(self, id, descricao, qtd_estoque, preco):
        self.__id = id
        self.__descricao = descricao
        self.__qtd_estoque = qtd_estoque
        self.__preco = preco

    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def get_qtd_estoque(self):
        return self.__qtd_estoque

    def get_preco(self):
        return self.__preco

    def set_id(self, id):
        self.__id = id

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_qtd_estoque(self, qtd_estoque):
        self.__qtd_estoque = qtd_estoque

    def set_preco(self, preco):
        self.__preco = preco