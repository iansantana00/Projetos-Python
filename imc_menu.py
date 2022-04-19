
from imc import Pessoa


def main():
    menu()


def menu():
    print("---------------------------------------------")
    print("CALCULADORA DE ÍNDICE DE MASSA CORPORAL (IMC)")
    print("---------------------------------------------")
    valores()


def valores():
    m = float(input("Digite o valor de sua massa(kg): "))
    h = float(input("Digite o valor de sua altura(m): "))

    pessoa1 = Pessoa(m, h)
    print(pessoa1.calcularIMC(m, h))

    imc = m / (h ** 2)

    if imc < 14.5:
        print("Você está com desnutrição")
    elif imc >= 14.5 and imc < 20:
        print("Você está abaixo do peso normal")
    elif imc >= 20 and imc < 24.9:
        print("Você está no peso normal")
    elif imc >= 24.9 and imc < 29.9:
        print("Você está com sobrepeso")
    elif imc >= 29.9 and imc < 30:
        print("Você está com obesidade")
    else:
        print("Você está com obesidade morbida")


if __name__ == "__main__":
    main()
