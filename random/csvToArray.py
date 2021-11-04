import csv
with open('Roster.csv', 'r') as f:
  file = csv.reader(f)
  my_list = list(file)
print(my_list)