def bisiesto (allo):

    a = allo%400
    b = allo%100
    c = allo%4

    if a == 0 or b == 0 or c == 0 :
      print ('El año es bisiesto.')
    else: 
      print ('El año es bisiesto.')

allo = input('Ingrese el número ') 
allo = int(allo)         
bisiesto(allo)
  
  