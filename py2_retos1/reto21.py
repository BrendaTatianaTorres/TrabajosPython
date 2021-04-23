

def ICM (peso,estatura):
  estatura2 = estatura*estatura
  indice = peso/estatura2
  print ('Su índice de masa corporal es', indice)

peso = input('Ingrese su peso en kilogramos ')
estatura = input('Ingrese su estatura en metros ') 
peso = int(peso)
estatura = float(estatura)
ICM (peso,estatura)
