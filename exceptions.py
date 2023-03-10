def divisors(num):
    divisors=[]
    for i in range(1,num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Put a number: "))
        if num < 0:
            raise ValueError("You can't put a number less than cero.")
        return print(divisors(num))
    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    run()