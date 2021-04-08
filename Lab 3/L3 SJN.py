CPUcycle = [7,5,4,1]
CPU = []*len(CPUcycle)
ID = []*len(CPUcycle)
index = 0
total =0

#search the smallest cycle to run in CPU
for i in range (len(CPUcycle)):
    
    #print table
    print("\nprocess ID   Burst time")
    for a in range(len(CPUcycle)):
        print("     ", (a+1),"          ",CPUcycle[a])


    minimum = 1000

    for x in range (len(CPUcycle)):
        if CPUcycle[x] == 0:
            continue

        elif CPUcycle[x] < minimum:
            minimum = CPUcycle[x]
            index = x
            
        else :
            continue
        
    CPUcycle[index] = 0
    if minimum == 1000:
        break
    else:
        ID.append(index+1)
        CPU.append(minimum)
        print("\nProcess ID = ",str(ID))
        print("burst time = ",str(CPU))

#print table
print("\nprocess ID   Burst time")
for a in range(len(CPUcycle)):
    print("     ", (a+1),"          ",CPUcycle[a])

tem = []

for i in CPU:
    tem.append(i)
    for j in tem:
        total = total+j
  
print("The average turnaround time is : ", (total / len(CPU)))
