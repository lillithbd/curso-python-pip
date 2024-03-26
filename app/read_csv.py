import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    
    #unir header y row
    for row in reader:
      iterable = zip(header, row)
      country_dict = dict(iterable)#{key: value for key, value in iterable}
      #print(country_dict)
      data.append(country_dict)
    return data
    

if __name__ == '__main__':
  #data = read_csv(r"C:\Users\Asus\GitProjects\curso-python-pip\app\data.csv")
  data = read_csv('data.csv')
  #data = read_csv.read_csv(r'C:\Users\Asus\GitProjects\curso-python-pip\app\data.csv')
  print(data[0])
  
    
    
    