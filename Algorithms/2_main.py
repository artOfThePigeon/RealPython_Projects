from random import randint
from timeit import repeat

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

def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
                 if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # display the name of the algorithm and the minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


ARRAY_LENGTH = 10000

if __name__ == "__main__":
    # generate an array of ARRAY_LENGTH items consisting of random integer values
    # between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # call the function using the name of the sorting algorithm and the array you just created
    run_sorting_algorithm(algorithm="bubble_sort", array=array)   

            
