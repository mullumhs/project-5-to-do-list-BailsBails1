"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use lists in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a list named favorite_foods and add at least five different food items to it
foods=["nachos","pizza","waffles","grapes","watermelon"]

# Change the third item in the list to a different food
foods[2]= "chocolate"

# Print out only the first and fourth items in the list
print(foods[0])
print(foods[3])
# Ask the user for a food item
new=input("please enter your favorite food: ")

# Append the user's food item to the list
foods.append(new)

# Print out the entire list of food items
for i in foods:
    print(i)