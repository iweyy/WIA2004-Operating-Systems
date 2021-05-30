maximum = 50
files = [0]*maximum
repeat = 1

while repeat == 1:
    start = int(input (f"Enter the starting block of the files (0-{maximum-1}): "))
    while start<0 or start>=maximum:
        if start>=maximum:
            print ("Exceed maximum number of file")
        if start<0:
            print ("Cannot be a negative number")
        start = int(input ("Enter the starting block of the files: "))

    length = int(input ("Enter the length of the files: "))
    while length<0 or length+start>maximum:
        if length+start>maximum:
            print ("Exceed maximum number of file")
        if length<0:
            print ("Cannot be less of equal; to 0")
        length = int(input ("Enter the length of the files: "))

    count = 0
    for i in range (length):
        if files[start+i] == 0:
            count += 1
    
    if count == length:
        for i in range (length):
            files[start+i] = 1
            print (f"files[{start+i}] = 1")
        print("The file is allocated to the disk")
    else:
        print("The file is not allocated to the disk")

    repeat = 3
    while repeat == 3:
        ans = input("Do you want to enter more files? (Yes/No): ")
        if (ans.lower() == "yes"):
            repeat = 1
        elif (ans.lower() == "no"):
            repeat = 0
        else:
            print("Invalid answer.")
            repeat = 3
print("Files Allocated are :")
for i in range (maximum):  
    print (f"files[{i}] = {files[i]}")