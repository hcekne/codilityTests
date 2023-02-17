# this is the cyclic rotation program

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
        print('this is the loop')
        print(i)

        # i was going the wrong way
        last = A[-1]
        del A[-1]
        A.insert(0,last)

        


    return A

    #return [] # this should be the cycled array
    #pass

A1 = [1,2,3,4,5,6,7]
K0 = 2

x = solution(A1, K0)
print(x)

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