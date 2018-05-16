import time
import logging
from compose_runner import ComposeRunner
from .. import utils
from docker_builder import docker_build 
from vagrant_builder import vagrant_build, vagrant_destroy
from ipaddress import ip_address, ip_network


def build(scenario_info, subnet):
    """
    Build all containers and VMs based off of given info
    args:
        scenario_info - Dictionary containing the info needed to build the containers and vms
        subnet - Subnet for scenario to operate in
    return
        return_info - Dictionary containing newly generated info from built containers and vms
    """
    
    logger = logging.getLogger('root')

    docker_info = {}
    vagrant_info = {}

    ip_list = utils.generate_ips(subnet, scenario_info['bot']['num-ips'] + 2)

    attacker_info = scenario_info['attacker']
    if 'random' in scenario_info['attacker']['ip']:
        attacker_info['ip'] = ip_list[0]
    else:
        if ip_address(unicode(scenario_info['attacker']['ip'])) in ip_network(unicode(subnet)):
            attacker_info['ip'] = scenario_info['attacker']['ip']
        else:
            logger.error('Attacker IP {} not in subnet {}'.format(scenario_info['attacker']['ip'], subnet))
            raise ValueError('Attacker IP not in subnet')

    logger.debug('Attacker IP: {}'.format(attacker_info['ip']))

    victim_info = scenario_info['victim']
    if 'random' in scenario_info['victim']['ip']:
        victim_info['ip'] = ip_list[1]
    else:
        if ip_address(unicode(scenario_info['victim']['ip'])) in ip_network(unicode(subnet)):
            victim_info['ip'] = scenario_info['victim']['ip']
        else:
            logger.error('Victim IP {} not in subnet {}'.format(scenario_info['victim']['ip'], subnet)) 
            raise ValueError('Victim IP not in subnet')

    logger.debug('Victim IP: {}'.format(victim_info['ip']))

    bot_info = scenario_info['bot']
    bot_info['ip_list'] = ip_list[2:]

    logger.debug('Bot IP list: {}'.format(bot_info['ip_list']))

    for key, value in scenario_info.iteritems():
        if value['manager'] == 'docker':
            docker_info[key] = value
        else:
            vagrant_info[key] = value

    docker_net = utils.docker_net_create(subnet)
    vagrant_info['bridge'] = "dm-{}".format(docker_net.id[:12])
    logger.debug('Docker Bridge: {}'.format(vagrant_info['bridge']))

    vagrant_info['cidr'] = subnet.split('/')[1]
    
    docker_info['victim_ip'] = victim_info['ip']
    docker_info['subnet'] = subnet

    logger.debug('Building Docker containers')
    docker_build(docker_info)
    time.sleep(10)
    logger.debug('building Vagrant VM')
    vagrant_build(vagrant_info)
    time.sleep(10)
    
    return_info = {}
    return_info['attacker'] = attacker_info
    return_info['victim'] = victim_info
    return_info['docker'] = docker_info
    return_info['vagrant'] = vagrant_info
    return_info['bridge'] = vagrant_info['bridge']

    return return_info

def run_scenario():
    c = ComposeRunner()
    c.unpause()

def pause_scenario():
    c = ComposeRunner()
    c.pause()

def cleanup_scenario(scenario_info):
    c = ComposeRunner()
    c.down()
    vagrant_destroy(scenario_info)


