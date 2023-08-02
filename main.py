class Animal:
    def __init__(self, name):
        self.name = name

    def hacer_sonido(self):
        pass

    def comer(self):
        pass

    def dormir(self):
        print(f'{self.name} está durmiendo')


class Perro(Animal):
    def __init__(self, name):
        super().__init__(name)

    def hacer_sonido(self):
        print(f'{self.name} está ladrando')

    def comer(self):
        print(f'{self.name} está comiendo')


class Gato(Animal):
    def __init__(self, name):
        super().__init__(name)

    def hacer_sonido(self):
        print(f'{self.name} está maullando')

    def comer(self):
        print(f'{self.name} está comiendo')


# Creamos los objetos
mi_perro = Perro('Firulais')
mi_gato = Gato('Garfield')

# Llamamos a los métodos
mi_perro.hacer_sonido()
mi_perro.comer()
mi_perro.dormir()

mi_gato.hacer_sonido()
mi_gato.comer()
mi_gato.dormir()
