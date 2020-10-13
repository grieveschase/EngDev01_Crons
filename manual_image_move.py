'''
Chase Grieves, May 2020
See img_directory_move.py for high level details.

'''


import os
import datetime

import img_vars_config

def write_error_log():
    with open(os.path.split(__file__)[0] + "//error_log_manual_imgs.txt","a") as o_file:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        o_file.write( str(datetime.datetime.now()) + "  :  " + str(exc_type) +"," + str(fname) +"," + str(sys.exc_info()[1])+ "," +"line: "+ str(exc_tb.tb_lineno) + "\n")

def write_app_log(app_text):
    with open(os.path.split(__file__)[0] + "//app_log_manual_imgs.txt","a") as o_file:
        o_file.write(str(datetime.datetime.now()) + " : " + app_text + "\n")

this_month_directory = datetime.datetime.now().strftime("_%B_%Y")

def sem_manual_img_copy(tool_name, source, dest, time_range):
    #mounted ufiles + tool_name directory, create that directory if needed.
    ufiles_tool_directory = dest + tool_name
    if not os.path.isdir(ufiles_tool_directory):
        os.mkdir(ufiles_tool_directory)

    #mounted ufiles + tool_name directory + current month directory, create that directory if needed.
    ufiles_month_tool_directory = ufiles_tool_directory + "/"+this_month_directory
    if not os.path.isdir(ufiles_month_tool_directory):
        os.mkdir(ufiles_month_tool_directory)
        write_app_log("New Directory created, " + ufiles_month_tool_directory)

    dt = datetime.datetime.now()
    timestamp = (dt - datetime.datetime(1970, 1, 1)).total_seconds()
    img_dirs = [source + "/"+ i for i in os.listdir(source) if  (timestamp - os.stat(source +"/" + i).st_mtime) < time_range ]
    for i in img_dirs:
        cp_command = "cp -p " + i + " %s"%dest +tool +'/' + this_month_directory + '/'
        os.system(cp_command)

for tool, path in img_vars_config.tool_path_manual_img_dict.items():
    try:
        sem_manual_img_copy(tool, path, img_vars_config.sem_img_dump_os_ufiles_path, 24*60*60*1)
    except:
        write_error_log()
