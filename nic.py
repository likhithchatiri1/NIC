import subprocess
import re

cmd = "wmic nic get AdapterType, Name, Installed, MACAddress, GUID, Manufacturer, Availability, NetConnectionID, PowerManagementSupported, Speed."

p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = p1.communicate()

print('out: {0}'.format(out))
print('error : {0}'.format(err))

if p1.returncode == 0:
    print('command : success')
else:
    print('command : failed')

def Update_Version():
    with open('version.txt', 'r') as file:
        filedata = file.read()

    update = filedata[filedata.find(":")+1:filedata.find("'")]
    filedata = filedata.replace(update,'1.2')

    with open('version.txt', 'w') as file:
        file.write(filedata)


Update_Version()
