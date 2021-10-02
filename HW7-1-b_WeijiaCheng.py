def main():
    MyClassmates = []
    
    again = 'y'

    while again == 'y':
        name = input("What is your first name? ")
        F_name = [name]
        MyClassmates += F_name
        print("Do you want ro add another name? ")
        again = input("y = yes,otherwise = no ")
        print()
        
    #print("Here are the names you entered. ")
    #print(MyClassmates)
    for name in MyClassmates:
        print(name)

        
main()
