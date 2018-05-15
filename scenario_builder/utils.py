import docker
import random
import subprocess
from ipaddress import IPv4Network

def generate_ips(subnet, number):
    """
    Generate number of random ips in given subnet
    """
    network = IPv4Network(unicode(subnet), strict=False)

    cidr = int(subnet.split('/')[1])
    num_ips = pow(2, (32-cidr)) - 2 

    ip_list = []
    for i in range(number):
        ip = str(network[random.randint(0,num_ips)])
        if ip not in ip_list:
            ip_list.append(ip)

    return ip_list

def docker_net_create(subnet):
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
    bits = 0
    for i in xrange(32-mask,32):
        bits |= (1 << i)
    return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))

def run_cmd(args):
    try:
        p = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print p.stdout.read()
    except subprocess.CalledProcessError as e:
        if e.output:
            print "Failed with exit code %d\nCommand: %s\n%s".format(
                e.returncode,
                " ".join(args),
                e.output.decode('utf-8')
            )
        else:
            print "Failed with exit code %d\nCommand: %s".format(
                e.returncode,
                " ".join(self.args)
            )
        raise
