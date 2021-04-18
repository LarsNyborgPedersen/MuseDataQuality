import os
import csv

rootdir = 'C:\\Users\\lars\\OneDrive - Aalborg Universitet\\Dokumenter 2\\Skoler\\Software AAU\\6. Semester\\P6\\muse - tracking'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if (os.path.join(subdir, file)[-4:] == ".csv"):
            #print (os.path.join(subdir, file))

            with open(os.path.join(subdir, file), newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')

                Delta_TP9_zero_in_a_row = 0
                Delta_AF7_zero_in_a_row = 0
                Delta_AF8_zero_in_a_row = 0
                Delta_TP10_zero_in_a_row = 0
                too_may_zero_in_a_row = False

                Delta_TP9_zero_total = 0
                Delta_AF7_zero_total = 0
                Delta_AF8_zero_total = 0
                Delta_TP10_zero_total = 0
                too_many_zero_total = False

                incrementTEMP = 0


                for row in reader:
                    if (row[1] == "0.0"):
                        Delta_TP9_zero_in_a_row += 1
                        Delta_TP9_zero_total += 1

                    else:
                        Delta_TP9_zero_in_a_row = 0

                    if (row[1] == "0.0"):
                        Delta_AF7_zero_in_a_row += 1
                        Delta_AF7_zero_total += 1
                    else:
                        Delta_AF7_zero_in_a_row = 0

                    if (row[1] == "0.0"):
                        Delta_AF8_zero_in_a_row += 1
                        Delta_AF8_zero_total += 1
                    else:
                        Delta_AF8_zero_in_a_row = 0

                    if (row[1] == "0.0"):
                        Delta_TP10_zero_in_a_row += 1
                        Delta_TP10_zero_total += 1
                    else:
                        Delta_TP10_zero_in_a_row = 0

                    too_many_in_a_row = 100
                    if Delta_TP9_zero_in_a_row > too_many_in_a_row or Delta_AF7_zero_in_a_row > too_many_in_a_row or Delta_AF8_zero_in_a_row > too_many_in_a_row or Delta_TP10_zero_in_a_row > too_many_in_a_row:
                       too_may_zero_in_a_row = True

                    too_many_total = 1000
                    if Delta_TP9_zero_total > too_many_total or Delta_AF7_zero_total > too_many_total or Delta_AF8_zero_total > too_many_total or Delta_TP10_zero_total > too_many_total:
                        too_many_zero_total = True
                    #print(', '.join(row))

                if (too_may_zero_in_a_row):
                    print("Too many zero's IN A ROW in file: " + os.path.join(subdir, file))
                if (too_many_zero_total):
                    print("Too many zero's TOTAL in file: " + os.path.join(subdir, file))

