def run():
    #    squares = []
#    for i in range(1,101):
#        if i % 3 != 0:          
#            squares.append(i**2)

    #funciones_anonimas(lambda argumentos:expresion)
    #Ejemplo con palindromo

    palindrome = lambda string: string == string[::-1]
    print(palindrome("ana"))

    #filter(filtrar)

    my_list = [1,4,5,6,9,13,19,21]
    odd1 = list(filter(lambda x: x%2 != 0, my_list))
    #filtra los numeros que, dividos en 2 no sean iguales a cero(numero inpares)

    print(odd1)

    #map

    my_list = [1,2,3,4,5]
    odd2 = list(map(lambda x: x**2 , my_list))

    print(odd2)

    #reduce

    from functools import reduce
    #importar reduce de functools

    my_list = [2,2,2,2,2]
    all_multiplied = reduce(lambda a,b: a*b,my_list)
    #lambda lleva 2 parametros a y b, a como el primer item de nuestra lista y b como el segundo item, 
    #al multiplicar a por b, a recive el resultado de la multiplicacion mientras que b recive el siguiente
    #valor de la lista que seria el tercero.

    print(all_multiplied)

    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    
    print(squares)

    my_list = [1, "Hello", True, 4.5]
    my_dict = {"Firstname" : "Santiago", "Lastname" : "Cordoba"}

    super_list = [
        {"Firstname" : "Santiago", "Lastname" : "Cordoba"},
        {"Firstname" : "Jose", "Lastname" : "Rodol"},
        {"Firstname" : "Juan", "Lastname" : "Rodriguez"},
        {"Firstname" : "Camilo", "Lastname" : "Alvarez"},
        {"Firstname" : "Jorge", "Lastname" : "Amion"},
    ]

    for vars in super_list:
        for key, values in vars.items():
            print(key, values)

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.4],
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()