__author__ = 'sriHarsha'
import os
import psutil
import datetime
import configparser
import os.path
import subprocess
from subprocess import check_output

global output_Dir, process_name, geth_Function, blockChain_dir, Time_Stamp
process_name = "geth.exe"

Time_Stamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
output_Dir, config, blockChain_dir, geth_Function = " ", "", "", ""

blockChain_dir = 'C:\\private\\blockchain'
output_Dir = 'C:\\private\\logs.txt'


# geth_Function =  'geth --datadir "/home/ubuntu/Desktop/private/blockchain/" --networkid 3141592 --nat extip:52.34.24.43 --port 30303 console'



def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


# for Raspberry-pi
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    print ['resvalue:', res]
    return (res.replace("temp=", "").replace("'C\n", ""))


# For windows and linux
def get_PID():
    pid = 0
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            pid = proc.pid

    print ['pid:', pid]
    if pid == 0:
        print ['geth_Function:', geth_Function]
        # execute geth statement
        # os.system(geth_Function)
    return pid


def write_File(output):
    if not os.path.isfile(output_Dir):
        myfile = open(output_Dir, 'w')
        myfile.write("Time_Stamp,cpu,mem,Directory_Size,CPUtemperature")
        myfile.write("\n")

    else:
        myfile = open(output_Dir, 'a')
    myfile.write(output)
    myfile.write("\n")
    myfile.close()


def linux_getcpu_mem(pid):
    command = "ps -p " + str(pid) + "-o %cpu,%mem"
    print command
    out = subprocess.check_output(command, shell=True)
    out = out.replace("%CPU %MEM\n", '').split(' ')
    return out


    # Efficient for linux
    # def get_linuxPid():
    # return os.system("ps -ef | grep geth| grep -v  grep| awk '{print $2}'")


def windows():
    os.chdir('C:\\Users\\saikaushik.mallela\\Desktop')
    psxmlgen = check_output([r'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe',
                             '-ExecutionPolicy',
                             'Unrestricted',
                             ". \"./ps_cpu.ps1\";"], shell=True)
    result = psxmlgen.strip().replace('\r\n', '').replace('-', '').split(' ')
    out = str(result[len(result) - 1] + " " + result[len(result) - 2]).split(' ')
    return out


if __name__ == "__main__":
    global geth_pid
    # read_propertyFile()
    geth_pid = str(get_PID())

    # for linuxrip
    # direct_output = linux_getcpu_mem(geth_pid)


    # for windows
    direct_output = windows()

    cpu = direct_output[0]
    mem = direct_output[1]

    rest = windows()
    print rest

    Directory_Size = int(get_size(blockChain_dir))
    # rasp only
    CPUtemperature = getCPUtemperature()
    run_output = str(Time_Stamp)+','+str(cpu) +','+str(mem)+','+str(Directory_Size)+','+str(CPUtemperature)

    write_File(run_output)





# timestamp'
# ram memory,
# cpu usage

# blockchain folder size
# network stats
# Pi temperatures
# def read_propertyFile():
# config = configparser.ConfigParser()
# config.read(config_file)

##output_Dir = config.get('DEFAULT', 'output_Dir')
## geth_Function = config.get('DEFAULT', 'geth_Function')
# blockChain_dir = config.get('DEFAULT', 'blockChain_dir')
# print geth_Function
