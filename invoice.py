# Para retornar o valor do Objeto criado deve utilizar o metodo @property no
# getteres e os objeto.setter nos setteres

class Invoice:

    def __init__(self, numeroItemFaturado: int, descricao: str,
                 quantidade: int, precoUnitario: float) -> None:
        self.__numeroIntemFaturado = numeroItemFaturado
        self.__descricao = descricao
        self.__quantidade = quantidade
        self.__precoUnitario = precoUnitario

    @property
    def InvoiceAmount(self):
        return self.__quantidade * self.__precoUnitario

    @property
    def NumeroItemFaturado(self):
        return self.__numeroIntemFaturado

    @NumeroItemFaturado.setter
    def NumeroItemFaturado(self):
        return self.__numeroIntemFaturado

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def Descricao(self, descricao):
        self.__descricao = descricao

    @property
    def Quantidade(self):
        return self.__quantidade

    @Quantidade.setter
    def Quantidade(self, quantidade):
        if quantidade < 0:
            self.__quantidade = 0
        else:
            self.__quantidade = quantidade

    @property
    def PrecoUnitario(self):
        return self.__precoUnitario

    @PrecoUnitario.setter
    def PrecoUnitario(self, precoUnitario):
        if precoUnitario < 0:
            self.__precoUnitario = 0
        else:
            self.__precoUnitario = precoUnitario

    def desconto(self, percentual):
        self.__precoUnitario = self.__precoUnitario - \
            (self.__precoUnitario * (percentual / 100))


invoice1 = Invoice(1, "mousepad", 10, 50.0)
print(invoice1.Descricao)
print(invoice1.__dict__)
invoice1.desconto(10)
print(invoice1.PrecoUnitario)
invoice2 = Invoice(2, "teclado", 15, 100.0)
print(invoice2.__dict__)
