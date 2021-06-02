from time import sleep 
senha = "3210"
usuario = "Rafael"
contador = 0
digusuario = input("Digite o nome do usuário: ").capitalize()


while digusuario != usuario:
    contador += 1
    print (contador)
    if contador == 3:
        print ("As suas tentativas esgotaram!")
        sleep(3)
        exit()   
    print ("Usuário não encontrado, digite novamente!")
    digusuario = input("Digite o nome do usuário: ").capitalize()
    

digsenha = input ("digite a senha: ")
contador = 0

while digsenha != senha:
    contador += 1
    print (contador)
    if contador == 3:
        print ("As suas tentativas esgotaram!")
        sleep(3)
        exit()
    print ("Senha incorreta digite novamente!!! ")
    digsenha = input ("digite a senha: ")

    
    
print ("BEM VINDO AO BANCO DOS BANCOS!")


class conta():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def sacar(self):
        valorsaq = int(input(f"{self.titular}, digite o valor que deseja sacar: "))
        saque = self.saldo - valorsaq
        self.saldo = saque
        print (f"{self.titular} fez o saque no valor de {valorsaq}, restando sua conta o saldo: R$ {saque}")


    def dep(self):
        valordep = int(input(f"{self.titular}, digite o valor que deseja depositar: "))
        dep = self.saldo + valordep
        self.saldo = dep
        print (f"{self.titular} fez o depósito no valor de {valordep},  o seu saldo agora é: R$ {dep}")
        sleep(3)

    def sald(self):
        print(f"O seu saldo é de R${self.saldo}.")

a = conta ("Rafael", 5000)
a.sald()
a.sacar ()
a.dep ()


        


    
    