import csv

fname = "data/activites.csv"
file1 = open(fname, "r")

fname2 = "data/equipements.csv"
file2 = open(fname2, "r")

fname3 = "data/installations.csv"
file3 = open(fname3, "r")
 
try:
    reader = csv.reader(file1, delimiter=',')
    for row in reader:
        print (row)
    reader2 = csv.reader(file2)
    for row in reader2:
        print (row)
        
    reader3 = csv.reader(file3)
    for row in reader3:
        print (row)
finally:
    file1.close()
    file2.close()
    file3.close()