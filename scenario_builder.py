import argparse
from scenario_builder import manager
  
parser = argparse.ArgumentParser(description='Forensic Scenario Builder CLI')
parser.add_argument('--bot', required=True, nargs=1, help='Location of file describing bot container or vm.')
parser.add_argument('--bot-num', nargs=1, type=int, default=[1], help='Number of bot containers to spawn. Defaults to one.')
parser.add_argument('--attacker', required=True, nargs=1, help='Location of file describing attacker container or vm.')
parser.add_argument('--attacker-ip', nargs=1, default=['random'], help='Assign static ip to attacker. Defaults to random assignment.')
parser.add_argument('--victim', required=True, nargs=1, help='Location of file describing victim container or vm.')
parser.add_argument('--victim-ip', nargs=1, default=['random'], help='Assign static ip to victim. Defaults to random assignment.')
parser.add_argument('--logs', nargs='?', const='/var/log/', help='Location(s) to pull log file(s) from on victim after scenario is done.')
parser.add_argument('--disk-image', nargs='?', const='./filesystem.image.gz', help='Create disk image of victim after scenario is done')
parser.add_argument('--memory-dump', help='Create memory dump of victim after scenario is done')
parser.add_argument('--pcap', help='Create packet capture of scenario traffic')
parser.add_argument('--subnet', default='10.0.0.0/8', help='Subnet to place scenarios and containers on. Defaults to 10.0.0.0/8')

args = parser.parse_args()
arg_dict = {}
arg_dict['bot'] = {'dir': args.bot[0],
                   'num-ips': args.bot_num[0],
                   'manager': 'docker'}

arg_dict['attacker'] = {'dir': args.attacker[0],
                        'ip': args.attacker_ip[0],
                        'manager': 'docker'}

arg_dict['victim'] = {'dir': args.victim[0],
                      'ip': args.victim_ip[0],
                      'manager': 'vagrant'}

arg_dict['subnet'] = args.subnet
arg_dict['pcap'] = args.pcap
arg_dict['disk_image'] = args.disk_image
arg_dict['logs'] = args.logs
arg_dict['mem_dump'] = args.memory_dump

manager.run_scenario(arg_dict)
