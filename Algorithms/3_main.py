def insertion_sort(array):
    #loop from the second element of the array until the last element
    for i in range(1, len(array)):
        #this is the element we want to position in its correct place
        key_item = array[i]

        #initialize the variable that will be used to find the correct
        #position of the element referenced by key_item
        j = i - 1

        #run through the list of item (the left portion of the array) and find
        #the correct position of the lement referenced by key_item. Do this only
        #if key_item is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            #shit the value one position to the left and reposition j to point to the
            #next element (from right of j)
            array[j + 1] = array[j]
            j -= 1

        #when you finish shifting element, you can position key_item in its correct location
        array[j + 1] = key_item

    return array

    
