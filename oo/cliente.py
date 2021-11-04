from carrinho_compra import CarrinhoCompra


class Cliente(object):

    def __init__(self, nome, cpf, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__carrinho = None

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_endereco(self):
        return self.__endereco

    def get_carrinho(self):
        return self.__carrinho

    def pegar_carrinho(self):
        self.abandonar_carrinho()
        self.__carrinho = CarrinhoCompra()

    def abandonar_carrinho(self, atualizar_estoque=True):
        if self.get_carrinho() is not None:
            self.get_carrinho().abandonar_carrinho(atualizar_estoque)
            self.__carrinho = None

    def comprar(self):
        if self.get_carrinho() is not None:
            self.get_carrinho().calcula_preco()
            self.abandonar_carrinho(False)
            print("Volte sempre!")
