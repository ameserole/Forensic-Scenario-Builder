import docker
from docker_builder import docker_build 
from vagrant_builder import vagrant_build

client = docker.from_env()

def generate_ips(subnet, number):
    """
    Generate number of random ips in given subnet
    """

    return ['10.1.2.3', '10.10.10.10', '10.3.2.2', '10.4.3.2']

def build(scenario_info, subnet):
    """
    Build all containers and VMs based off of given info
    """
    
    docker_info = {}
    vagrant_info = {}
        
    ip_list = generate_ips('10.0.0.0/8', scenario_info['bot']['num-ips'] + 2)

    attacker_info = scenario_info['attacker']
    attacker_info['ip'] = ip_list[0]

    victim_info = scenario_info['victim']
    victim_info['ip'] = ip_list[1]

    bot_info = scenario_info['bot']
    bot_info['ip_list'] = ip_list[2:]

    for key, value in scenario_info.iteritems():
        if value['manager'] == 'docker':
            docker_info[key] = value
        else:
            vagrant_info[key] = value

    docker_info['victim_ip'] = victim_info['ip']
    docker_info['subnet'] = subnet

    docker_build(docker_info)
    vagrant_build(vagrant_info)

