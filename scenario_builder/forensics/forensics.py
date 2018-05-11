import os
from ansible_playbook import AnsibleRunner

def pcap(scenario_info, pcap_write):
    cmd = "sudo tcpdump -i {} -s 65535 -w {} &".format(scenario_info['bridge'], pcap_write) 
    os.system(cmd)

def logs(scenario_info):
    print os.getcwd()
    runner = AnsibleRunner('./scenario_builder/forensics/playbooks/logs-linux.yaml', hosts='./scenario_builder/forensics/hosts')
    runner.run_playbook()

def memory_dump():
    return True

def disk_image():
    return True

def custom():
    return True
