import os
import csv

rootdir = 'C:\\Users\\lars\\OneDrive - Aalborg Universitet\\Dokumenter 2\\Skoler\\Software AAU\\6. Semester\\P6\\muse - tracking'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if (os.path.join(subdir, file)[-4:] == ".csv"):
            #print (os.path.join(subdir, file))

            with open(os.path.join(subdir, file), newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')

                Delta_TP9 = 0
                Delta_AF7 = 0
                Delta_AF8 = 0
                Delta_TP10 = 0
                tooManyZeros = False

                incrementTEMP = 0


                for row in reader:
                    if (row[1] == "0.0"):
                        Delta_TP9 += 1
                    else:
                        Delta_TP9 = 0

                    if (row[1] == "0.0"):
                        Delta_AF7 += 1
                    else:
                        Delta_AF7 = 0

                    if (row[1] == "0.0"):
                        Delta_AF8 += 1
                    else:
                        Delta_AF8 = 0

                    if (row[1] == "0.0"):
                        Delta_TP10 += 1
                    else:
                        Delta_TP10 = 0

                    tooMany = 1000
                    if Delta_TP9 > tooMany or Delta_AF7 > tooMany or Delta_AF8 > tooMany or Delta_TP10 > tooMany:
                       tooManyZeros = True

                    #print(', '.join(row))

                if (tooManyZeros):
                    print("Too many zero's in file: " + os.path.join(subdir, file))