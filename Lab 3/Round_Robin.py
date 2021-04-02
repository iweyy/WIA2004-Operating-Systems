noOfJob=int(input("Enter number of job: "))
quantumTime=int(input("Enter Quantum Time: "))
arrivalTime=list(range(noOfJob))
cpuCycle=list(range(noOfJob))
for i in range(noOfJob):
    print("Enter Arrival Time and CPU Cycle for Job ",i+1)
    arrivalTime[i]=int(input("Arrival Time: "))
    cpuCycle[i]=int(input("CPU Cycle: "))