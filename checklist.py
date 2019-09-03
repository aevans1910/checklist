#I would like to thank Ben Laferty for helping me with many of the steps in this, Jess 
# Trin for helping me with user input errors, and Jess for helping me get unblocked from bugs

checklist = list ()

#Create
def create(item):
    checklist.append(item)

#Read
def read(index):
    return checklist[index]

#Update
def update(index, item):
    checklist[index] = item

#Destroy
def destroy (index):
    checklist.pop(index)

#User input
def user_input(prompt):
    #the input function will display a message in the 
    #terminal and wait for user input
    user_input = input (prompt)
    return user_input

#List all items in list
def list_all_items():
    index = 0
    for list_item in checklist:
        print ("{} {}".format(index, list_item))
        index += 1

#Marks items as completed
def mark_completed():  
    for list_item in checklist:
        print ("√ {}".format(list_item))

#Uncheck items
def unmark_completed(item):
    index = 0
    for list_item in checklist:
        print ("{} {}".format(index, list_item))
        index += 1

#Select
def select(function_code):
    function_code = function_code.upper()

    #Create item
    if function_code == "A":
        input_item = user_input ("Input item:")
        create(input_item)

    #Update
    elif function_code == "U":
        update_index =  user_input("Index Number? ")
        updated_item = user_input("New item name: ")
        update(int(update_index), updated_item)

    #Read item
    elif function_code == "R":
        item_index = user_input("Index number? ")
        item = read(int(item_index))  
        print(item)
 
    #Unmarking items
    elif function_code == "C":
        checked_index = user_input("Index number? ")
        unmark_completed(checked_index)

    #Print all items
    elif function_code == "P":
        list_all_items()

    #Destroy items
    elif function_code == "D":
       select_index = user_input("Index number? ")
       destroy (int(select_index))

    #Quitting
    elif function_code == "Q":
        return False

    #Catch all
    else:
        print("Unknown Option")

    return True

running = True
while running:
    selection = user_input(
        "Press A to add to list, U to update items, R to read from list, C to uncheck items off the list, P to display list, D to delete items and Q to quit")
    running = select(selection) 
    mark_completed()

# Test function.  Not needed except for testing.


# def test():
#     # Create
#     create("purple sox")
#     create("red cloak")

#     print(read(0))
#     print(read(1))

#     # Update and destroy
#     update(0, "purple socks")
#     destroy(1)
#     print(read(0))

#     print(read(1))

#     # testing marking complete and incomplete
#     print(mark_completed(0))
#     print(read(0))
#     print(unmark_completed(0))
#     print(read(0))

#     # testing select
#     select("A")
#     select("U")
#     select("R")
#     select("C")
#     select("P")
#     select("D")
#     select("Q")

# test()
