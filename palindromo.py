def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")

    if len(texto) <= 1:
        return True

    if texto[0] != texto[-1]:
        return False

    return es_palindromo(texto[1:-1])

palabra = input("Ingrese una palabra: ")

if es_palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")