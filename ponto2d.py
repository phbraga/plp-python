import math


class Ponto2D (object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Ponto2D(x=self.x + other.x,
                       y=self.y + other.y)

    def distancia(self, p_outro):
        x_dif = (self.x - p_outro.x) ** 2
        y_dif = (self.y - p_outro.y) ** 2

        return math.sqrt(x_dif + y_dif)
