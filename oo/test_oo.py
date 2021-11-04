from cliente import Cliente
from produto import Produto

produto1 = Produto(id=1, descricao="iphone 13", qtd_estoque=10, preco=9000)
produto2 = Produto(id=2, descricao="macbook pro M1", qtd_estoque=10, preco=28000)

nome = input("Informe o seu nome: ")
cpf = input("Informe o seu CPF: ")
endereco = input("Informe o seu endereco: ")

cliente = Cliente(nome, cpf, endereco)
cliente.pegar_carrinho()
cliente.get_carrinho().adicionar(produto=produto1, qtd=2)
cliente.get_carrinho().adicionar(produto=produto2, qtd=1)
cliente.get_carrinho().remover(produto=produto1, qtd=1)
cliente.comprar()


# carrinho = CarrinhoCompra()
#
# print('-------- ADD 1')
# carrinho.adicionar(produto1, 3)
# carrinho.mostrar_carrinho()
#
# print('-------- ADD 2')
# carrinho.adicionar(produto2, 7)
# carrinho.mostrar_carrinho()
#
# print('-------- REM 1')
# carrinho.remover(produto1, 2)
# carrinho.mostrar_carrinho()
#
# print('-------- REM 2')
# carrinho.remover(produto2, 10)
# carrinho.mostrar_carrinho()


