valor_1 = int(input("Ingrese el primer número: "))
valor_2 = int(input("Ingrese el segundo numero:"))

diferncia = abs(valor_1 - valor_2)

if diferncia % 2 == 0:

  print (" suma de los valores:", valor_1 + valor_2)
elif diferncia < 10 and diferncia in [2,3,5,7]:
  print("El resultado es: ", valor_1 * valor_2)
if diferncia % 10 == 4:
  print ("Los digitos son: ", valor_1, valor_2)