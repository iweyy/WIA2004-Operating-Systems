class Node:
    def __init__(self, parent, file):
        self.parent = parent
        self.file = file
        self.folders = {}
        self.files = []


class Directory():
    def __init__(self):
        self.root = Node(None, "C:")
        self.node = self.root

    def addFolder(self, folder):
        currNode = self.node
        if folder in currNode.folders:
            print('Folder already exists')
        else:
            currNode.folders[folder] = Node(currNode, folder)

    def addFile(self, file):
        currNode = self.node
        if file in currNode.files:
            print('File already exists')
        else:
            currNode.files.append(file)

    def printDirectory(self):
        if self.node == self.root:
            return 'C:'
        else:
            currNode = self.node
            path = []
            while currNode != self.root:
                path.append(currNode.file)
                currNode = currNode.parent
            path.append("C:")
            path.reverse()
            return "\\".join(path)

    def showContents(self):
        currNode = self.node
        showFolders = []
        showFiles = []

        if len(currNode.folders) == 0:
            print("No folders in this directory")
        else:
            for folder in currNode.folders:
                showFolders.append(folder)
            str = ', '.join(showFolders)
            print("Folders:", str)

        if len(currNode.files) == 0:
            print("No files in this directory")
        else:
            for file in currNode.files:
                showFiles.append(file)
            str = ', '.join(showFiles)
            print("Files:", str)

    def prevDirectory(self):
        if self.node == self.root:
            print("Already at root node")
        else:
            self.node = self.node.parent

    def changeDirectory(self, dir):
        currNode = self.node
        if dir in currNode.folders:
            self.node = currNode.folders[dir]
        else:
            print("Directory does not exist")


dir = Directory()

while True:

    print("Current Directory:", dir.printDirectory())
    print('What do you want to do in this directory?')
    print('1 - Create New Folder')
    print('2 - Create New File')
    print('3 - Show Directory Contents')
    print('4 - Change Directory')
    print('5 - Return to Previous Directory')
    print('Exit - End')
    cmd = input()

    if cmd == "1":
        folderName = input("Insert Folder Name: ")
        dir.addFolder(folderName)
    elif cmd == "2":
        fileName = input("Insert File Name: ")
        dir.addFile(fileName)
    elif cmd == "3":
        dir.showContents()
    elif cmd == '4':
        newDir = input('Insert Directory: ')
        dir.changeDirectory(newDir)
    elif cmd == "5":
        dir.prevDirectory()
    elif cmd.lower() == "exit":
        break
    else:
        print("Please enter the right command")

    print()
