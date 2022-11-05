import csv
from statistics import mean

with open('task19.csv', newline='') as f:
    data = [row for row in csv.reader(f, delimiter=';')]
    
data = data[1::]
print(f"Cуммарное расстояние с 7 по 9 октября: {sum([int(item[3]) for item in list(filter(lambda x: 7 <= int(x[0].split()[0]) <= 9, data))])}\n"
      f"Cредняя масса груза из города Осинки: {mean([int(item[-1]) for item in list(filter(lambda x: x[1] == 'Осинки', data))])}\n"
      f"Cуммарный расход бензина с 1 по 3 октября: {sum([int(item[4]) for item in list(filter(lambda x: 1 <= int(x[0].split()[0]) <= 3, data))])}\n"
      f"Cредняя масса груза в город Березки: {mean([int(item[-1]) for item in list(filter(lambda x: x[2] == 'Березки', data))])}\n")
