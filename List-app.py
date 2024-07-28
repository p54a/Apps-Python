while True:
    ask = input("Hello, do you want to create a list? ")
    ask = ask.lower()

    if ask == "yes":
       list1 = []
       break
    elif ask == "no":
       print("Thanks, don't forget to visit as again.")
       exit()
    else:
       print("Please choose either yes or no.")

print("This is your list", list1)

while True:
    command = input("What do you want to do to your list: ")
    command = command.lower()
    
    if command == "add":
        try:
            where = int(input("Choose where do you want to add to your list from 0-" + str(len(list1)) + ": "))
        except ValueError:
            print("You need to choose a number between 0-" + str(len(list1)))
            continue
        
        add = input("What do you want to add: ")
        
        if where == 0:
            list1.insert(0, add)
            print(list1)
        elif where == False:
            print("You need to choose a pleace to add your item in.")
        elif where == len(list1):
            list1.append(add)
            print(list1)
        else:
            list1.insert(where, add)
            print(list1)
    elif command == "remove":
        print(list1)
        remove = input("What do you want to remove: ")
        list1.remove(remove)
    elif command == "reverse":
        list1.reverse()
        print(list1)
    elif command == "clear":
        list1.clear()
        print(list1)
    elif command == "sort":
        list1.sort()
        print(list1)
    else:
        print("Please choose either (add, remove, reverse, clear or sort)")
        print(list1)