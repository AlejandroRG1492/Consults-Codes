import csv


def readFile(ruta):
  with open(ruta,"r") as file:
    data = csv.reader(file,delimiter=",")
    header = next(data)
    

    tabla = []

    for row in data:
      datos = zip(header,row)
      diccionario = {key:value for key,value in datos}
      tabla.append(diccionario)   

  
  return tabla