from .. import utils

class ComposeRunner:
    """
    Wrapper class for running docker-compose commnads
    """

    def __init__(self):
        pass

    def build(self):
        cmd = ['docker-compose']
        cmd.append('build')
        utils.run_cmd(cmd)

    def up(self, detach=False):
        cmd = ['docker-compose']
        cmd.append('up')
        if detach:
            cmd.append('--d')
        utils.run_cmd(cmd)

    def down(self):
        cmd = ['docker-compose']
        cmd.append('down')
        utils.run_cmd(cmd)

    def stop(self):
        cmd = ['docker-compose']
        cdm.append('stop')
        utils.run_cmd(cmd)

    def pause(self):
        cmd = ['docker-compose']
        cmd.append('pause')
        utils.run_cmd(cmd)

    def unpause(self):
        cmd = ['docker-compose']
        cmd.append('unpause')
        utils.run_cmd(cmd)
