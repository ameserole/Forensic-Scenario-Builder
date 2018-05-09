import os

def pcap(scenario_info, pcap_write):
    cmd = "sudo tcpdump -i {} -s 65535 -w {} &".format(scenario_info['bridge'], pcap_write) 
    os.system(cmd)

