import matplotlib.pyplot as plt
A = []

def llenar_A (num):
  
  while num != 1:
    A.append(num)
    par=num%2
    if par!=0:
      num=num*3
      num=num+1
    num=num//2
  return 0

def llenar_plot (A):  
  plt.plot(A)
  plt.show()

num = input ('Digite el primer número de la lista ')
num=int(num)
llenar_A(num)
llenar_plot(A)