import vagrant
from jinja2 import Environment, FileSystemLoader, select_autoescape

#http://code.activestate.com/recipes/576483-convert-subnetmask-from-cidr-notation-to-dotdecima/
def calc_netmask(mask):
    bits = 0
    for i in xrange(32-mask,32):
        bits |= (1 << i)
    return "%d.%d.%d.%d" % ((bits & 0xff000000) >> 24, (bits & 0xff0000) >> 16, (bits & 0xff00) >> 8 , (bits & 0xff))


def gen_vagrantfile(vagrant_info):
    
    netmask = calc_netmask(int(vagrant_info['cidr']))

    env = Environment( 
        loader=FileSystemLoader(vagrant_info['victim']['dir']),
    )
    template = env.get_template('Vagrantfile-template')
    vagrantfile = template.render(victim_ip=vagrant_info['victim']['ip'],
                                  bridge=vagrant_info['bridge'],
                                  netmask=netmask)
    vagrant_loc = vagrant_info['victim']['dir'] + '/Vagrantfile'

    f = open(vagrant_loc, 'w')
    f.write(vagrantfile)
    f.close()
    return vagrant_loc

def vagrant_build(vagrant_info):
    vagrant_loc = gen_vagrantfile(vagrant_info)
    v = vagrant.Vagrant(vagrant_info['victim']['dir'], quiet_stdout=False, quiet_stderr=False)
    v.provision()
    v.up()

    return True
