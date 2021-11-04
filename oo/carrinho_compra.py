from item import Item

class CarrinhoCompra(object):

    def __init__(self, qtd_max_itens=200):
        self.__qtd_max_itens = qtd_max_itens
        self.__itens = []

    def get_qtd_max_itens(self):
        return self.__qtd_max_itens

    def get_itens(self):
        return self.__itens

    def mostrar_carrinho(self):
        for item in self.get_itens():
            print(item)

    def adicionar(self, produto, qtd):
        if len(self.get_itens()) < self.get_qtd_max_itens():
            item = Item(produto, qtd)
            if produto.get_qtd_estoque() >= qtd and qtd > 0:
                produto.set_qtd_estoque(produto.get_qtd_estoque() - qtd)
                self.get_itens().append(item)

    def remover(self, produto, qtd, atualizar_estoque=True):
        item = self.__busca_item(produto)
        if item is not None:
            qtd_remover = qtd if qtd <= item.get_qtd() else item.get_qtd()
            item.set_qtd(item.get_qtd() - qtd_remover)
            if atualizar_estoque:
                produto.set_qtd_estoque(produto.get_qtd_estoque() + qtd_remover)

            if item.get_qtd() == 0:
                self.get_itens().remove(item)

    def __busca_item(self, produto):
        for item in self.get_itens():
            if produto.get_id() == item.get_produto().get_id():
                return item

        return None

    def abandonar_carrinho(self, atualizar_estoque=True):
        for item in self.get_itens():
            self.remover(item.get_produto(), item.get_qtd(), atualizar_estoque)

    def calcula_preco(self):
        preco = 0
        for item in self.get_itens():
            preco += item.calcula_preco()

        print(f"Valor total da compra: R${preco:.2f}")

        return preco