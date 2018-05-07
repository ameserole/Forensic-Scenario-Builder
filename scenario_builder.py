import argparse

def dispatcher(args):
    print args
    
parser = argparse.ArgumentParser(description='Forensic Scenario Builder CLI')
parser.add_argument('--bot', required=True, nargs=1, help='Location of file describing bot container or vm.')
parser.add_argument('--bot-num', nargs=1, type=int, default=1, help='Number of bot containers to spawn. Defaults to one.')
parser.add_argument('--attacker', required=True, nargs=1, help='Location of file describing attacker container or vm.')
parser.add_argument('--attacker-ip', nargs=1, default='random', help='Assign static ip to attacker. Defaults to random assignment.')
parser.add_argument('--victim', required=True, nargs=1, help='Location of file describing victim container or vm.')
parser.add_argument('--victim-ip', nargs=1, default='random', help='Assign static ip to victim. Defaults to random assignment.')
parser.add_argument('--logs', nargs='*', help='Location(s) to pull log file(s) from on victim after scenario is done.')
parser.add_argument('--disk-image', help='Create disk image of victim after scenario is done')
parser.add_argument('--memory-dump', help='Create memory dump of victim after scenario is done')
parser.add_argument('--pcap', help='Create packet capture of scenario traffic')
parser.add_argument('--subnet', default='10.0.0.0/8', help='Subnet to place scenarios and containers on. Defaults to 10.0.0.0/8')


args = parser.parse_args()
dispatcher(args)
