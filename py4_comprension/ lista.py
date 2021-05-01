A = [2,4,6,8,1,1]
B = [1,3,5,7,9,2]

n = len(A)//2

C = [ A[i+1]**2*B[2*i]+B[n+i] for i  in range (n)]

print(type(lista))
print('C =', lista)
