import threading
import time



class Semaphore():
    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())       # to avoid concurrence
        self.value = initial                                    

    def up(self):
        with self.lock:
             self.value += 1         #increment by 1
             self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1         #decrement by 1

class Fork():
    def __init__(self, number):
        self.number = number           # Fork's number
        self.user = -1                 # keep track of philosopher using it
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):         # used for synchronization
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            print("Philosopher[%s] took Fork[%s]" % (user, self.number))
            self.lock.notifyAll()

    def drop(self, user):         # used for synchronization
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            print("Philosopher[%s] dropped Fork[%s]" % (user, self.number))
            print("Philosopher[%s] THINKING" % (user))
            self.lock.notifyAll()

class Philosopher (threading.Thread):
    def __init__(self, number, left, right, waiter):
        threading.Thread.__init__(self) # call Thread library
        self.number = number            # philosopher number
        self.left = left
        self.right = right
        self.waiter = waiter            

    def run(self):
        
        time.sleep(1)
        self.waiter.down()              # start service by waiter
        # think
        time.sleep(1)                 
        self.left.take(self.number)     # pickup left Fork
        time.sleep(1)      # (yield makes deadlock more likely)
        self.right.take(self.number)    # pickup right Fork
        # eat
        time.sleep(1)                
        print("Philosopher[%s] EATING" % (self.number))
        self.right.drop(self.number)    # drop right Fork
        time.sleep(1)
        self.left.drop(self.number)     # drop left Fork
        time.sleep(1)
        self.waiter.up()              # end service by waiter
        time.sleep(1)
        print("Philosopher[%s] finished THINKING & EATING" % self.number)

def dinner():
    # number of philosophers / fork
    n = int(input('Enter Total Philosophers : '))
    print("\n")
    # waiter for deadlock avoidance (n-1 available)
    waiter = Semaphore(n-1)
    # list of Forks
    f = [Fork(i) for i in range(n)]
    # list of philsophers
    p = [Philosopher(i, f[i], f[(i+1)%n], waiter) for i in range(n)]

    for i in range(n):
        p[i].start()        # start the thread for each philosopher

dinner()