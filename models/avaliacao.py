class Avaliacao:
    def __init__(self, ouvinte, nota):
        self._ouvinte = ouvinte
        self._nota = nota
    
    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, valor):
        if not isinstance(valor, float):
            raise ValueError("A nota deve ser um float")
        if valor <1.0 or valor > 5.0:
            raise ValueError("Nota deve estar entre 1.0 e 5.0")
        self._nota = valor
    