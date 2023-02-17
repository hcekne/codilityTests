###--------------CYCLIC ROATION------------------------------------------###

# this is the cyclic rotation program

# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).
# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
# Write a function:
# def solution(A, K)
# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
# For example, given
#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given
#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]
# Given
#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]
# Assume that:
# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


#---START SOLUTION----------#

def solution(A, K):
    # Implement your solution here
    # given the one dimensional array of length N ra
    N = len(A)
    if N == 0:
        return A
    if K==0:
        return A
    if K%N == 0:
        return A
    
    if K > N:
        K = K - ((K // N) * N)
    
    for i in range(K):
        #print('this is the loop')
        #print(i)
        last = A[-1]
        del A[-1]
        A.insert(0,last)

    return A

    #pass
#---END-------------------------------

#---EXAMPLES

# A1 = [1,2,3,4,5,6,7]
# K0 = 2

# x = solution(A1, K0)
# print(x)

# x = solution(A1, K0)
# print('Example0')
# print(A1)
# print(K0)
# print(x)

# A1 = [1,4,5,6,7,8,9,10,5,3,2]
# K1 = 50 

# print(A1)
# print(K1)
# x = solution(A1, K1)
# print('Example1')
# print(x)


# A1 = [1,4,5,6,7,8,9,10,5,3,2]
# K2 = 3
# print(A1)
# print(K2)
# x = solution(A1, K2)
# print('Example2')

# print(x)

# A1 = [1,4,5,6,7,8,9,10,5,3,2]
# K3 = 0
# print(A1)
# print(K3)
# print('Example3')

# x = solution(A1, K3)
# print(x)
