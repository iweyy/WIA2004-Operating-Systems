# initialize number of pages to be sent into memory
# set = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 9]
set = [8, 2, 7, 4, 8, 6, 3, 5, 3, 1, 0, 7, 5, 9, 6]

# initialize number of pages that memory can hold
capacity = 4

# initialize memory slots and index slots
memory = []
index = []


# create least recently used algorithm
def LRU():

    # initialize page faults and page hits
    pageFaults = 0
    pageHits = 0

    # algorithm runs until set is empty
    for i in set:

        # print page from set
        print('Input page:', i)

        # if page in set does not exist in memory
        if i not in memory:

            # if length of memory has not reach intended capacity
            if len(memory) < capacity:

                # add page from set into memory
                memory.append(i)

                # add -1 into index
                index.append(-1)

                # increment all index by 1
                for j in range(len(index)):
                    index[j] += 1

            # if length of memory has reached intended capacity
            else:

                # page from memory with index of 3 (lru) is replaced by page from set
                memory[index.index(capacity-1)] = i

                for j in range(len(index)):

                    # increment all index by 1
                    index[j] += 1

                    # change index of most recently used page to 0
                    if index[j] == capacity:
                        index[j] = 0

            # increment page fault by 1 every time page in set does not exist in memory
            pageFaults += 1

        # if page in set exists in memory
        else:

            for j in range(len(index)):

                # increment index by 1 if index is lower than index of page from set
                if index[j] < index[memory.index(i)]:
                    index[j] += 1

            # change index of page from set to 0
            index[memory.index(i)] = 0

            # increment page hit by 1 every time page in set exists in memory
            pageHits += 1

        # print memory, index, page faults and page hits
        print('Set:', memory)
        print('Index:', index)
        print('Page faults:', pageFaults)
        print('Page hits:', pageHits, '\n')


# print output
print('LRU Page Replacement Algorithm:')
LRU()
