import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  #plt.savefig(f'./imgs/{name}.png') --De esta manera no está funcionando
  plt.savefig(r'C:\Users\Asus\GitProjects\curso-python-pip\app\imgs\Colombia.png')
  plt.close() 

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig('chart_pie_Final.png')
  plt.close() 

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 200, 300]
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
