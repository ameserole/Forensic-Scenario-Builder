from jinja2 import Environment, FileSystemLoader, select_autoescape
from compose_runner import ComposeRunner
import time

def gen_compose_file(docker_info):
    """
    Generate docker-compose file from template
    args:
        docker_info - Dictionary containing the information needed to generate compose file
    return:
        None
    """

    env = Environment(
        loader=FileSystemLoader('./scenario_builder/builder/templates'),
        autoescape=select_autoescape(['yml'])
    )

    template = env.get_template('compose-template.yml')
    compose = template.render(attacker_dir=docker_info['attacker']['dir'],
                              attacker_ip=docker_info['attacker']['ip'],
                              victim_ip=docker_info['victim_ip'],
                              bot_dir=docker_info['bot']['dir'],
                              bot_ips=docker_info['bot']['ip_list'],
                              subnet=docker_info['subnet'])

    f = open('docker-compose.yml', 'w')
    f.write(compose)
    f.close()

def docker_build(docker_info):
    """
    Build all of the docker containers
    args:
        docker_info - Dictionary containing the information needed to build the containers
    return:
        None
    """
    
    gen_compose_file(docker_info)
    c = ComposeRunner()
    c.build()

    # Need to bring up containers and pause them 
    # so that the Vagrant vm is discoverable once attached to the network
    c.up(detach=True)
    time.sleep(10)
    c.pause()

