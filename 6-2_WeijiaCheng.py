import os
def main():
    f = open("coffee.txt","w")
    x = 'y'
    while x =='y':
        de = input("Enter the description for coffee: ")
        count = float(input("Enter the Quantity: "))

        f.write(de+" ")
        f.write(str(count)+'\n')

        x = input("Do you want to add more data?\nEnter y for yes: ")

    f.close()
    print("All data has been record")

    f = open("coffee.txt","r")
    de = f.readline()
    while de != "":
        de = de.rstrip('\n')
        q = de.split()[-1]
        de = de.split()[0:-1]
        des = ""
        for i in de:
            des = des + " " +i
        print("Description:",des)
        print("Quantity:",q)

        de = f.readline()

    f.close()

    s = input("Do you want to search?\nEnter y for yes ")
    while s == 'y':
        f = open("coffee.txt","r")
        f2 = open("temp.txt","w+")
        s2 = input("Enter the description you want to find: ")
        found = False
        de = f.readline()
        while de != "":
            de = de.rstrip('\n')
            q = de.split()[-1]
            de = de.split()[0:-1]
            des = ""
            for i in de:
                des = des + " " +i
            if s2 in des:
                print("The description is:",des)
                print("The Quantity is:",q)
                found = True
                a = input("If you want to remove it, enter r\nIf you want to update it, enter u: ")
                if a == "r":
                    print("It has been removed")
                elif a == 'u':
                    newq = float(input("Please enter a new quantity: "))
                    f2.write(des+' ')
                    f2.write(str(newq)+"\n")
                    print("The quantity has been updated")
                else:
                    f2.write(des+' ')
                    f2.write(str(q) + '\n')
            else:
                f2.write(des+' ')
                f2.write(str(q) + '\n')
            de = f.readline()
            
        if not found:
            print("We did not find it")
        s = input("Do you want to search more?\nEnter y for yes ")
        f.close()
        f2.close()
        os.remove('coffee.txt')
        os.rename('temp.txt', 'coffee.txt')
        

main()
