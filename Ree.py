import random


def run():
    print("------Investment------")
    name_c = input("Write the name of your new coin: ")
    random_numb = str(random.randint(0, 10000))
    print(name_c + " currently costs " + random_numb)
    inv = input("How much money will you invest in " + name_c + "?: ")
    inv = int(inv)

    print("Let's see what happend with " + name_c)
    print(str(name_c + " up " + + "%"))
if __name__ == "__main__":
    run()