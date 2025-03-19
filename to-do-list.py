"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: to-do-list.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#title
print("welcome to your to do list!") 

def menu():

    print("1 to add to the list")
    print("2 to remove from list")
    print("3 to view list")
    print("4 to exit")
    ans=input("what is your choice")


    if ans== "1":
        add_list()

def add_list():

    while True:
        new=input("please enter something for your list")
        list.append(new)

        contin = input("continue?: ")
        if contin == "a":
            return








def my_list():
    list=[]
    list.sort()





