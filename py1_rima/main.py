print("Bienvenido")

archivo = open ('palabras500.csv', encoding = "utf-8")
lineas = archivo.readlines()
archivo.close()


def buscar_rimas (rima):
  for i in range(499):
    palabra = lineas[i]
    a = rima in palabra 
    if a == True:
      n_ult=len(rima)
      b = tuple(range(-1,-n_ult-1,-1))
      c= min(b)
      d= max(b)
      algo = palabra[c-1:d]
      e = rima in algo
      if e == True:
        print (palabra)

rima=input("Ingrese la palabra que quiere (rimar)")
print(" ")

buscar_rimas(rima)