from builder import builder

def run_scenario(args):
    """
    build_args = {
            'bot': {
                'dir': '/home/messy/Documents/scenario/bot',
                'num-ips': 2,
                'manager': 'docker'
            },
            'attacker': {
                'dir': '/home/messy/Documents/scenario/attacker',
                'ip': 'random',
                'manager': 'docker'
            },
            'victim': {
                'dir': '/home/messy/Documents/scenario/victim',
                'ip': 'random',
                'manager': 'vagrant',
                'pcap': 'false'
            }
        }
    """
    build_args = {}
    build_args['bot'] = args['bot']
    build_args['attacker'] = args['attacker']
    build_args['victim'] = args['victim']
    subnet = args['subnet']
    builder.build(build_args, subnet)

