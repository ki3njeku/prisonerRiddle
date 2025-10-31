import secrets

BOXES = 100
box_object = []
def create_boxes(): #Creates the bexes with a random number inside them
    i = 1
    slip_array = list(range(1,BOXES + 1))
    while i <= BOXES:
        slip_choice = secrets.choice(slip_array)
        box_object.append((i, slip_choice))
        slip_array.remove(slip_choice)
        i +=1

def follow_number(number, limit): #The method which Veritasium proposed to navigate the riddle
    current_focus = number #Number is the prisoners number which as suggested is the first box to open
    j = 1
    while True:
        current_focus = box_object[current_focus - 1][1]
        j += 1
        if box_object[current_focus - 1][1] == number: #If the slip with the prisoner's number is found
            return True
        if j >= limit: #If the limit of the number of tries is reached
            return False
        
def statistic_check(prisoner_number): #To run the experiment once with this number of prisoners
    prisoners = list(range(1,prisoner_number + 1))
    for prisoner in prisoners:
        survived = follow_number(prisoner, prisoner_number / 2)
        if not survived: #If one person doesn't find their slip, the whole crew of prisoners dies
            return False

successes = 0
for l in range(10000):
    create_boxes()
    check = statistic_check(BOXES)
    if check != False:
        successes += 1
    box_object.clear()
print(f'{successes/100}% success rate')