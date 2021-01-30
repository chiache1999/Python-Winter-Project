import csv
with open("./example.csv",encoding="utf-8") as fh:
    data = csv.reader(fh,delimiter=',',doublequote = True)
    for row in data:
        print(','.join(row)) 
        print(len(row))