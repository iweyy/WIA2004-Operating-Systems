arrivalTime=[0,0,0,0]
cpuCycle=[8,4,9,5]
temp_cc=[]
n=len(cpuCycle)
qt=4
jobDone=[]
wt=[]
tt=[]
count=time=flag=waitingTime=turnAroundTime=0
remain=n    # indicate when can exit while loop
seq=" "
for i in cpuCycle:
    temp_cc.append(i)   # update cpu cycle

while remain!=0:
    if temp_cc[count]<=qt and temp_cc[count]>0:
        time+=temp_cc[count]
        temp_cc[count]=0
        flag=1  # indicate the Job is done
        seq+="->P"+str((count+1))
        print("Job P"+str(count+1)," is coming in and done")
    elif temp_cc[count]>0:
        temp_cc[count]-=qt
        time+=qt
        seq+="->P"+str((count+1))
        print("Job P"+str(count+1)," is coming in")
    if temp_cc[count]==0 and flag==1:
        remain-=1
        jobDone.append(count+1)
        wt.append(time-arrivalTime[count])
        tt.append(time-arrivalTime[count]-cpuCycle[count])
        waitingTime+=time-arrivalTime[count]-cpuCycle[count]
        turnAroundTime+=time-arrivalTime[count]
        flag=0
    if count==n-1:
        count=0 # check for another loop
    elif arrivalTime[count+1]<=time:
        count+=1     
    else:
        count=0
    print(seq)

print("Job \t waiting time \t turn around time")
for i in range(n):
    print("P",jobDone[i],"\t",wt[i],"\t \t ",tt[i])

print("average waiting time ",(waitingTime*1.0/n))
print("average turn around time ",(turnAroundTime*1.0/n))
print("sequence ",seq)
