from conexoes import Conexoes

class Viagem:
    
    # CONSTRUTOR
    def __init__(self, id, origem, destino) -> None:
        self._id = id
        self._origem = origem
        self._destino = destino
        self.inicio = None
        self._size = 0

    # ID
    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    # ORIGEM
    def getOrigem(self):
        return self._origem
    
    def setOrigem(self, origem):
        self._origem = origem

    # DESTINO
    def getDestino(self):
        return self._destino
    
    def setDestino(self, destino):
        self._destino = destino

    # MÉTODOS
    def adicionarParada(self, parada):
        if not self.inicio:
            self.inicio = Conexoes(parada)
        else:
            pos = self.inicio
            while pos.next:
                pos = pos.next
            pos.next = Conexoes(parada)
            
        self._size = self._size + 1

    def __len__(self):
        return self._size

    def __getItem__(self, index):
        pos = self.inicio
        for i in range(index):
            if pos:
                pos = pos.next

        return pos

    def __repr__(self):
        pass

    def __str__(self):
        itens = ''
        saida = f'Código: {self.getId()}\nOrigem: {self.getOrigem()}\nDestino: {self.getDestino()}\n'

        if(self._size == 1):
            saida = saida + 'Conexão: '
        else:
            saida = saida + 'Conexões: '

        pos = self.inicio
        cont = 0
        while pos:
            cont = cont + 1
            if(self._size == 1 or cont == self._size):
                itens = itens + str(pos.parada)
            else:
                itens = itens + str(pos.parada) + ' => '
            pos = pos.next
        saida = saida + itens

        return saida