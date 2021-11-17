import csv

def readRoster():
  with open('Roster.csv', 'r') as f:
    file = csv.reader(f)
    my_list = list(file)
  print(my_list)
  returned_list = []
  for x in my_list:
    x = str(x)
    x = x.replace("['", "")
    x = x.replace("']", "")
    returned_list.append(x)
  return returned_list