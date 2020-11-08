#Move .rpt and .cst file data from sems to eng_data
#=============OverView================
'''
Run by cron every 10 - 15 mins.
1. Check that SEMs and EngData directories are mounted.
2. Copy new .rpt and .cst files over to network dirve.

'''
import os, subprocess, sys
from skywater_email import *

#error log writing function.
def write_error_log(input_string = None):
    if not input_string:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        with open("cd_data_error_log.txt", 'a') as o_file:
            o_file.write(str(datetime.datetime.now()) + str(exc_type) +  str(exc_obj) +  ' line: '+ str(exc_tb.tb_lineno) + "\n" )
    else:
        with open("cd_data_error_log.txt", 'a') as o_file:
            o_file.write(str(datetime.datetime.now()) + input_string +  "\n" )

mount_points = ['/mnt/eng_data',
                '/home/ccag/Desktop/vera401',
                '/home/ccag/Desktop/vera402',
                '/home/ccag/Desktop/verity401',
                ]

dest_path = "/mnt/eng_data/F4PHOTO/Opal_Data/this_month/"

src_paths = [
            '/home/ccag/Desktop/vera401/reports/Production/Production/VSEM401/',
            '/home/ccag/Desktop/vera402/reports/Production/Production/VSEM402/',
            '/home/ccag/Desktop/verity401/reports/Production/Production/Production/',
            ]


for mp in mount_points:
    if not os.path.ismount(mp):
        try:
            subprocess.call(['mount',mp])
            if not os.path.ismount(mp):
                write_error_log(str(datetime.datetime.now()) + str(mp) + str(" mount point failed to mount.") )
        except:
            write_error_log()
            subject = "CD Data Sweeper Error, Mount Points"
            body ="Error with CD Data sweeper. Unable to Mount: %s" %mp
            to_list = ['chase.grieves@skywatertechnology.com']
            send_email(to_list,subject, body)

for src in src_paths:
    try:
        subprocess.call(['find',src,'-type','f','-name','*.rpt*','-mtime','-.01','-exec','cp','-p','{}',dest_path,';'])
        subprocess.call(['find',src,'-type','f','-name','*.cst*','-mtime','-.01','-exec','cp','-p','{}',dest_path,';'])
    except:
        write_error_log()
