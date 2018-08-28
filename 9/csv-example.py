import csv

infilename = "dummy.csv"
infile = open(infilename)    # should check for problems using try-except

csvreader = csv.reader(infile)

for itemlist in csvreader:
    print("ITEMLIST: " + str(itemlist))

print(str(csvreader))

infile.close()
