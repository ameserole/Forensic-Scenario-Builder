from builder import builder

def run_scenario(args):
    build_args = {}
    build_args['bot'] = args['bot']
    build_args['attacker'] = args['attacker']
    build_args['victim'] = args['victim']
    subnet = args['subnet']
    builder.build(build_args, subnet)

