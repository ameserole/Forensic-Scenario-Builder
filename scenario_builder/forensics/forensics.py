import os
from ansible_runner import AnsibleRunner

def pcap(bridge, pcap_write):
    """
    Wrapper function to start listening to traffic with tcpdump
    args:
        bridge - The linux bridge created by docker to listen on
        pcap_write - the location to write the pcap file
    return:
        None
    """
    logger = logging.getLogger('root')
    logger.debug('Listing on {}'.format(bridge))
    logger.debug('Writing pcap to {}'.format(pcap_write))
    cmd = "sudo tcpdump -i {} -s 65535 -w {} &".format(bridge, pcap_write) 
    os.system(cmd)


def logs(logs_loc):
    """
    Wrapper function to pull logs off of the victim vm with ansible
    args:
        logs_loc - location of the log files on the victim vm
    return:
        None
    """
    logger = logging.getLogger('root')
    log_path = "log_path={}".format(logs_loc)
    logger.debug('Pulling logs from {}'.format(log_path))
    runner = AnsibleRunner('./scenario_builder/forensics/playbooks/logs-linux.yaml', hosts='./scenario_builder/forensics/hosts', extra_var=log_path)
    runner.run()
    os.rename('./scenario_builder/forensics/playbooks/logs.zip', './logs.zip')


def disk_image(victim):
    """
    Wrapper function to create disk image of victim vm with ansible
    args:
        victim - location of vagrantfile
    return:
        None
    """

    tmpfile = victim + 'filesystem.image.gz'
    runner = AnsibleRunner('./scenario_builder/forensics/playbooks/diskimage-linux.yaml', hosts='./scenario_builder/forensics/hosts')
    runner.run()
    os.rename(tmpfile, './filesystem.image.gz')

def memory_dump(victim):
    """
    Wrapper function to create memory dump of victim vm with ansible
    args:
        victim - location of vagrantfile
    return:
        None
    """

    runner = AnsibleRunner('./scenario_builder/forensics/playbooks/mem-dump-linux.yaml',  hosts='./scenario_builder/forensics/hosts')
    runner.run()
    tmpfile = victim + 'mem-image.lime' 
    os.rename(tmpfile, './mem-image.lime')


def custom():
    """
    Wrapper function to run custom ansible playbook
    args:
        None
    return:
        None
    """
    return True
