import os
import sys
import csv
import datetime

# 
# STEP1: get filepaths
now = datetime.datetime.now()
timestamp = now.strftime("%Y_%m_%d")
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

#
# STEP3: copy target files
def job_avg(inputfile,outputfile,method):
    with open(inputfile, "r") as csvfile_in:
        with open(outputfile, 'w') as csvfile_out:
            reader = csv.reader(csvfile_in, delimiter=' ', quotechar='|')
            writer = csv.writer(csvfile_out)
            for row in reader:
                if method:
                    # calculate here the average
                    ok = True
                else:
                    # detect here if one needs to delete the row
                    ok = False
                if ok:
                    writer.writerow(row)
    return

def recursive_copy(from_t,to_t,method):
    if not os.path.exists(from_t):
        return
    if not os.path.exists(to_t):
        os.mkdir(to_t)
    for filename in os.listdir(from_t):
        new_from_t = from_t + "/" + filename
        new_to_t = to_t + "/" + filename
        print("Copy "+new_from_t+" to "+new_to_t)
        if os.path.isdir(new_from_t):
            recursive_copy(new_from_t,new_to_t,method)
        if os.path.isfile(new_from_t):
            job_avg(new_from_t,new_to_t,method)

recursive_copy(workingdirectory_data,workingdirectory_result_avg,True)
recursive_copy(workingdirectory_data,workingdirectory_result_del,False)
