import os
from ansible_runner import AnsibleRunner

def pcap(bridge, pcap_write):
    cmd = "sudo tcpdump -i {} -s 65535 -w {} &".format(bridge, pcap_write) 
    os.system(cmd)


def logs(logs_loc):
    log_path = "log_path={}".format(logs_loc)
    print log_path
    runner = AnsibleRunner('./scenario_builder/forensics/playbooks/logs-linux.yaml', hosts='./scenario_builder/forensics/hosts', extra_var=log_path)
    runner.run()
    os.rename('./scenario_builder/forensics/playbooks/logs.zip', './logs.zip')


def disk_image(victim):
    tmpfile = victim + 'filesystem.image.gz'
    runner = AnsibleRunner('./scenario_builder/forensics/playbooks/diskimage-linux.yaml', hosts='./scenario_builder/forensics/hosts')
    runner.run()
    os.rename(tmpfile, './filesystem.image.gz')

def memory_dump(victim):
    runner = AnsibleRunner('./scenario_builder/forensics/playbooks/mem-dump-linux.yaml',  hosts='./scenario_builder/forensics/hosts')
    runner.run()
    tmpfile = victim + 'mem-image.lime' 
    os.rename(tmpfile, './mem-image.lime')


def custom():
    return True
