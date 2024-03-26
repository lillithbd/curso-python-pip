import utils
import read_csv
import charts
import pandas as pd

def run():
 '''
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
 '''  
  # df = pd.read_csv('C:\\Users\\Asus\\GitProjects\\curso-python-pip\\app\\data.csv')
  #(r'C:/Users/Asus/GitProjects/curso-python-pip/app/data.csv')
  #df = pd.read_csv('C:\\Users\\Asus\\GitProjects\\curso-python-pip\\app\\data.csv')
  df = pd.read_csv('data.csv', encoding='utf-8')
  df = df[df['Continent'] == 'Africa']
  
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)
  
  data = read_csv.read_csv('data.csv')
  #data = read_csv.read_csv(r"C:/Users/Asus/GitProjects/curso-python-pip/app/data.csv")
  #data = df.read_csv('data.csv', encoding='utf-8')
  country = input('Type Country => ')
  print(country)
  
  result = utils.population_by_country(data, country)
  
  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
       
#este if hace que si el modulo main es llamado  desde la terminal se ejecuta el método run por defecto
if __name__ == '__main__':
  run()