import csv

def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

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
  #data = read_csv('./app/data.csv') de esta manera no lee el archivo
  data = read_csv(r'C:\Users\Asus\GitProjects\curso-python-pip\app\data.csv')
  print(data[0])
  
    
    
    