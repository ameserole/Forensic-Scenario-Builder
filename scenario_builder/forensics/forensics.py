import os
from ansible_playbook import AnsibleRunner

def pcap(scenario_info, pcap_write):
    cmd = "sudo tcpdump -i {} -s 65535 -w {} &".format(scenario_info['bridge'], pcap_write) 
    os.system(cmd)

def logs(scenario_info):
    runner = AnsibleRunner('./scenario_builder/forensics/playbooks/logs-linux.yaml', hosts='./scenario_builder/forensics/hosts')
    runner.run_playbook()

def disk_image(scenario_info):
    tmpfile = '/tmp/filesystem.image.gz'
    if not os.path.exists(tmpfile):
        open(tmpfile, 'a').close()
    runner = AnsibleRunner('./scenario_builder/forensics/playbooks/diskimage-linux.yaml', hosts='./scenario_builder/forensics/hosts')
    runner.run_playbook()
    os.rename('/tmp/filesystem.image.gz', scenario_info['disk_image'])

def memory_dump():
    return True

def custom():
    return True
