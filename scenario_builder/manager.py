from builder import builder

def run_scenario(args=None):
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
                'manager': 'vagrant'
            }
#            'pcap': False,
        }

    subnet = '10.0.0.0/8'
    builder.build(build_args, subnet)

run_scenario()
