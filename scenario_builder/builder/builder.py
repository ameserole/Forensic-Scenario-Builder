import docker
from docker_builder import docker_build 
from vagrant_builder import vagrant_build

client = docker.from_env()

def generate_ips(subnet, number):
    """
    Generate number of random ips in given subnet
    """

    return ['10.1.2.3', '10.10.10.10', '10.3.2.2', '10.4.3.2']

def docker_net_create(subnet, victim_ip):
    ipam_pool = docker.types.IPAMPool(
        subnet=subnet,
        aux_addresses={
                'victim': victim_ip
            }
    )

    ipam_config = docker.types.IPAMConfig(
        pool_configs=[ipam_pool]
    )

    docker_net = client.networks.create(
        name="scenario_net",
        driver="bridge",
        ipam=ipam_config
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

    docker_net = docker_net_create(subnet, victim_info['ip'])
    vagrant_info['bridge'] = "br-{}".format(docker_net.id[:12])

    docker_info['victim_ip'] = victim_info['ip']
    docker_info['subnet'] = subnet

    docker_build(docker_info)

#    net_id = client.networks.list(names="scenario_net")[0].id
#    vagrant_info['bridge'] = "br-{}".format(net_id[:12])

    vagrant_build(vagrant_info)

