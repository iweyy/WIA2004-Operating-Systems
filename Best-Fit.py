blockSize=[10,15,5,9,3]
jobSize=[1,4,7,12]
blockNew=list(range(len(jobSize)))
fragment=[]

print("After allocation (Best fit):")
print("Job Size\t Memory block size\t Fragment")

for i in range(len(jobSize)):
    low=9999
    for j in range(len(blockSize)):
        frag=blockSize[j]-jobSize[i]
        if frag>=0:
            if low>frag:
                low=frag
                blockNew[i]=blockSize[j]
    fragment.append(low)

for t in range(len(jobSize)):
    print(jobSize[t],"\t \t \t",blockNew[t],"\t \t \t \t \t",fragment[t])
