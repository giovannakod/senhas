import random

carct = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVDXYZ12345678910@"
comp = int(input("Digite o tamanho da senha:"))
senha = ""
for i in range(comp):
    senha += random.choice(carct)
print("Sua senha:", senha)
