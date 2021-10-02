
def main():
    
    A = ['Sam','Eric','Don','Glenn','Jaeki','Melissa','Fred','Jannette','Maria']
    B = ['Sara','Eliza','Sam','Glenn','Maria','Alex']
    count = 0
    C = []
    for name in B:
        if name in A:
            count += 1
            C.append(name)
    print(C)
    print("There are",count,"students in list C.")

main()
