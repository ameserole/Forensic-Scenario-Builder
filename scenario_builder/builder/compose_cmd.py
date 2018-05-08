import subprocess

def compose_run(args):
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


def compose_build():
    args = ['docker-compose', 'build']
    compose_run(args)

def compose_up(detach=False):
    args = ['docker-compose', 'up']
    if detach:
        args.append('--d')
    compose_run(args)

def compose_down():
    args = ['docker-compose', 'down']
    compose_run(args)

def compose_stop():
    args = ['docker-compose', 'stop']
    compose_run(args)

def compose_pause():
    args = ['docker-compose', 'pause']
    compose_run(args)

def compose_unpause():
    args = ['docker-compose', 'unpause']
    compose_run(args)
