def concat (a, b):
  return a + ', ' + b

def input_concat():
  primeiro_parametro = str(input("Primeiro parametro: "))
  segundo_parametro = str(input("Segundo parametro: "))
  resultado = concat(primeiro_parametro, segundo_parametro)
  print(resultado)

input_concat()
