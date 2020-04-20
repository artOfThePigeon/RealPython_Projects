def merge(left, right):
    #if the first array is empty, then nothing needs to be merged
    #and you can return the second array as the result
    if len(left) == 0:
        return right

    #if the second array is empty, then nothing needs to be merged,
    #and you can return the first array as the result
    if len(right) ==0:
        return left

    result = []
    index_left = index_right = 0

    #now go through both arrays until all the elements
    #make it into the resultant array
    while len(result) < len(left) + len(right):
        #the elements need to be sorted to add them to the resultant array, so you
        #need to decide whether to get the next element from the first or second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        #if you reach the end of either array, then you can add the remaining elements
        #from the other array to the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    #if the input array contains fewer than two elements, then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    #sort the array by recursively splitting the input into two equal halves, sorting
    #each half and merging them together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

from random import randint
from timeit import repeat


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
    run_sorting_algorithm(algorithm="merge_sort", array=array)   
    

