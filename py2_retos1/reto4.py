print ('A continuación se le pedirán 2 números para calcular cual es mayor de los dos o si son iguales.')
a = input('Digite el primer número ')
b = input('Digite el segundo número ')

if a > b:
  print("El número mayor es",a)
if b > a:
  print("El número mayor es",b)
if a == b:
  print("Los números",a,'y',b,'son iguales')