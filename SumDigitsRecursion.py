#Using recursion to find out the sum of digits of an N digit number 

sumDigits(1447)


def sumDigits(N):
    '''
    N: a non-negative integer
    returns, Integer: sum of digits of the number
    '''
    if N < 10:
        return N
    else:
         q = N // 10
         r = N % 10
         return r + sumDigits(q)
