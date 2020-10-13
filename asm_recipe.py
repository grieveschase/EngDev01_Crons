import ftplib
import getpass
import telnetlib
import time
import os
ascii_files = [txt for txt in os.listdir(os.getcwd()) if "_ascii.txt" in txt]
for ascii_txt in ascii_files:
    session = ftplib.FTP("172.18.23.43",'sys.2682','free time')

    file = open(ascii_txt,'rb')                  # file to send
    session.storbinary('STOR ' + ascii_txt , file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()


    print('start')
    HOST = "172.18.23.43"

    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"login:")
    tn.write(b"sys.2682\r\n")

    tn.read_until(b"Password: ")
    tn.write(b"free time\r\n")
    time.sleep(1)
    tn.write(b"dos2unix -ascii " + ascii_txt.encode("utf-8") +b" > " + ascii_txt.replace("_ascii","").encode("utf-8") + b"\r\n")
    time.sleep(1)
    tn.write(b"chmod 777 " + ascii_txt.replace("_ascii","").encode("utf-8") + b"\r\n")
    print(ascii_txt)
    time.sleep(1)
    tn.write(ascii_txt.replace("_ascii","").encode("utf-8") + b"\r\n")
    time.sleep(1000)

    tn.close()

    print('done')


home_dir = "/home/ccag/"
f = [home_dir + i for i in os.listdir(home_dir) if "recipes_to_text" in i]
for i in f:
    os.remove(i)
