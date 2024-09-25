#prueba para github actions

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return f"{numero} es un número par."
    else:
        return f"{numero} es un número impar."

if __name__ == "__main__":
    numero = int(input("Introduce un número: "))
    print(verificar_par_impar(numero))
