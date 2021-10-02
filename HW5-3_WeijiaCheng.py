
# asks members for the amount of fat and carbohydrate (in grams)
# that they consumed in a day.

def main():
    fat = float(input('what is the fat? '))
    carb = float(input('what is the carbohydrate? '))
    calories_fat(fat)
    calories_carbs(carb)
    

# calculates calories that result from the fat
# calories_from_fat = fat × 9

def calories_fat(fat):
    calories_from_fat = fat * 9
    print("Your calories from fat is ",calories_from_fat)


# calculates calories that result from the carbohydrates
# calories_from_carbs = carb × 4

def calories_carbs(carb):
    calories_from_carbs = carb * 4
    print("Your calories from carbohydrate is ",calories_from_carbs)
    

main()
