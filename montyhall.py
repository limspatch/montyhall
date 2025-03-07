# Python
# Monty Hall's Paradox
import random

car_or_goat = ['car', 'goat', 'goat']

Monty_Hall_is_right = 0

# Type number of runs
try:
    num = int(input("Enter number of runs:"))
except ValueError:
    print("Invalid input")

# 3 doors: your choice, door 1, door 2 
your_choice, door1, door2 = '', '', ''

for _ in range(num):
    random.shuffle(car_or_goat)

    # Suppose that you have selected the first door.
    your_choice = car_or_goat[0]
    door1 = car_or_goat[1]
    door2 = car_or_goat[2]

    # Get index of the door where goat behind
    # If there is two goats behind door1, door2 -> just get the first door1 since car_or_goat is random shuffled.
    # Use set to filter out the door where goat behind
    goat_idx = [door1, door2].index('goat')
    goat_door = [door1, door2][goat_idx]
    changeable_door = list(set([door1, door2]) - set(goat_door))[0]

    # Change your door
    your_choice, changeable_door = changeable_door, your_choice
    
    # Count if the paradox is right
    if your_choice == 'car':
        Monty_Hall_is_right += 1

# Check validation
validation = Monty_Hall_is_right / num
print(f'Validation: {validation}')

# Enter number of runs:1000000
# Validation: 0.666159
