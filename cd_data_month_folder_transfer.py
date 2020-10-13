#To be run at the end of each month.
'''
1. Save last_month data to tar.gz file.
2. remove data in last_month file.
3. copy data from this_month dir to last_month dir.
4. remove data from this_month dir

'''
import os, subprocess, sys, datetime
from datetime import timedelta

def write_error_log(input_string = None):
    if not input_string:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        with open("cd_data_tar_zip_error_log.txt", 'a') as o_file:
            o_file.write(str(datetime.datetime.now()) + str(exc_type) +  str(exc_obj) +  ' line: '+ str(exc_tb.tb_lineno) + "\n" )
    else:
        with open("cd_data_tar_zip_error_log.txt", 'a') as o_file:
            o_file.write(str(datetime.datetime.now()) + input_string +  "\n" )


#1. Save last_month data to tar.gz file.
try:
    this_month_directory =( datetime.datetime.now() - timedelta(days=2)).strftime("%Y-%m")
    subprocess.call(['tar' ,'-zcf', '/mnt/eng_data/F4PHOTO/Opal_Data/'+ this_month_directory + '.tar.gz', '/mnt/eng_data/F4PHOTO/Opal_Data/last_month'])
except:
    write_error_log()

#2. remove data in last_month file.
new_tar_file_name = '/mnt/eng_data/F4PHOTO/Opal_Data/'+ this_month_directory + '.tar.gz'
if os.path.exists(new_tar_file_name):
    try:
        subprocess.call(['find', '/mnt/eng_data/F4PHOTO/Opal_Data/last_month/', '-type', 'f' ,'-exec', 'rm', '{}', ';'])
    except:
        write_error_log()
else:
    write_error_log(new_tar_file_name + " Was not created!!!")

#3. copy data from this_month dir to last_month dir.
subprocess.call(['cp' ,'-a' ,'/mnt/eng_data/F4PHOTO/Opal_Data/this_month/.', '/mnt/eng_data/F4PHOTO/Opal_Data/last_month/'])

#4. remove data from this_month dir
src_number_files = len(os.listdir('/mnt/eng_data/F4PHOTO/Opal_Data/this_month/'))
dest_number_files = len(os.listdir('/mnt/eng_data/F4PHOTO/Opal_Data/last_month/'))
if src_number_files == dest_number_files:
    try:
        subprocess.call(['find', '/mnt/eng_data/F4PHOTO/Opal_Data/this_month/', '-type', 'f' ,'-exec', 'rm', '{}', ';'])
    except:
        write_error_log()
else:
    write_error_log("Error when copying contents from this_month to last_month, number of files do not match!")
















#
