# Start
# asks the user to enter a temperature in Celsius degree
C = float(input("Please enter a temperature in Celsius degree: "))

# converts it to Fahrenheit degree
F = (C * 1.8) + 32

print("This temperature converts to Fahrenheit degree should be",F)

# If the temperature > 212 F
# display a message indicating that the temperature is above boiling water temperature. 
# If the temperature < 32 F
# display a message indicating that the temperature is below freezing temperature. 
if F > 212:    
    print("The temperature is above boiling water temperature.")
if F < 32:
    print("The temperature is below freezing temperature.")

# End
