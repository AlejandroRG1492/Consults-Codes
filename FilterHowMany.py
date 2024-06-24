
def cuantos (dic , columnName):

 
  diccionario = dic
  lista_data_Column = []

  
#se guarda el numero de categorias dentro de la columna buscada
  for lista in diccionario:
    for key, value in lista.items():
      if key == columnName:
        
        if value not in lista_data_Column:
          lista_data_Column.append(value)
        


        
  return lista_data_Column