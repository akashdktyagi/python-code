
import numpy as np
import time

def add_list(size_of_list):
    l1 = list(range(size_of_list))
    l2 = list(range(size_of_list))
    l = [l1[i] + l2[i] for i in range(size_of_list)]
    return l

def add_ndarray(size_of_array):
    l1 = np.arange(size_of_array)
    l2 = np.arange(size_of_array)
    return l1 + l2

if __name__=="__main__":
    start_time = time.time()

    print(add_list(10000000))
    # print(add_ndarray(10000000))


    # Stop the timer
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    print(f"Time taken: {elapsed_time} seconds")