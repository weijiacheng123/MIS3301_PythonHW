
def main():
    f = open('number.txt')
    line = f.readline()
    count = 0
    while line != "":
        line = f.readline()
        x = line.rstrip("\n").split(" ")
        if len(x)==1:
            break
        count += float(x[-1])
    print("the total time of videos is ",count)
main()

