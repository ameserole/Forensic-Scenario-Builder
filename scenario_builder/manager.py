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
                'manager': 'vagrant',
                'pcap': 'false'
            }
        }

    subnet = '192.168.50.1/24'
    builder.build(build_args, subnet)

run_scenario()
