import docker
import time
import compose_cmd
import random
from ipaddress import IPv4Network
from docker_builder import docker_build 
from vagrant_builder import vagrant_build, vagrant_destroy

client = docker.from_env()

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

def build(scenario_info, subnet):
    """
    Build all containers and VMs based off of given info
    """
    
    docker_info = {}
    vagrant_info = {}

    ip_list = generate_ips(subnet, scenario_info['bot']['num-ips'] + 2)

    attacker_info = scenario_info['attacker']
    if 'random' in scenario_info['attacker']['ip']:
        attacker_info['ip'] = ip_list[0]
    else:
        attacker_info['ip'] = scenario_info['attacker']['ip']

    victim_info = scenario_info['victim']
    if 'random' in scenario_info['victim']['ip']:
        victim_info['ip'] = ip_list[1]
    else:
        victim_info['ip'] = scenario_info['victim']['ip']

    bot_info = scenario_info['bot']
    bot_info['ip_list'] = ip_list[2:]

    for key, value in scenario_info.iteritems():
        if value['manager'] == 'docker':
            docker_info[key] = value
        else:
            vagrant_info[key] = value

    docker_net = docker_net_create(subnet)
    vagrant_info['bridge'] = "dm-{}".format(docker_net.id[:12])
    vagrant_info['cidr'] = subnet.split('/')[1]

    docker_info['victim_ip'] = victim_info['ip']
    docker_info['subnet'] = subnet

    docker_build(docker_info)
    time.sleep(10)
    vagrant_build(vagrant_info)
    time.sleep(10)
    
    return_info = {}
    return_info['attacker'] = attacker_info
    return_info['victim'] = victim_info
    return_info['docker'] = docker_info
    return_info['vagrant'] = vagrant_info
    return_info['bridge'] = vagrant_info['bridge']

    return return_info

def run(scenario_info):
    compose_cmd.compose_unpause()

def tear_down(scenario_info):
    compose_cmd.compose_down()
    vagrant_destroy(scenario_info)

