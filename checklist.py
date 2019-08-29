#Create
def create(item):
    checklist.append(item)

#Read
def read(index):
    return checklist[index]

checklist = []

#Update
def update(index, item):
    checklist[index] = item

#Destroy
def destroy (index):
    checklist.pop(index)

#List all items in list
def list_all_items():
    index = 0
    for list_item in checklist:
        print ("{} {}".format(index, list_item))
        index += 1

#Marks items as completed
def mark_completed():  
    index = 0  
    for list_item in checklist:
        print ("√ {}".format(list_item))
        index += 1

#User input
def user_input(prompt):
    #the input function will display a message in the 
    #terminal and wait for user input
    user_input = input (prompt)
    return user_input

#Select
def select (function_code):
    #Create item
    if function_code == "C":
        input_item = user_input ("Input item:")
        create(input_item)

    #Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        read(item_index)

    #Print all items
    elif function_code == "P":
        list_all_items()

    #Catch all
    else:
        print("Unknown Option")

        



#Testing
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    
    list_all_items()

    mark_completed()

    select("C")
    list_all_items()
    select("R")
    list_all_items()

test()

