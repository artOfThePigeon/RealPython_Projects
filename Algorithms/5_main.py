#compact implementation of quicksort

from timeit import repeat
from random import randint


def quicksort(array):
    #if the input array contains fewer than two elements, then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    #select your 'pivot' element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        #elements that are smaller than the pivot go to the 'low' list. Elements that
        #are larger than the pivot go to the high list. Elements that are equal to pivot go
        #to the 'same' list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    #the final result combines the sorted 'low' list with the 'same' list and the sorted 'high' list
    return quicksort(low) + same + quicksort(high)            

    #run this after each algorithm to time it. put the algo name in the "" at bottom



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
    run_sorting_algorithm(algorithm="quicksort", array=array)   
    

