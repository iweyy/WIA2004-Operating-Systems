pageFrame = list(range(2))
job = ['a', 'b', 'a', 'c', 'a', 'b', 'd', 'b', 'a', 'c', 'd']

for i in range(len(pageFrame)):
    pageFrame[i] = -1
hit = 0
fault = 0
j = 0

for i in range(len(job)):
    check = False
    for k in range(len(pageFrame)):
        if (pageFrame[k] == job[i]):
            check = True
            hit += 1
    if (check == False):
        pageFrame[j] = job[i]
        j += 1
        if(j >= len(pageFrame)):
            j = 0
        fault += 1

rat = hit/len(job)
print("Hit: ", hit, " Fault: ", fault, "Hit ratio: ", rat)
