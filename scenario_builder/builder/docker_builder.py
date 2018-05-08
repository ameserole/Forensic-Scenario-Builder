from jinja2 import Environment, FileSystemLoader, select_autoescape
import compose_cmd

def gen_compose_file(docker_info):
    env = Environment(
        loader=FileSystemLoader('./builder/templates'),
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
    return True

def docker_build(docker_info):
    gen_compose_file(docker_info)
    compose_cmd.compose_build()
    compose_cmd.compose_up(detach=True)
    compose_cmd.compose_pause()
    return True

