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
    
    length = len(MyClassmates)
    index = 0
    MyClassmates[-1] = 'XXX'
    #print(MyClassmates)
    while index < length:
        print(MyClassmates[index])
        index += 1
        
    

        
main()
