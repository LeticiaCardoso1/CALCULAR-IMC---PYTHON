def imc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso / (altura * 2)
    print(imc)
    if imc < 18.5:
        print("Baixo Peso")
    elif 18.5 <= imc < 25:
        print("Peso Adequado")
    elif 25 <= imc < 30:
        print("Sobrepeso")
    elif 30 <= imc < 35:
        print("Obesidade Grau 1")
    else:
        print("Obesidade Grau 2 ou maior")
        print(f"Seu Índice de Massa Corporal é: {imc}")

imc()
