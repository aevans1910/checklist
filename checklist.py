checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)
#Create
def create(item):
    checklist.append(item)

#Read
def read(index):
    return checklist[index]
    
checklist = ['Blue', 'Orange']
checklist[1] = 'Cats'
print (checklist)