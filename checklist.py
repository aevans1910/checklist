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

#Testing
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

test()
