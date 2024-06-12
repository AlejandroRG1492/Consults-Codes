import matplotlib.pyplot as plt

def barChart(x,y):
  fig, ax = plt.subplots()
  ax.bar(x,y)
  plt.show()