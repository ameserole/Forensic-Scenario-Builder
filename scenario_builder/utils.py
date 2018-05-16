import docker
import logging
import random
import subprocess
from Crypto.PublicKey import RSA
from os import chmod
from ipaddress import IPv4Network

def generate_ips(subnet, number):
    """
    Generate number of random ips in given subnet
    args:
        subnet - cidr notation of subnet to generate ips from
        number - number of ips to return
    return:
        ip_list - list containing generated ips
    """
    network = IPv4Network(unicode(subnet), strict=False)

    cidr = int(subnet.split('/')[1])
    max_ip_num = pow(2, (32-cidr)) - 2 

    ip_list = []
    for i in range(number):
        ip = str(network[random.randint(0,max_ip_num)])
        if ip not in ip_list:
            ip_list.append(ip)

    return ip_list

def docker_net_create(subnet):
    """
    Create a docker network for containers and vms to attach to
    args:
        subnet - The subnet for the network to operate in
    return:
        docker_net - The created docker_network object
    """
    
    client = docker.from_env()

    ipam_pool = docker.types.IPAMPool(
        subnet=subnet,
    )

    ipam_config = docker.types.IPAMConfig(
        pool_configs=[ipam_pool]
    )

    docker_net = client.networks.create(
        name="scenario_net",
        driver="macvlan",
        ipam=ipam_config,
        check_duplicate=True,
    )

    return docker_net

#http://code.activestate.com/recipes/576483-convert-subnetmask-from-cidr-notation-to-dotdecima/
def calc_netmask(mask):
    """
    Convert from CIDR number to netmask
    args:
        mask - CIDR number (e.g. 24)
    return:
        netmask - Generated netmaks (e.g. 24 -> 255.255.255.0)
    """

    bits = 0
    for i in xrange(32-mask,32):
        bits |= (1 << i)
    return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))

def run_cmd(args):
    """
    Wrapper function for subprocess to run arbitrary commands and catch and failures
    args:
        args - argument list to pass to Popen
    return:
        None
    """
    logger = logging.getLogger('root')

    try:
        p = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        logger.debug('Command: {}\nOutput:\n{}'.format(
            " ".join(args),
            p.stdout.read()
        ))
    except subprocess.CalledProcessError as e:
        if e.output:
            logger.error("Command: {}\nFailed with exit code {}\n{}".format(
                " ".join(args),
                e.returncode,
                e.output.decode('utf-8')
            ))
        else:
            logger.error("Command: {}\nFailed with exit code {}\n".format(
                " ".join(self.args),
                e.returncode
            ))
        raise

# https://stackoverflow.com/questions/2466401/how-to-generate-ssh-key-pairs-with-python
def gen_ssh_keypair():
    """
    Generate SSH Keypair for vagrant
    args:
        None
    return:
        None
    """

    key = RSA.generate(4096)
    with open("/tmp/vagrant_private.key", 'w') as content_file:
        chmod("/tmp/vagrant_private.key", 0600)
        content_file.write(key.exportKey('PEM'))
    pubkey = key.publickey()
    with open("/tmp/vagrant_public.key", 'w') as content_file:
        content_file.write(pubkey.exportKey('OpenSSH'))


# https://stackoverflow.com/questions/7621897/python-logging-module-globally
def setup_custom_logger(name):
    """
    Setup custom logging format
    args:
        name - logger name
    return:
        None
    """

    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
