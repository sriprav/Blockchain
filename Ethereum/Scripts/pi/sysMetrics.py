__author__ = 'sriHarsha'
import os
import psutil
import datetime
import configparser
import os.path
import subprocess

global output_Dir, process_name, geth_Function, blockChain_dir, Time_Stamp
process_name = "geth.exe"

Time_Stamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
output_Dir, config, blockChain_dir, geth_Function = " ", "", "", ""

blockChain_dir = '//home//pi//private//blockchain//chaindata'
output_Dir = '//home//pi//Desktop//logs.txt'


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


def write_File(output):
    if not os.path.isfile(output_Dir):
        myfile = open(output_Dir, 'w')

    else:
        myfile = open(output_Dir, 'a')
    myfile.write(output)
    myfile.write("\n")
    myfile.close()




    # Efficient for linux
    # def get_linuxPid():
    # return os.system("ps -ef | grep geth| grep -v  grep| awk '{print $2}'")


if __name__ == "__main__":
    global geth_pid
    # read_propertyFile()
    geth_pid = get_PID()
    command = "ps -p " + str(geth_pid) + "-o %cpu,%mem"
    direct_output = subprocess.check_output(command, shell=True)
    direct_output = direct_output.replace("%CPU %MEM\n", '').split(' ')
    cpu = direct_output[0]
    mem = direct_output[1]
    Directory_Size = int(get_size(blockChain_dir))
    # rasp only
    CPUtemperature = getCPUtemperature()
    run_output = Time_Stamp.join(',').join(cpu).join(',').join(mem).join(',').join(Directory_Size).join(',').join(
        CPUtemperature)

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
