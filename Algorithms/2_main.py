def bubble_sort(array):
    n = len(array)

    for i in range(n):
        #start looking at each item of the list one by one, comparing it with
        #its adjacent value. With each iteration, the portion of the array that
        #that you look at shrinks because the remaining items have already beem sorted.
        for j in range(n - i - 1):
            #create a flag that will allow the function to terminate early if there's nothing
            #left to sort
            already_sorted = True

            if array[j] > array[j + 1]:
                # if the item you're looking at is greater than its
                # adjacent value then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                #since you had to swap two elements,
                #set the already_sorted flag to False so the
                #algorithm doesn't finish prematurely
                already_sorted = False

        #If there were no swaps during the last iteration,
        #the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array
            
