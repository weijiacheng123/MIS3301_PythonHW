# Start
# ask temperature

temp = float(input("what is the substance’s temperature? "))
#temp >= 102.5
while temp >= 102.5:
    print("The temperature is too high.")
    print("Turn the thermostat down and wait 5 minutes.")
    print("Then take the temperature again and enter it in the system.")
    temp = float(input("what is the substance’s temperature? "))
    
    


#'The temperature is too high.'
#'Turn the thermostat down and wait 5 minutes.'
#'Then take the temperature again and enter it in the system.’
