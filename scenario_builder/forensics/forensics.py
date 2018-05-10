import os

def pcap(scenario_info, pcap_write):
    cmd = "sudo tcpdump -i {} -s 65535 -w {} &".format(scenario_info['bridge'], pcap_write) 
    os.system(cmd)

def logs():
    return True

def memory_dump():
    return True

def disk_image():
    return True

def custom():
    return True
