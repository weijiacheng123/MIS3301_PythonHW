# start
# ask for width1 and width2, length1 and length2
width1 = float(input("what is width1? "))
length1 = float(input("what is length1? "))
width2 = float(input("what is width2? "))
length2 = float(input("what is length2? "))

# the area of a rectangle is the rectangle’s length multiply by its width.
# calculate the area of each rectangular and display which rectangle has a greater area.
rec1_area = width1 *length1
rec2_area = width2 * length2

# display it if the areas are the same. 
# rec1 is bigger than rec2
# rec1 is as large as rec2
# rec1 is not bigger than rec2
if rec1_area > rec2_area or rec1_area == rec2_area:
    if rec1_area > rec2_area:
        rec1 = True
        if rec1:
            print("rec1 is bigger than rec2")
    else: 
    #if rec1_area == rec2_area:
        print("rec1 is as large as rec 2")
        
    
else:
    if rec1_area < rec2_area:
        #if rec1_area < rec2_area:
        rec1 = False
        #else:
            #rec1_area == rec2_area
            #print("rec1 is as large as rec 2")
        if rec1 == False:
            print("rec1 is not bigger than rec2")


#if rec1:
    #print("rec1 is bigger than rec2")
#else:
    #rec1_area == rec2_area
    #print("rec1 is as large as rec 2")
   

#if rec1 == False:
    #print("rec1 is not bigger than rec2")
#else:
    #rec1_area == rec2_area
    #print("rec1 is as large as rec 2")

# end
