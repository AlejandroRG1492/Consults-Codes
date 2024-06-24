import matplotlib.pyplot as plt


def barChart(x,y):
  fig, ax = plt.subplots()
  ax.bar(x,y)
  plt.show()

def pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()