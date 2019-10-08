#create a program that will allow you to enter events organizable by hour. There must be menu options of some form, and you must be able to easily edit, add, and delete events without directly changing the source code.
#(note that by menu i dont necessarily mean gui. as long as you can easily access the different options and receive prompts and instructions telling you how to use the program, it will probably be fine)

events = {}

def addEvent():
    hour = input("Please enter time of the event:")
    name = input("Please enter name of the event:")
    events[hour] = name

    next = input("Do you want to add next event? (y) for yes, (n) for no")

    if next == 'y':
        addEvent()
    else:
        print("Thank you")
        mainMenu()

def editEvent():
    hour = input("Please enter time of the event:")
    if hour in events.keys():
        name = input("Please enter updated name of the event:")
        events[hour] = name
        print("Thank you!")
        mainMenu()
    elif hour not in events.keys():
        print("Event for that hour does not exist. Please choose another hour")
        editEvent()

def removeEvent():
    hour = input("Please enter time of the event you want to remove:")
    if hour in events:
        del events[hour]
    else:
        print("There is no such event")

def viewEvent():
    print(events)
    enteredName = input("Please provide name of event you want to show:")
    for hour, name in events.items():
        if enteredName == name:
            print(hour)
            next = input("Do you want to see next event?")
            if next == "y":
                viewEvent()
            else:
                mainMenu()
        else:
            print("There is no such event")
            viewEvent()


def mainMenu():
    print("""This is aplication for organizing events. Please choose what action you want to do from below:
    [1] Add new event
    [2] Edit existing event
    [3] Remove event
    [4] View event
    [5] Exit program""")

    choice = int(input("Please type position of action you want to take:"))

    if choice == 1:
        addEvent()
    elif choice == 2:
        editEvent()
    elif choice == 3:
        removeEvent()
    elif choice == 4:
        viewEvent()
    elif choice == 5:
        exit()
    else:
        print("Please choose 1 to 5 from menu")

mainMenu()