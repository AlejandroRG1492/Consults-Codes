import Charts
import HowMany
import LeerCSV
import FilterHowMany

if __name__ == "__main__":
  tabla = LeerCSV.readFile("./HR_capstone_dataset.csv")



  #porcentaje de empleados que estan dentro o fuera de la compañia
  print("PERCENTAGE OF EMPLOYEE WHO LEFT (1) OR STAYED(0) IN THE COMPANY")
  Lista, xaxis , yaxis = HowMany.cuantos(tabla,'left')

  tabla = list(filter(lambda x: x["left"]== "0", tabla))


  # filtro por salarios y departamento
  print("COMPARATION BETWEEN SALARY AND DEPARTMENT")
  Categorias = FilterHowMany.cuantos(tabla, "salary")
  print(" ")

  for i in Categorias:
    
    tabla2 = list(filter(lambda x : x["salary"]== i, tabla))
    print("The employees that earn ", i, " salary are ", len(tabla2))
    print("From those ", len(tabla2), "it is found that:")
    Lista, xaxis , yaxis = HowMany.cuantos(tabla2,'Department')
    print(" ")


  
  # filtro por departamento y salarios
  print("COMPARATION BETWEEN DEPARTMENT AND SALARY")
  Categorias = FilterHowMany.cuantos(tabla, "Department")
  print(" ")

  for i in Categorias:

    tabla3 = list(filter(lambda x : x["Department"]== i, tabla))
    print("The employees in the area of ", i, " Department are ", len(tabla3))
    print("From those ", len(tabla3), "it is found that:")
    Lista, xaxis , yaxis = HowMany.cuantos(tabla3,'salary')
    print(" ")


  

  Lista, x , y = HowMany.cuantos(tabla,'salary')
  Charts.barChart(x, y)
  
  
  
  


  


