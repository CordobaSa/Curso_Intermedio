def palindrome(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacia."
#Si la longitud del string cumple con ser mayor a cero el codigo sigue adelante, pero si no lo cumple manda el mensaje de error.
    return string == string[::-1]

print(palindrome(" ")) 