def findMinSquares(n):

    T = [0] * (n + 1)
 
    for i in range(n + 1):
 
        T[i] = i
 
        j = 1
        while j*j <= i:

            T[i] = min(T[i], 1 + T[i - j*j])
            j += 1
 
    return T[n]
 
 
if __name__ == '__main__':
 
    n = 3
    print('The minimum number of squares is', findMinSquares(n))
