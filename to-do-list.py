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
Task_list = []
def menu():

    print("1 to add to the list")
    print("2 to remove from list")
    print("3 to view list")
    print("4 to exit")
    ans=input("what is your choice: ")


    if ans== "1":
        add_list()

    if ans== "3":
        view_list()


    if ans== "2":
        remove_list()



    

def add_list():

    while True:
        new=input("please enter something for your list: ")
        Task_list.append(new)

        contin = input("press 1 to end, or press enter to continue: ")
        if contin == "1":
            return

def view_list():

   
       for i in Task_list:
        print(i)

def remove_list():

    for i in Task_list:
        print(i)

    while True:

        remove=input("please enter something you want to remove: ")
        Task_list.remove(remove)

        for i in Task_list:
             print(i)
       

        contin = input("press 1 to end, or press enter to continue: ")
        if contin == "1":
            return
           

def my_list():
    list=[]
    list.sort()

while True:
    menu()
    contin = input("press 4 to exit program, press enter to go back to main menu: ")
    if contin == "4":
        break



