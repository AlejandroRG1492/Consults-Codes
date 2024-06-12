import Charts
import HowMany
import LeerCSV

if __name__ == "__main__":
  tabla = LeerCSV.readFile("./HR_capstone_dataset.csv")
 
  
  Lista, xaxis , yaxis = HowMany.cuantos(tabla,'salary')
  print("""
  -------------------------------------------------------
  """)
  Lista, xaxis , yaxis = HowMany.cuantos(tabla,'Department')
  print("""
  -------------------------------------------------------
  """)
  Lista, xaxis , yaxis = HowMany.cuantos(tabla,'number_project')
  
  Charts.barChart(xaxis,yaxis)
  
  

