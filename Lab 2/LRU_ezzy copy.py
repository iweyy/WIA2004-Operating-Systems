# initialize number of pages that memory can hold
capacity = 4

# initialize number of pages to be sent into memory
set = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 9]
# set = [8, 2, 7, 4, 8, 6, 3, 5, 3, 1, 0, 7, 5, 9, 6]

# initialize memory slots
memory = {}


# define least recently used algorithm
def LRU():

    # initialize page faults and page hits
    pageFaults = 0
    pageHits = 0
    index = 1

    # algorithm runs until set is empty
    for i in set:

        # if page in set does not exist in memory
        if i not in memory:

            # if length of memory does not reach intended capacity
            if index <= 4:

                # add page from set into memory
                memory[index] = i
                index += 1

            # if length of memory reaches intended capacity
            else:

                # remove least recently used page in memory and add page from set into memory according to the index
                memory[2] = memory[1]
                memory[3] = memory[2]
                memory[4] = memory[3]
                memory[1] = i

            # increment page fault by 1
            pageFaults += 1

        # if page in set exists in memory
        else:

            # remove least recently used page in memory and add page from set into memory according to the index
            memory[2] = memory[1]
            memory[3] = memory[2]
            memory[4] = memory[3]
            memory[1] = i

            # increment page hit by 1
            pageHits += 1

        # print memory, page faults and page hits onto output
        print('Set:', memory)
        print('Page faults:', pageFaults)
        print('Page hits:', pageHits, '\n')


# print output
print('LRU Page Replacement Algorithm:')
LRU()
