class Conexoes:
    def __init__(self, parada) -> None:
        self.parada = parada
        self.next = None

    def __repr__(self):
        return self.parada

    def __str__(self):
        return self.__repr__