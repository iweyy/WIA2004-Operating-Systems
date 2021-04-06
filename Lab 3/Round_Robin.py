arrivalTime=[0,1,2,3]
burstTime=[8,4,9,5]
temp=[]
n=len(burstTime)
qt=4
jobDone=[]
wt=[]
tt=[]
count=time=remain=flag=waitingTime=turnAroundTime=0
remain=n
seq=" "
que=" "
for i in burstTime:
    temp.append(i)

while remain!=0:
    if temp[count]<=qt and temp[count]>0:
        time+=temp[count]
        temp[count]=0
        flag=1
        seq+="->P"+str((count+1))
    elif temp[count]>0:
        temp[count]-=qt
        time+=qt
        seq+="->P"+str((count+1))
    if temp[count]==0 and flag==1:
        remain-=1
        jobDone.append(count+1)
        wt.append(time-arrivalTime[count])
        tt.append(time-arrivalTime[count]-burstTime[count])
        waitingTime+=time-arrivalTime[count]-burstTime[count]
        turnAroundTime+=time-arrivalTime[count]
        flag=0
    if count==n-1:
        count=0
    elif arrivalTime[count+1]<=time:
        count+=1     
    else:
        count=0
    print(seq)

print("Job \t waiting time \t turn around time")
for i in range(n):
    print("P",jobDone[i],"\t",wt[i],"\t \t ",tt[i])
print("sequence ",seq)
print("average waiting time ",(waitingTime*1.0/n))
print("average turn around time ",(turnAroundTime*1.0/n))
