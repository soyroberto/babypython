import sys
def collatz_conjecture(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    try:
        num = int(sys.argv[1])
        if num <= 0:
            print("El número debe ser entero positivo.")
        else:
            result_sequence = collatz_conjecture(num)
            print("Secuencia generada por la conjetura de Collatz:")
            print(result_sequence)
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero positivo.")

if __name__ == "__main__":
    main()
