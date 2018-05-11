import subprocess
import os

def run(args):
    try:
        p = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print p.stdout.read()
    except subprocess.CalledProcessError as e:
        if e.output:
            print "Failed with exit code %d\nCommand: %s\n%s".format(
                e.returncode,
                " ".join(args),
                e.output.decode('utf-8')
            )
        else:
            print "Failed with exit code %d\nCommand: %s".format(
                e.returncode,
                " ".join(self.args)
            )
        raise


class AnsibleRunner:
    def __init__(self, playbook, hosts='./hosts', private_key='~/.ssh/id_rsa'):
        self.cmd = 'ansible-playbook'
        self.hosts = hosts
        self.playbook = playbook
        self.private_key = private_key

    def run_playbook(self):
        os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
        ansible_cmd = []
        ansible_cmd.append(self.cmd)
        ansible_cmd.append('-i')
        ansible_cmd.append(self.hosts)
        ansible_cmd.append(self.playbook)
        ansible_cmd.append('--private-key')
        ansible_cmd.append(self.private_key)                

        run(ansible_cmd)

