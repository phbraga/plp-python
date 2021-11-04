from ponto2d import Ponto2D
from quadrado import Quadrado

p1 = Ponto2D(x=2, y=4)
print(p1)
p2 = Ponto2D(x=3, y=5)
print(p2)
print(p1 + p2)
dist = p1.distancia(p2)
print(dist)

q = Quadrado(lado=3)
print(q)
print(f"Area: {q.area()}")
print(f"Comprimento: {q.comprimento()}")