from builder import builder
from forensics import forensics
import time

def run_scenario(args):
    build_args = {}
    build_args['bot'] = args['bot']
    build_args['attacker'] = args['attacker']
    build_args['victim'] = args['victim']
    subnet = args['subnet']

    scenario_info = builder.build(build_args, subnet)

    if args['pcap'] is not None:
        forensics.pcap(scenario_info, args['pcap'])

    print "running scenario"
    builder.run(scenario_info)
    time.sleep(60*5)   
    forensics.logs(scenario_info)
    builder.tear_down(scenario_info)
    print "Scenario Done"    
