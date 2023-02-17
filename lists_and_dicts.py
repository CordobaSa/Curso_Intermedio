def run():
#    squares = []
#    for i in range(1,101):
#        if i % 3 != 0:          
#            squares.append(i**2)

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