
def cuantos (dic , columnName):

 
  diccionario = dic
  total=0
  lista_data_Column = []
  suma_data_column = []

  
#se guarda el numero de categorias dentro de la columna buscada
  for lista in diccionario:
    for key, value in lista.items():
      if key == columnName:
        
        if value not in lista_data_Column:
          lista_data_Column.append(value)
        total += 1

# buscar cuantas veces se repite cada categoria
  for i in lista_data_Column:
    Contar = sum(1 for x in diccionario if x[columnName] == i)
    suma_data_column.append(Contar)
  

# se crea tupla para retornar las veces que se repite cada categoria.
  Union = list(zip(lista_data_Column,suma_data_column))

  for i in Union:
    for categoria in lista_data_Column:
      if i[0] == categoria:
        print(f'{round(i[1]/total,2)*100} % of employees or {i[1]} employees,  belongs to the category of {categoria} {columnName}')
        
  return Union , lista_data_Column , suma_data_column