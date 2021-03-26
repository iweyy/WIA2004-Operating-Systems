# initialize number of pages that memory can hold
capacity = 4

# initialize number of pages to be sent into memory
set = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

# initialize number of page slots in memory
memory = []


# define least recently used algorithm
def LRU():

    # initialize number of page faults and page hits
    pageFaults = 0
    pageHits = 0

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

                # remove first page in memory and add page from set into memory
                memory.remove(memory[0])
                memory.append(i)

            # increment page fault by 1 every time page in set does not exist in memory
            pageFaults += 1

        # if page in set exists in memory
        else:

            # remove existing page in memory and add new page from set into memory
            memory.remove(i)
            memory.append(i)

            # increment page hit by 1 every time page in set already exists in memory
            pageHits += 1

        # print memory, page faults and page hits onto output
        print('Set:', memory)
        print('Page faults:', pageFaults)
        print('Page hits:', pageHits, '\n')


# print output
print('LRU Page Replacement Algorithm:')
LRU()
