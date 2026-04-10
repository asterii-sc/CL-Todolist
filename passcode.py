import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_FILE = os.path.join(BASE_DIR, "todos.json")

try:
    with open(TODO_FILE, "r") as file:
        todoList = json.load(file)
except FileNotFoundError:
    todoList = []
    
    
print('set a suitable password for your system.')
password = input('set your password:\n')

print("hello world!")

systemPass = input("please insert your password: ")

while systemPass != password:
    print("incorrect password. try again.")
    systemPass = input("please try a different password: ")

print(f"hello {systemPass}, welcome home.")

#this is the task loop. everything happens jnside this while loop


while True:

#main loop
    
    print("Choose your action for today.\n——————————————————————————\nenter 't' for to-do list\nenter 'c' for cool magic tricks\nenter 'x' to exit the program")

#main input   

    actionMain = input("enter your letter of choice: ")

    while actionMain not in ['t','c','x']:
        print("invalid command")
        actionMain = input("enter your letter of choice: ")
        
#to do list function        

    if actionMain == 't':
        print(f'hello {systemPass}, here is your to do list:\n')
        for i, todo in enumerate(todoList, start = 1):
            print(f'{i}. {todo}')
        print('\n')
        print('choose action for your todo list:\ntype "n" for new todo list item\ntype "d" to remove a todo list item\ntype "r" to return back to main menu\n')
        todoAction = input('todo list action: ')
        while todoAction not in ['n', 'd', 'r']:
            print('invalid. try again')
            todoAction = input('todo list action: ')
        if todoAction == 'n':
            newTodo = input('type in your task: ')
            todoList.append(str(newTodo))
            with open(TODO_FILE, "w") as file:
                json.dump(todoList, file)
        elif todoAction == 'd':
            todoCut = int(input('enter a number to delete: ')) - 1
            todoList.pop(todoCut)
            with open(TODO_FILE, "w") as file:
                json.dump(todoList, file)
        else:
            continue
                             
#event functions                
                
    elif actionMain == 'c':
        print('\nwanna see a cool magic trick?')
        playerNum = input('pick a number from 1 ~ 10:\n')
        while playerNum not in str([1,2,3,4,5,6,7,8,9,10]):
            print('thats not a number between 1 and 10! try again.')
            playerNum = input('pick a number from 1 ~ 10:\n')

        playerLetter = input('now pick a letter from A ~ Z:\n')
        while playerLetter not in ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            print('only pick uppercase letters from A~Z!')
            playerLetter = input('now pick a letter from A ~ Z:\n')

        print(f'did you think of the letter {playerLetter} and the number {playerNum}?')
        continue
    elif actionMain == 'x':
        print('thanks for stopping by :D')
        break

