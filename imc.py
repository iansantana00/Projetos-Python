
class Pessoa:

    def __init__(self, massa: float, altura: float) -> float:

        self.__massa: float = massa
        self.__altura: float = altura

    @property
    def massa(self):
        return self.__massa

    @massa.setter
    def massa(self, massa):
        self.__massa = massa

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def calcularIMC(self, massa, altura) -> float:
        return self.__massa / (self.__altura ** 2)
