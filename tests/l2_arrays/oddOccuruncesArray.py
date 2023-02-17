###-------------- ODD OCCURENCES ARRAY -------------------------------###

# A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

# For example, in array A such that:
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the elements at indexes 0 and 2 have value 9,
# the elements at indexes 1 and 3 have value 3,
# the elements at indexes 4 and 6 have value 9,
# the element at index 5 has value 7 and is unpaired.
# Write a function:
# that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

# For example, given array A such that:
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the function should return 7, as explained in the example above.
# Write an efficient algorithm for the following assumptions:
# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.

def solution(A):
    # need to find the element that doesn't pair with another element
    # can put the array elements into a dict
    dict1 = {}

    N = len(A)

    if N == 1:
        return A[0]
        #print(A)

    else:
        # take the last element of the array and see if it is in the dict, if so delete the key from the dict, if not add it
        for i in range(N):
            last = A[-1]
            del A[-1]
            if last in dict1:
                del dict1[last]
            else:
                dict1[last] = 1
        
        res = list(dict1.keys())[0]
        return res

#--END-----------------------------------------------------------------------

#--TESTS---------------------------------------------------------------------

A1 = [1,1,3,4,3,4,5,6,7,6,7,8,8,9,9,100,100]
x = solution(A1)
print(x)

A2 = [42]
x = solution(A2)

print(x)
    

