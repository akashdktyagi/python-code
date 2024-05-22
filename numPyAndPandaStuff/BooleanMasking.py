
import numpy as np

if __name__=="__main__":
    arr1 = np.arange(9)
    print(arr1, arr1.shape)
    mat1 = arr1.reshape(3,3)
    print(mat1, mat1.shape)

    # students = np.array(["Alice", "Bob", "Charlie", "David", "Eve"])
    # math_scores = np.array([85, 91, 89, 92, 88])

    # mask = math_scores > 90
    #
    # result = students[mask]
    #
    # print(result)


    # arr_dat = np.random.rand(4, 2) # this is student
    # print(arr_dat)
    #
    # # user id from 0 to 3
    # arr_id = np.arange(4)  # this is maths score
    # print(arr_id)
    #
    # # pick data for user id 2
    # mask = arr_id == 2 # u created a mask
    # print(arr_dat[mask]) # u appled the mask on students
    #
    # # pick data for user id 0 and 3
    # print(arr_dat[(arr_id == 0)
    #               | (arr_id == 3)])

    # scores = np.array([[85, 91, 89, 92, 88], [78, 95, 88, 93, 85], [91, 88, 92, 85, 90]])
    #
    # # We create a Boolean mask where we check if the score is greater than 90
    # mask = scores > 90
    #
    # # We apply the mask to the scores array
    # high_scores = scores[mask]
    # high_scores.re
    #
    # print(high_scores)