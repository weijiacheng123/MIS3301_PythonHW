
def main():
    l = []
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    
    total = 0
    for i in range(1,13):
        x = int(input("Enter the rainfall for the month {}:".format(i)))
        l.append(x)
        total += x

    print("Total rainfall:",total)
    
    avg = total / 12
    print("Average rainfall:",avg)
    
    h = max(l)
    index_h = l.index(h)
    print("Highest rainfall:",months[index_h])
    
    
    low = min(l)
    index_l = l.index(low)
    print("Lowest rainfall:",months[index_l])
    
main()
