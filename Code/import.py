import csv
import GestionEquipement

gp = GestionEquipement
gp.newTables()


fname = "data/activite.csv"
file1 = open(fname, "r")

fname2 = "data/equipements.csv"
file2 = open(fname2, "r")

fname3 = "data/installations.csv"
file3 = open(fname3, "r")
 
try:
    reader = csv.reader(file1, delimiter=',', quotechar='"')
    for row in reader:
        gp.insertActivite(row[4], row[5])
        
    reader2 = csv.reader(file2, delimiter=',', quotechar='"')
    for row in reader2:
        gp.insertEquip(row[4], row[5], row[2])
        gp.insertEquipActiv()
        
    reader3 = csv.reader(file3, delimiter=',', quotechar='"')
    for row in reader3:
        gp.insertInstall(row[1],row[0],row[7],row[4],row[2],row[10],row[9])


finally:
    file1.close()
    file2.close()
    file3.close()



# import csv
# fname = "data/activite.csv"
# # file1 = open(fname, "r")

# # fname2 = "data/equipements.csv"
# # file2 = open(fname2, "r")

# # fname3 = "data/installations.csv"
# # file3 = open(fname3, "r")
 
# with open(fname, 'rt') as f:

#     reader = csv.reader(f, delimiter=',', quotechar='"')
#     for row in reader:
#         act = Activite(row[1], row[0])
#         print(act)

# f.close();
#     # reader2 = csv.reader(file2, delimiter=',', quotechar='"')
#     # for row in reader2:
#     #     print (row)
        
#     # reader3 = csv.reader(file3, delimiter=',', quotechar='"')
#     # for row in reader3:
#     #     print (row)
