from heranca.cachorro import Cachorro, CachorroAdestrado

cachorro = Cachorro("Bob", "Pastor Alemao")
cachorro_adestrado = CachorroAdestrado("Logan", "Pitbull")

print(cachorro)
print(cachorro_adestrado)

cachorro.latir()
cachorro.domir()
cachorro.comer()

cachorro_adestrado.latir()
cachorro_adestrado.domir()
cachorro_adestrado.comer()
cachorro_adestrado.deitar()
cachorro_adestrado.rolar()
cachorro_adestrado.fingir_de_morto()
