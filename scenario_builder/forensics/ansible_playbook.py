import subprocess

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

def ansible_playbook():
    #ansible-playbook -i hosts playbooks/logs-linux.yaml --private-key ~/.ssh/id_rsa
    args = ['ansible-playbook', '-i', 'hosts', 'playbooks/logs-linux.yaml', '--private-key', '~/.ssh/id_rsa']
    run(args)
