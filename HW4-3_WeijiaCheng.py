

# calculate the energy consumed by a centrifuge
# speed should be multiplied by 10
# unique minimum and maximum speed
Min_speed = 15
Max_speed = 36
Increment = 5
Conversion_factor = 10

# print the heading
print('Speed\tEnergy')

# print the speed
for speed in range (Min_speed, Max_speed, Increment):
    energy = speed * Conversion_factor
    print (speed,'\t', energy)
    


#this is another way

#print('Speed\tEnergy')
#i = 0
#speed = 15

#for i in range (5):
    
    #energy = speed * 10
    #print (speed,'\t', energy)
    #i = i + 1
    #speed = speed + 5
