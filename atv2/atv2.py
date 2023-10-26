#1
nome = input("Digite seu nome: ")
print("Seja bem-vindo", nome)


#2
numero = input("Digite um número: ")
numero = int(numero)
print("Você digitou o número:", numero)


#3
peso = float(input("Digite seu peso (em quilogramas): "))
altura = float(input("Digite sua altura (em metros): "))
imc = peso / (altura ** 2)
print("Seu IMC é:", imc)
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Seu peso está dentro da faixa saudável.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")