A = [2,4,6,8,1,1]
B = [1,3,5,7,9,9]
C = []

def llenar_C (A,B):
  n = len(A)//2
  for i in range(n):
    Ai = A[i+1]**2
    Bi = B[2*i]
    mult = Ai*Bi
    suma = mult + B[n+i]
    C.append(suma)
  resultado = C
  print ('C =', resultado)
  print('\n')

print('\n')
print('A continuacion verá el resultado de el arreglo propuesto ')
llenar_C (A,B)