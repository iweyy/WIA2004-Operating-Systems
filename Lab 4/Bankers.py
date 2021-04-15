def test():
    allocation = [[0, 1, 0],[2, 0, 0],[3, 0, 2],[2, 1, 1] ,[0, 0, 2]]
    maximum = [[7, 5, 3],[3, 2, 2],[15,15,15],[2, 2, 2],[4, 3, 3]]
    available = [3, 3, 2]

    a = 5 #len alloc
    b = 3 #len alloc[]

    need = []
    place = [] #ans

    print ("max\t: "+str(maximum))
    print ("alloc\t: "+str(allocation))

    #calculate need value
    for i in range (a):
        temp = []
        for j in range (3):
            temp.append(maximum[i][j] - allocation[i][j])
        need.append(temp)

    print ("need\t: "+str(need),"\n")

    status =  [0]*a #job status
    for i in range (a):
        for j in range (a):
            if (status[j]==0):
                for k in range (b):
                    print("checking : "+str(need[j])+"\tavailable : "+str(available),end = "\t")
                    if(need[j][k] > available[k]):
                        print("status : larger than available")
                        break
                    place.append(maximum.index(maximum[j]))
                    print("status : update status & available value ->",end = "")
                    print(str(allocation[j])+" + "+str(available),end = "")
                    #update available
                    for l in range (b):
                        available[l] += allocation[j][l]
                    print (" = "+str(available))
                    status[j] =  1 #update status
                    break     
      
    if len(place) == a :
        print("Following is the SAFE Sequence") 
        for i in range(a):
            print(" P"+str(place[i])+" ->", end="") 
    else:
        print ("It is Unsafe state (not all process allocated) :") 
        for i in range(len(place)):
            print(" P"+str(place[i])+" ->", end="")                  
test()