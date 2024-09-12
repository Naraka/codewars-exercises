def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  return a / b

operaciones = {
  "sumar": sumar,
  "restar": restar,
  "multiplicar": multiplicar,
  "dividir": dividir
}

operacion = "sumar"
a = 5
b = 3

resultado = operaciones[operacion](a, b)
print(resultado)
