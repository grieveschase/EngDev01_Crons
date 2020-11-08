'''
Chase Grieves, May 2020.
The purpose of this script is to copy image containing directories from the CD-SEMs to a location on the shared network drive.
This script is intended to run on a local VM with mounted paths to the SEM image storage directories (source) and the shared network drive (dest).

Highlevel Walkthrough:
Check and create current month directory (dest) to store images based on month of measurement and which tool it was measured on.
Utilize os.listdir() to pull name of all image directories and filter which ones to copy to network based on time range (copy if measured between now and now - time_range).
Send os.system() commands to copy recursively and retain time stamp.

Application Logging takes place for successful events: app_log.txt
Error logging takes place for error events: error_log.txt

'''

import os
import datetime
import sys
import img_vars_config


def write_error_log():
    with open(os.path.split(__file__)[0] + "//img_directory_move_error_log.txt","a") as o_file:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        o_file.write( str(datetime.datetime.now()) + "  :  " + str(exc_type) +"," + str(fname) +"," + str(sys.exc_info()[1])+ "," +"line: "+ str(exc_tb.tb_lineno) + "\n")

def write_app_log(app_text):
    with open(os.path.split(__file__)[0] + "//img_directory_move_log.txt","a") as o_file:
        o_file.write(str(datetime.datetime.now()) + " : " + app_text + "\n")


this_month_directory = datetime.datetime.now().strftime("_%B_%Y")
#tool_name: sem tool name, lowercase, corresponds to directory name for final dest storage.
#source: mounted path to image containing directories on SEM.
#dest: mounted path to network storage of mass SEM images.
#time_range: number of seconds back to pull/copy image directories from source to dest. Best to do approx 3 days (60*60*24*3)
def sem_img_directory_copy_date_range(tool_name, source, dest, time_range):

    #mounted ufiles + tool_name directory, create that directory if needed.
    ufiles_tool_directory = dest + tool_name
    if not os.path.isdir(ufiles_tool_directory):
        os.mkdir(ufiles_tool_directory)

    #mounted ufiles + tool_name directory + current month directory, create that directory if needed.
    ufiles_month_tool_directory = ufiles_tool_directory + "/"+this_month_directory
    if not os.path.isdir(ufiles_month_tool_directory):
        os.mkdir(ufiles_month_tool_directory)
        write_app_log("New Directory created, " + ufiles_month_tool_directory)

    #CentOS uses python2.x , timestamp functionality is fickle. Needed total seconds for timestamp filtering of image directories.
    dt = datetime.datetime.now()
    timestamp = (dt - datetime.datetime(1970, 1, 1)).total_seconds()

    #list of image directories from mounted source tool directory.
    #filtered by directories created in the past time_range seconds and ones created in current month to eliminate overlap of putting last months images in current directory.
    img_dirs = [source + "/"+ i for i in os.listdir(source) if (datetime.datetime.fromtimestamp(os.stat(source +"/" + i).st_mtime).strftime("_%B_%Y") == this_month_directory) and ((timestamp - os.stat(source +"/" + i).st_mtime) < time_range)]
    for i in img_dirs:
        cp_command = "cp -pr " + i + " %s"%dest +tool +'/' + this_month_directory + '/'
        os.system(cp_command)

for tool, path in img_vars_config.tool_path_dict.items():
    try:
        # sem_img_directory_copy_date_range( tool_name, source, dest, time_range )
        sem_img_directory_copy_date_range(tool, path, img_vars_config.sem_img_dump_os_ufiles_path, 24*60*60*3)
    except:
        write_error_log()
