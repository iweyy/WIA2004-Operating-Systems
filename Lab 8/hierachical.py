class Hierachical:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def PrintTree(self,level):
        for i in range(level):
            print('|_', end='')
        print('',self.value)
        if self.left:
            self.left.PrintTree(level+1)
        if self.right:
            self.right.PrintTree(level)


root = Hierachical("Root")
root.left = Hierachical("User 1")
root.left.right = Hierachical("User 2")
root.left.left = Hierachical("A")
root.left.left.right = Hierachical("B")
root.left.left.right.right = Hierachical("C")
root.left.left.right.right.left = Hierachical("F")
root.left.right.left = Hierachical("D")
root.left.right.left.right = Hierachical("E")

root.PrintTree(0)