import telnetlib
import time
import os

#Remove image directories from CD-SEMs in standard directories

#=========VERITY401===============
sem_host = 'verity401'
tn = telnetlib.Telnet(sem_host)
tn.read_until(b"login:")
tn.write(b"opal\r\n")
time.sleep(1)
tn.write(b"find /usr/local/opal/images/AutoSave/Production/Production/Production -type d -mtime +3 -exec rm -rf {} \;\r\n")
time.sleep(200)
tn.write(b"find /usr/local/opal/images/User -type f -mtime +5 -exec rm -rf {} \;\r\n")
time.sleep(20)
tn.close()

#=========VERA401===============
sem_host = 'vsem401'
tn = telnetlib.Telnet(sem_host)
tn.read_until(b"login:")
tn.write(b"opal\r\n")
time.sleep(1)
tn.write(b"find /usr/local/opal/images/AutoSave/Production/Production/VSEM401 -type d -mtime +3 -exec rm -rf {} \;\r\n")
time.sleep(200)
tn.write(b"find /usr/local/opal/images/User -type f -mtime +5 -exec rm -rf {} \;\r\n")
time.sleep(20)
tn.close()

#=========VERA402===============
sem_host = 'vsem402'
tn = telnetlib.Telnet(sem_host)
tn.read_until(b"login:")
tn.write(b"opal\r\n")
time.sleep(1)
tn.write(b"find /usr/local/opal/images/AutoSave/Production/Production/VSEM402 -type d -mtime +3 -exec rm -rf {} \;\r\n")
time.sleep(200)
tn.write(b"find /usr/local/opal/images/User -type f -mtime +5 -exec rm -rf {} \;\r\n")
time.sleep(20)
tn.close()
