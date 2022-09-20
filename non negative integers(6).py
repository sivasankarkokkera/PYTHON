
def maxArea( A):
    l = 0
    r = len(A) -1
    area = 0
     
    while l < r:
        # Calculating the max area
        area = max(area, min(A[l],
                        A[r]) * (r - l))
     
        if A[l] < A[r]:
            l += 1
        else:
            r -= 1
    return area
 
# Driver code
a = [1, 5, 4, 3]
b = [3, 1, 2, 4, 5]
c = [1,8,6,2,5,4,8,3,7]
d = [1,1]
e = [7,3]
 
print(maxArea(a))
print(maxArea(b))
print(maxArea(c))
print(maxArea(d))
print(maxArea(e))
