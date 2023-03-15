#def read():
#    numbers = []
#    with open("./files/number.txt", "r", encoding="utf-8") as f:
#        for lines in f:
#            numbers.append(int(lines))
#    print(numbers)


def write():
    names = ["Santiago","Valentina","Carlos", "Vivi"]
    with open("./files/names.txt", "w", encoding="utf-8") as n:
        for name in names:
            n.write(name)
            n.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()