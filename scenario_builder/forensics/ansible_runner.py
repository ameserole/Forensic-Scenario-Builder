from .. import utils
import os

class AnsibleRunner:
    def __init__(self, playbook, hosts='./hosts', private_key='~/.ssh/id_rsa', extra_var=None):
        self.cmd = 'ansible-playbook'
        self.hosts = hosts
        self.playbook = playbook
        self.private_key = private_key
        self.extra_var = extra_var

    def run(self):
        os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
        ansible_cmd = []
        ansible_cmd.append(self.cmd)
        ansible_cmd.append('-i')
        ansible_cmd.append(self.hosts)
        ansible_cmd.append(self.playbook)
        ansible_cmd.append('--private-key')
        ansible_cmd.append(self.private_key)                
        if self.extra_var is not None:
            ansible_cmd.append('--extra-var')
            ansible_cmd.append(self.extra_var)

        utils.run_cmd(ansible_cmd)

