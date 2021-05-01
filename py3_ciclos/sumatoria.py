A=[2,4,6,8]
B=[1,3,5,7]
C=[9,7,6,4]


def  sumatoria (A,B,C):
  n = len(A)
  sumar= 0
  for i in range(n):
    mult = A[i]*B[i]
    suma = mult + C[i]
    sumar = sumar + suma
  resultado = sumar+n**2
  print (resultado)
  print('\n')

print('\n')
print('A continuacion verá el resultado de la sumatoria propuesta, siendo A =', A, ' B =', B,'y C =', C )
print('\n')
sumatoria(A,B,C)