from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_pro import suma_pro

def menu():
    print("Selecciona una opción:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma pro de una lista de números")
    print("6. Salir")

    while True:
        choice = input("Ingrese su opción (1-6): ")

        if choice == '1':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", sumar(a, b))
        elif choice == '2':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", restar(a, b))
        elif choice == '3':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", multiplicar(a, b))
        elif choice == '4':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", dividir(a, b))
        elif choice == '5':
            numeros = input("Ingrese los números separados por comas: ")
            numeros = [float(n) for n in numeros.split(",")]
            print("Resultado:", suma_pro(numeros))
        elif choice == '6':
            print("BYE...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
