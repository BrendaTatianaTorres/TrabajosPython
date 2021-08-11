A = [2,4,6,8,1,1]
B = [1,3,5,7,9,9]
C = [4,5,6,9,2,3]

n = len(A)
n2 = n**2
x = sum(A[i]*B[i]+C[i] for i  in range (n))+n2
print (x)