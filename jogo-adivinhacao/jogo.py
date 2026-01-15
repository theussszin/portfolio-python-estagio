import random

numero_secreto = random.randint(1, 10)
tentativa = 0

print("Adivinhe o número entre 1 e 10")

while tentativa != numero_secreto:
    tentativa = int(input("Digite um número: "))
    
    if tentativa < numero_secreto:
        print("Muito baixo!")
    elif tentativa > numero_secreto:
        print("Muito alto!")
    else:
        print("Parabéns! Você acertou 🎉")
