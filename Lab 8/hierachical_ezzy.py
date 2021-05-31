class Node():
    def __init__(self, parent, file):
        self.parent = parent
        self.file = file
        self.path = []

    def getFileName(self):
        return str(self.file)

    def addFile(self, file):
        node = Node(self, file)
        self.path.append(node)

    def getParent(self):
        return self.parent

    def getPath(self, index):
        return self.path[index]

    def printPath(self):
        for file in self.path:
            print(file.getFileName())

    def printTree(self, level):
        if (level == 0):
            print("Directory List: ")
        for i in range(level):
            print("-|", end="")
        print(self.getFileName())
        if len(self.path) != 0:
            for file in self.path:
                file.printTree(level+1)

    def findFile(self, file):
        for file in self.path:
            if (file.getFileName() == file):
                return file

        return -1


def printDirectory(node):
    path = ''
    temp = node
    while (temp.getFileName() != "\\"):
        path = temp.getFileName() + "\\" + path
        temp = temp.getParent()

    path = "\\" + path
    print(path, end=">")


root = Node(None, "\\")
currFolder = root

while True:
    printDirectory(currFolder)

    cmd = [word for word in input().split()]
    arguments = len(cmd)
    if arguments == 1:
        command = cmd[0]
    elif arguments == 2:
        command = cmd[0]
        fileName = str(cmd[1])
    else:
        print("Please enter the right command")
        continue

    if (command == "cd" and arguments == 2):
        if fileName == ".." and currFolder != root:
            currFolder = currFolder.getParent()
        elif fileName == ".." and currFolder == root:
            print("In root")
        else:
            if (currFolder.findFile(fileName) == -1):
                print(f"\"{fileName}\" not found")
            else:
                currFolder = currFolder.findFile(fileName)
    elif (command == "mkdir" and arguments == 2):
        currFolder.addFile(fileName)
    elif (command == "mkfile" and arguments == 2):
        currFolder.addFile(fileName)
    elif(command == "dir"):
        currFolder.printPath()
    elif (command == "tree"):
        root.printTree(0)
    elif (command == "exit"):
        root.printTree(0)
        print("Exited")
        break
    else:
        print("Please enter the right command")
        continue
