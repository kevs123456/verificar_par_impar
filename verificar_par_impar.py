def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f"{numero} es un número par."
    else:
        return f"{numero} es un número impar."

if __name__ == "__main__":
    while True:  # Bucle para seguir pidiendo un número
        try:
            numero = int(input("Introduce un número: "))
            print(verificar_par_impar(numero))
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Error: Debes introducir un número válido. Inténtalo de nuevo.")
            #v2
