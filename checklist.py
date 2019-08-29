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
    for list_item in checklist:
        print ("√ {}".format(list_item))

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

test()

