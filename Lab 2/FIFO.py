pageFrame = list(range(4))
job = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

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
            print(job[i]," >> hit",pageFrame)
            hit += 1
    if (check == False):
        pageFrame[j] = job[i]
        print(job[i]," >> in",pageFrame)
        j += 1
        if(j >= len(pageFrame)):
            j = 0
        fault += 1

rat = hit/len(job)
print("Hit: ", hit, " Fault: ", fault, "Hit ratio: ", rat)
