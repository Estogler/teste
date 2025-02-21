class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu temho {self.idade} anos.")

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

p1 = Pessoa("kaua", 19, 77, 1.75)
p1.apresentar()
print(f"meu imc é {p1.calcular_imc():.2f}")