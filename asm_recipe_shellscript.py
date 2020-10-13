from ftplib import FTP
import os
import datetime
from datetime import datetime
import time
import ftplib

asm_walkup_id = "172.18.23.43"

ftp = FTP(asm_walkup_id)
ftp.login('sys.2682','free time')
asm_directorys = ["ASM404","ASM405","ASM407","ASM413","ASM414","ASM417","ASM418","ASM419","ASM420","ASM421","ASM422","ASM424"]

for asm_directory in asm_directorys:
    recipes = []
    recipes_single = []
    all_recipes_listed = []
    tool_source = []
    asm_direc_file_path = "/usr/asm/sys.2682/user_data/jobs/FAB/" + asm_directory +"/"
    ftp.cwd(asm_direc_file_path)
    prod_list = ftp.nlst()


    for tic in prod_list:
        if "PROD_" in tic:
            temp_cwd = asm_direc_file_path + tic
            ftp.cwd(temp_cwd)
            temp_prod_list = ftp.nlst()
            for recipe_ind in temp_prod_list:
                prod_temp_var = tic +"/" +recipe_ind
                recipes.append(prod_temp_var)
                recipes_single.append(recipe_ind)
                tool_source.append(asm_directory)
    new_text_file = "all_" + asm_directory + "_recipes_to_text_ascii.txt"
    file = open(new_text_file,"w")
    file.write("#!/bin/csh -f")
    file.write("\n")
    file.write('set HOST = "cmi"')
    file.write("\n")
    file.write('set USER = "ccag"')
    file.write("\n")
    file.write('set PASSWD = "king123"')
    file.write("\n")
    file.write("\n")

    for tic in range(len(recipes)):
        recipe_prod_temp = recipes[tic]
        recipe_single_temp = recipes_single[tic]
        tool_source_temp = tool_source[tic]
        line = "cp user_data/jobs/FAB/"+tool_source_temp+"/"+recipe_prod_temp + " user_data/jobs/"
        file.write(line)
        file.write("\n")

        line = "pas_recipe_export " + recipe_single_temp + " " + recipe_single_temp+"_text.txt"
        file.write(line)
        file.write("\n")
        line = "\\rm -f user_data/jobs/" + recipe_single_temp
        file.write(line)
        file.write("\n")

        line = "mv user_data/" +recipe_single_temp+"_text.txt" + " ."
        file.write(line)
        file.write("\n")

        line ='set FILE = ' + '"' + recipe_single_temp+'_text.txt"'
        file.write(line)
        file.write("\n")

        line = "ftp -n $HOST <<END_SCRIPT"
        file.write(line)
        file.write("\n")

        line = "quote USER $USER"
        file.write(line)
        file.write("\n")

        line = "quote PASS $PASSWD"
        file.write(line)
        file.write("\n")

        line = "cd public_html/ASM_Tool_text_recipes/" + tool_source_temp +"/"
        file.write(line)
        file.write("\n")

        line = "put $FILE"
        file.write(line)
        file.write("\n")

        line = "quit"
        file.write(line)
        file.write("\n")

        line = "END_SCRIPT"
        file.write(line)
        file.write("\n")

        line = "\\rm -f " + recipe_single_temp+'_text.txt'
        file.write(line)
        file.write("\n")
        file.write("\n")
    file.write('echo "----------DONE----------"' )
    file.close()


    print("DONE---------------")
print("DONE---------------")
print("DONE---------------")


asm_walkup_id = "172.18.23.43"
asm_walkup_un = "sys.2682"
asm_walkup_pw = "free time"
cmi_ftp_user = "ccag"
cmi_ftp_pw = "king123"

ftp = FTP(asm_walkup_id)
ftp.login(asm_walkup_un, asm_walkup_pw)

#path to the individual tool directories found on the asm walkup.
asm_tool_directory = "/usr/asm/sys.2682/user_data/jobs/FAB/"
#tool directories found in asm_tool_directory
asm_directorys = ["ASM404","ASM405","ASM407","ASM413","ASM414","ASM417","ASM418","ASM419","ASM420","ASM422","ASM424"]

#Cycle through the directories of each tool.
#Each tool holds a directories for each device, in the device directory is a single (sometimes multiple) binary asm recipe file.
#if a device directory starts with 'PROD_' then look inside that directory for files to pull.
for asm_directory in asm_directorys:
    tool_asm_directory = asm_directory
    asm_directory = asm_directory +"/ENG/rsc"
    #two lists are recorded for each tool. The directory that holds one or more asm recipe files, and the recipe files themselves.
    #These lists of strings are recorded and used to build the shell script text.
    #list of individual recipe files found
    recipes = []
    #list of the directory for a given recipe file.
    recipes_single = []
    asm_direc_file_path = asm_tool_directory + asm_directory +"/"
    ftp.cwd(asm_direc_file_path)
    prod_list = ftp.nlst()

    for tic in prod_list:
        try:
            ftp.cwd("./" + tic)
            ftp.cwd("..")
        except ftplib.error_perm:
            recipes.append(tic)
            recipes_single.append(tic)


    new_text_file = "all_" + tool_asm_directory + "_rsc_" + "_recipes_to_text_ascii.txt"
    file = open(new_text_file,"w")
    file.write("#!/bin/csh -f")
    file.write("\n")
    file.write('set HOST = "cmi"')
    file.write("\n")
    file.write('set USER = "%s"'%cmi_ftp_user)
    file.write("\n")
    file.write('set PASSWD = "%s"'%cmi_ftp_pw)
    file.write("\n")
    file.write("\n")

    for tic in range(len(recipes)):
        recipe_prod_temp = recipes[tic]
        recipe_single_temp = recipes_single[tic]

        line = "cp user_data/jobs/FAB/"+asm_directory+"/"+recipe_prod_temp + " user_data/jobs/"
        file.write(line)
        file.write("\n")

        line = "pas_recipe_export " + recipe_single_temp + " " + recipe_single_temp+"_text.txt"
        file.write(line)
        file.write("\n")
        line = "\\rm -f user_data/jobs/" + recipe_single_temp
        file.write(line)
        file.write("\n")

        line = "mv user_data/" +recipe_single_temp+"_text.txt" + " ."
        file.write(line)
        file.write("\n")

        line ='set FILE = ' + '"' + recipe_single_temp+'_text.txt"'
        file.write(line)
        file.write("\n")

        line = "ftp -n $HOST <<END_SCRIPT"
        file.write(line)
        file.write("\n")

        line = "quote USER $USER"
        file.write(line)
        file.write("\n")

        line = "quote PASS $PASSWD"
        file.write(line)
        file.write("\n")

        line = "cd public_html/ASM_Tool_text_recipes/" + asm_directory +"/"
        file.write(line)
        file.write("\n")

        line = "put $FILE"
        file.write(line)
        file.write("\n")

        line = "quit"
        file.write(line)
        file.write("\n")

        line = "END_SCRIPT"
        file.write(line)
        file.write("\n")

        line = "\\rm -f " + recipe_single_temp+'_text.txt'
        file.write(line)
        file.write("\n")
        file.write("\n")
    file.write('echo "----------DONE----------"' )
    file.close()
ftp.close()
