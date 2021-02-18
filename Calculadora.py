class Calculadora():
    def __init__(self):
        self.funcoes = {
            "soma": self.soma,
            "subtracao": self.subtracao,
            "multiplicacao": self.multiplicacao,
            "divisao": self.divisao,
            "raiz_quadrada": self.raiz_quadrada,
            "porcentagem": self.porcentagem
        }

    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

    def multiplicacao(self, x, y):
        return x * y

    def divisao(self, x, y):
        return x / y

    def raiz_quadrada(self, x):
        return x ** (1 / 2)

    def porcentagem(self, x, y):
        return (x * y) / 100


if __name__ == '__main__':
    calculadora = Calculadora()
    resultado = calculadora.funcoes['raiz_quadrada'](169)
    print("resultado", resultado)
