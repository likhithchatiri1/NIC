import subprocess
import platform

if platform.system() == "Windows":
    cmd = "wmic nic get AdapterType, Name, Installed, MACAddress, GUID, Manufacturer, Availability, NetConnectionID, PowerManagementSupported, Speed."
    # cmd = "ipconfig"
    p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = p1.communicate()

    print('out: {0}'.format(out))
    print('error : {0}'.format(err))

    if p1.returncode == 0:
        print('command : success')
    else:
        print('command : failed')

elif platform.system() == "Darwin":
    cmd = "networksetup -listallhardwareports"

    B = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = B.communicate()

    if B.returncode == 0:
        print('Result : Passed')
    else:
        print("Result : Failed")
        print("err:couldn't find{0}".format(err))

elif platform.system() == "Linux":
    cmd = "hwinfo"

    B = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = B.communicate()

    if B.returncode == 0:
        print('Result : Passed')
    else:
        print("Result : Failed")
        print("err:couldn't find{0}".format(err))

else:
    print("OS not found")
def Update_Version():
    Version_Number = '1.2'

    with open('version.txt', 'r') as file:
        filedata = file.read()

    Update = filedata[filedata.find(":")+1:filedata.find("'")]
    filedata = filedata.replace(Update,Version_Number)

    with open('version.txt', 'w') as file:
        file.write(filedata)


Update_Version()
