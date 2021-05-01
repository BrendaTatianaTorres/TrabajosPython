A = ['cama', 'ropa', 'color', 'cafe', 'almohada']

n=len(A)
for i in range(n):
    palabra = A[i]
    rima = [palabra[i] for i in range (n) if 'a' in palabra[-1]] 
print (rima)



      