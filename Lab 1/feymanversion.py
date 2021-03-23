block_size = [100,500,200,300,600]
process_size = [212,417,112,526]

def firstfit(blocksize,processsize):
    #show early state
    print("\nfirst fit:")
    print("Process No.\tProcess Size\tBlock no.")
    #check for each process size
    for x in processsize:
        #reset block status
        flag = 0
        #check for each current block size
        for y in blocksize:
            #check block status
            if flag == 1:
                #pass the code
                continue
            #check first fit
            if int(x)<=int(y):
                #update block size
                print (str(processsize.index(x)+1)+"\t\t"+str(x)+"\t\t"+str(blocksize.index(y)+1))
                #update current block size
                blocksize[blocksize.index(y)] = y-x
                #update status for done block
                flag = 1
        #processsize doesnt fit into any block size
        if flag==0:
            print(str(processsize.index(x)+1)+"\t\t"+str(x)+"\t\tnot allocated")

def bestfit(blocksize,processsize):
    #show early state
    print("\nbest fit:")
    print("Process No.\tProcess Size\tBlock no.")
    #check for each process size
    for x in processsize:
        #reset minimum block size
        mini = 9999999
        #check for each current block size
        for y in blocksize:
            #check whether processsize fit into blocksize
            if int(x)<=int(y):
                #check whether blocksize is smaller than minimum value
                if int(y)< mini:
                    #update minimum value
                    mini = y              
        #check if having a minimum block size to fit in
        if mini!=9999999:
            #print output
            print (str(processsize.index(x)+1)+"\t\t"+str(x)+"\t\t"+str(blocksize.index(mini)+1))
            #update current block size
            blocksize[blocksize.index(mini)] = mini-x
        #if there are no other option to choose
        else:
            print(str(processsize.index(x)+1)+"\t\t"+str(x)+"\t\tnot allocated")

#runcode here
print("block size:\t"+ str(block_size))
print("process size:\t"+ str(process_size))        
firstfit(block_size,process_size)  
#bestfit(block_size,process_size)  