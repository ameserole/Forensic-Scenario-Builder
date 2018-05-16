from builder import builder
from forensics import forensics
import logging
import sys
import time
import traceback

def run_scenario(args):
    """
    Manage the building, running, and teardown of the scenario 
    as well as the collection of forensic artifacts based on 
    passed arguments.
    args:
        args - dictionary containing the arguments passed in from the command line
    return:
        None
    """
    try:
        logger = logging.getLogger('root')    

        build_args = {}
        build_args['bot'] = args['bot']
        build_args['attacker'] = args['attacker']
        build_args['victim'] = args['victim']
        subnet = args['subnet']

        logger.debug('Building Scenario')
        scenario_info = builder.build(build_args, subnet)

        if args['pcap'] is not None:
            logger.debug('Setting up tcpdump')
            forensics.pcap(scenario_info['bridge'], args['pcap'])

        logger.debug('Running scenario')
        builder.run_scenario()

        logger.debug('Sleeping {} minutes'.format(args['timeout']))

        for i in range(args['timeout']):
            logger.debug('Slept {} out of {} minutes'.format(i, args['timeout']))
            time.sleep(60)   

        builder.pause_scenario()
        if args['logs'] is not None:
            logger.debug('Creating logs')
            forensics.logs(args['logs'])
            logger.debug('Done creating logs')

        if args['disk_image'] is not None:
            logger.debug('Creating Disk Image')
            forensics.disk_image(args['victim']['dir'])
            logger.debug('Done creating disk image')

        if args['mem_dump'] is not None:
            logger.debug('Creating Memory Dump')
            forensics.memory_dump(args['victim']['dir'])
            logger.debug('Done creating memory dump')

    except Exception as e:
        logger.error('Caught unexpected error: {}'.format(traceback.format_exc()))

    finally:
        logger.debug('Tearing everything down')
        builder.cleanup_scenario(scenario_info)
        logger.debug('Scenario Done')


