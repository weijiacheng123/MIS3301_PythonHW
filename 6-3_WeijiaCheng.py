def main():
    f = open('numbers.txt','r')
    count = 0
    num = f.readline()
    while num != "":
        num = float(num.rstrip())
        count += num
        num = f.readline()
    print("The average is:",count)

main()
