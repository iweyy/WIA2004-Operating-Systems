# initialize number of pages that memory can hold
capacity = 4

# initialize number of pages to be sent into memory
set = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
#set = [8, 2, 7, 4, 8, 6, 3, 5, 3, 1, 0, 7, 5, 9, 6]

# intialize number of page slots in memory
memory = []


# define first in first out algorithm
def FIFO():

    # initialize page faults, page hits and index
    pageFaults = 0
    pageHits = 0
    index = 0

    # algorithm runs until set is empty
    for i in set:

        # if page in set does not exist in memory
        if i not in memory:

            # if length of memory does not reach intended capacity
            if len(memory) < capacity:

                # add page from set into memory
                memory.append(i)

            # if length of memory reaches intended capacity
            else:

                # remove page in memory and add page from set into memory according to current index
                memory.remove(memory[index])
                memory.insert(index, i)

                # increment index by 1
                index += 1

            # increment page fault by 1 every time page in set does not exist in memory
            pageFaults += 1

        # if page in set exist in memory
        else:

            # increment page hit every time page in set already exists in memory
            pageHits += 1

        # revert index to 0 if index is above 3
        if index > 3:
            index = 0

        # print memory, page faults and page hits onto output
        print('Set:', memory)
        print('Page faults:', pageFaults)
        print('Page hits:', pageHits, '\n')


# print output
print('FIFO Page Replacement Algorithm:')
FIFO()
