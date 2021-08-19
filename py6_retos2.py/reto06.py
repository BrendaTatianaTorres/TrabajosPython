import random
i=input("Presione enter")
n=random.randrange(1,121)
print("El número es:", n)

if 10<=n<=50:
  print("El número generado aleatoriamente se encuentra en el rango de [10,50]")
if 50<n<=100:
  print("El número generado aleatoriamente se encuentra en el rango de (50,100]")
if n>100:
  print("El número generado aleatoriamente es mayor a 100")
if n<10:
  print("El número generado aleatoriamente es menor a 10")