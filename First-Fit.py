blockSize=[100,500,200,300,600]
jobSize=[212,417,112,426]
fragment=[]
blockNew=[]

for i in range(len(jobSize)):
    for j in range(len(blockSize)):
        if blockSize[j]>=jobSize[i]:
            fragment.append((blockSize[j]-jobSize[i]))
            blockNew.append(blockSize[j])
            blockSize.remove(blockSize[j])
            break

print("After allocation (First fit): ")
print("Job size \t Memory block size \t Fragment")
for i in range(len(blockNew)):
    print(jobSize[i]," \t \t",blockNew[i]," \t \t \t \t",fragment[i])