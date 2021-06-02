class pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def printar(self):
        print(f"O nome é {self.nome}, o sobrenome é {self.sobrenome}, a idade é {self.idade}")

a = pessoa ('Rafael', 'Freitas', 24)
a.printar()
    
