class A_Excep(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return "Error " + str(self.valor)

