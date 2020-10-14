import os, subprocess, sys

#error log writing function.
def write_error_log(input_string = None):
    error_log_filename = "drive_mount_checker_error_log.txt"
    if not input_string:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        with open(error_log_filename, 'a') as o_file:
            o_file.write(str(datetime.datetime.now()) + str(exc_type) +  str(exc_obj) +  ' line: '+ str(exc_tb.tb_lineno) + "\n" )
    else:
        with open(error_log_filename, 'a') as o_file:
            o_file.write(str(datetime.datetime.now()) + input_string +  "\n" )

mount_points = ['/mnt/eng_data',
                '/mnt/ufiles',
                '/home/ccag/Desktop/vera401',
                '/home/ccag/Desktop/vera402',
                '/home/ccag/Desktop/verity401',
                ]

for mp in mount_points:
    if not os.path.ismount(mp):
        try:
            subprocess.call(['mount',mp])
            if not os.path.ismount(mp):
                write_error_log(str(datetime.datetime.now()) + str(mp) + str(" mount point failed to mount.") )
        except:
            write_error_log()
