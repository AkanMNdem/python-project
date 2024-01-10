#B'day shooping list
#add item, remove item, show list, clear list, sort, quit program

shopping_list=[]

def add_item(item):
    shopping_list.append(item)
    print(f"Added {item} to shopping list")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"removed {item} from shopping list")
    else:
        print(f"{item} not found in list")

def show_list():
    print(shopping_list)

def clear_list():
    shopping_list.clear()
    print("Cleared shopping list", shopping_list)

def sort_list():
    shopping_list.sort()
    print("List sorted", show_list())

def list_of_commands():
    print("-add    : Adds and item to the list")
    print("-remove : Removes an item from the list")
    print("-show   : Prints the list")
    print("-clear  : Clears the list")
    print("-sort   : Sorts the list in ascending order")
    print("-quit   : Quit Program")
    print("-help   : Show available commands")
    print()

while True:
    user_input= input("Enter a command or type 'help for list of commands: ").lower()

# Check if the input is a non-integer
    if not user_input.isdigit():
        if user_input == "help":
            list_of_commands()
        elif user_input == "add":
            input_item = input("Enter item to add: ")
            add_item(input_item)
        elif user_input =="remove":
            input_item = input("Enter item to remove")
            remove_item(input_item)
        elif user_input=="show":
            show_list()
        elif user_input=="clear":
            clear_list()
        elif user_input=="sort":
            sort_list()
        elif user_input=="quit":
            break
        else:
            print("Invalid command, type 'help' for options")
    else:
        print("Invalid input. Please enter a non-integer value.")
