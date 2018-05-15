import vagrant
from .. import utils
from jinja2 import Environment, FileSystemLoader, select_autoescape


def gen_vagrantfile(vagrant_info):
    """
    Add all of the networking info to the victims Vagrantfile template
    args:
        vagrant_info - Dictionary with all of the info needed to generate the Vagrantfile 
    return:
        None
    """
    
    netmask = utils.calc_netmask(int(vagrant_info['cidr']))

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
    """
    Generate Vagrantfile and build VM
    args:
        vagrant_info - Dictionary with all of the info needed to build the VM
    return:
        None
    """
    vagrant_loc = gen_vagrantfile(vagrant_info)
    v = vagrant.Vagrant(vagrant_info['victim']['dir'], quiet_stdout=False, quiet_stderr=False)
    v.up()

    return True

def vagrant_destroy(vagrant_info):
    """
    Destroy vagrant VM
    args:
        vagrant_info - dictionary with info needed to destroy vagrant VM
    return:
        None
    """
    vagrantfile = vagrant_info['victim']['dir']
    v = vagrant.Vagrant(vagrantfile, quiet_stdout=False, quiet_stderr=False)
    v.destroy()
