#run this after each algorithm to time it. put the algo name in the "" at bottom

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
    run_sorting_algorithm(algorithm="", array=array)   
    
