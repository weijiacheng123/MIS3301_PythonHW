# this program is calculates the multiplication of two numbers


def main():
    num1 = float(input("What is the first number? "))
    num2 = float(input("What is the second number? "))
    calc_multi(num1,num2)


def calc_multi(num1,num2):
    result = num1 * num2
    print("The result of",num1,"*",num2,"is",result)


main()
