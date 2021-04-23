def palindromo (palabra):
  nletras = len(palabra) 
  invpalabra = palabra[::-1]
  a = invpalabra in palabra
  if a == True:
    print ('La palabra', palabra, 'es una palindromo')
  else:
    ('La palabra', palabra, 'no es un palindromo')

palabra = input('Ingrese la palabra ')
palindromo(palabra)