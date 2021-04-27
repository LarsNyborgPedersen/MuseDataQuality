import os
import sys
import csv
import datetime
import decimal


# 
# STEP1: get filepaths
now = datetime.datetime.now()
timestamp = now.strftime("%Y_%m_%d_%h_TIME_%H_%M_%S")
workingdirectory_base = os.getcwd()
workingdirectory_data = workingdirectory_base + "/Data"
workingdirectory_result_avg = workingdirectory_base + "/Results_average_" + timestamp
workingdirectory_result_del = workingdirectory_base + "/Results_delete_" + timestamp
print("Workingdirectory: "+workingdirectory_base)
print("Datasource      : "+workingdirectory_data)
print("Result average  : "+workingdirectory_result_avg)
print("Result delete   : "+workingdirectory_result_del)

#
# STEP2: create directories when needed
if not os.path.exists(workingdirectory_base):
    print("Panic: working directory not exists!")
    sys.exit()
if not os.path.exists(workingdirectory_data):
    print("Panic: data directory does not exists!")
    sys.exit()
if not os.path.exists(workingdirectory_result_avg):
    print("ResultAverage directory does not exists... creating...")
    os.mkdir(workingdirectory_result_avg)
if not os.path.exists(workingdirectory_result_del):
    print("ResultDel directory does not exists... creating...")
    os.mkdir(workingdirectory_result_del)


def find_next_row(all_rows, index):
    row_to_return = []
    for x in range(index, len(all_rows)):
        currently_examined_row = all_rows[x]
        if not replacerow(all_rows[x]):
            return all_rows[x]

    return row_to_return



# Determine if row has to be replaced
def replacerow(row):
    replace = False
    if len(row) < 2:
        replace = True
    else:
        for x in range(1,4):
            if row[x] == "0.0" or row[x] =="":
                replace = True

    return replace

#
# STEP3: copy target files
def find_average_row(previous_row, current_row, next_row):
    average_row = current_row
    if len(previous_row) >= 25 and len(next_row) >= 25:
        for x in range(1, 24):
            try:
                previous = float(previous_row[x])
                next = float(next_row[x])



                average = (previous + next) / 2


                average_row[x] = str(average)[:15]
            except ValueError:
                pass
    return average_row



def job_avg(inputfile, outputfile, find_average):
    lines = 0

    with open(inputfile, "r") as csvfile_in:
        with open(outputfile, 'w', newline = '') as csvfile_out:
            reader = csv.reader(csvfile_in, delimiter=',', quotechar='|')
            writer = csv.writer(csvfile_out)

            #Put all rows in list all_rows
            all_rows = []
            for row in reader:
                all_rows.append(row)

            #Write row as normal, average or delete it
            for index, item in enumerate(all_rows):

                #Always write the header
                #if(index == 0):
                #    writer.writerow(item)

                if replacerow(item):

                    # Passing is the same as deleting the line
                    if not find_average:
                        pass

                    # If we need the average
                    if find_average:
                        previous_row = all_rows[index-1]
                        current_row = item
                        next_row = find_next_row(all_rows, index)

                        if replacerow(previous_row) or replacerow(next_row) or previous_row[1] == "Delta_TP9":
                            pass
                        else:
                            average_row = find_average_row(previous_row, current_row, next_row)
                            writer.writerow(average_row)
                            lines += 1


                else:
                    writer.writerow(item)
                    lines += 1


    return lines

def recursive_copy(from_t, to_t, find_average):
    linesRequired = 2000
    filesWithEnoughLines = 0

    if not os.path.exists(from_t):
        return
    if not os.path.exists(to_t):
        os.mkdir(to_t)
    for filename in os.listdir(from_t):
        new_from_t = from_t + "/" + filename
        new_to_t = to_t + "/" + filename
        print("Copy "+new_from_t+" to "+new_to_t)
        if os.path.isdir(new_from_t):
            recursive_copy(new_from_t, new_to_t, find_average)
        if os.path.isfile(new_from_t):
            lines = job_avg(new_from_t, new_to_t, find_average)
            print("Lines: " + str(lines))
            if (lines >= linesRequired):
                filesWithEnoughLines += 1
    print("Files with more than " + str(linesRequired) + "lines: " + str(filesWithEnoughLines))


recursive_copy(workingdirectory_data,workingdirectory_result_avg,True)
recursive_copy(workingdirectory_data,workingdirectory_result_del,False)





