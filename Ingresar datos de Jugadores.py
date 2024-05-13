
def VerificarNumero(x,y):
  while True:
    resultado = x.isdigit()
    if resultado is True:
      break
    else:
      x = input(f"Ingrese un valor numerico para {y}: ")
  return x


datos = ["Nombre", "Apellido", "Edad"]
datosJugador = []
ListaJugadores = []


# se ingresa numero de jugadores verificando que sea numeros
jugadores = input("Ingrese el numero de jugadores: ")
numero = VerificarNumero(jugadores, str("numero de jugadores"))
jugadores = int(numero)

# se crean los datos de cada jugador

for n in range(jugadores):
  print("--------DATOS DEL JUGADOR # " + str(n+1))

  for i in datos:
    data = input("Introduce el " + i + ": ")
    
    #aqui solo se verifica que la edad sea numero
    if i == "Edad":
      edad = VerificarNumero(data, str("edad"))
      datosJugador.append(edad)   
      
    else:
      datosJugador.append(data)
  
  directorio = dict(zip(datos,datosJugador))
  ListaJugadores.insert(n,directorio)
  
  datosJugador = []

print(ListaJugadores)


