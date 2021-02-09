import os
import cmd
import platform
import subprocess
import sys 

sys.stdout = open("output.txt", "w")

lines = []
my_file = open("C:\\Users\\esteban.salto.NA\\source\\repos\\automation-ping\\automation-ping\\ip_list.txt")
for line in my_file: 
    l = [i.strip() for i in line.split(' ')] 
    lines.append(l[0])

def ping(host):
        command = ['ping', '-n', '5', '-a', line]


        subprocess.call(command)
count = 0
for line in lines:
        ping(line)
        if ping == 0:
                count = count + 1
                strCount = str(count)
 
                print ("###result:PASS###",count)
                print ("==============================")
                print(line, 'timed out' "is not pinging")
                with open('logfile.txt','a+') as f:
                        f.write(print)
        else:
                print(line, 'Pinging %' "its responding")
sys.exit

                
        



#with open("C:\\Users\\esteban.salto.NA\\source\\repos\\automation-ping\\automation-ping\\ip_list.txt") as file:
#        print (file.read())
#        dump = print (file.read())
#        dump = (file.read())
#        dump = (dump.splitlines())






#IP = open("ip_list.txt", "rb")
#for line in ip_list: 
#    l = [i.strip() for i in line.split(' ')] 
#    IP.append(l[0])
#
#def Main():
#    for ip in IP: 
#      ping = os.system("ping", "-c", "1", "-n", "-W", "2", ip)
#      if ping:
#            CT=time.strftime ("%H:%M:%S %d/%m/%y")
#            alert=' No Connection'
#            with open('logfile.txt','a+') as f:
#                f.write('\n'+CT)
#                f.write(alert)
#
#      time.sleep(4)
#
#if __name__ == "__main__":
#    Main()