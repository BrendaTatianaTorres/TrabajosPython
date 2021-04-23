def tabla (numero1, numero2):
  for i in range(1,numero2+1,1):
    multi = numero1*i
    print (numero1, '*' ,i, '=' , multi)
  
numero1 = input ('Escriba el número del que quiere ver la tabla ')
numero2 = input ('Escriba el número hasta el que quiere ver la tabla ')  
numero1=int(numero1)
numero2=int(numero2)
tabla(numero1,numero2)