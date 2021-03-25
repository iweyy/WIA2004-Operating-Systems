block_size = [100,500,200,300,600]
process_size = [212,417,112,526]
def bestfit(blocksize,processsize):
    #show early state
    print("\nbest fit:")
    print("Process No.\tProcess Size\tBlock no.\tfragment")
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
            print (str(processsize.index(x)+1)+"\t\t"+str(x)+"\t\t"+str(blocksize.index(mini)+1)+"\t\t"+str(y-x))
            #update current block size
            blocksize[blocksize.index(mini)] = -1
        #if there are no other option to choose
        else:
            print(str(processsize.index(x)+1)+"\t\t"+str(x)+"\t\tnot allocated")

#runcode here
print("block size:\t"+ str(block_size))
print("process size:\t"+ str(process_size))        
bestfit(block_size,process_size)  