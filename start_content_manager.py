import subprocess
from sys import argv

CONTAINER_NAME = 'danny-site'
PORT_MAPPING = '127.0.0.1:8096:8000'
VOLUME_MAPPING = '{}/src/img:/images'.format(argv[1])
IMAGE = 'personal_website'

def check_for_container(name):
    command = ['docker', 'ps', '-a']
    output = subprocess.check_output(command)
    for line in output.split('\n'):
        if name in line:
            print 'Container "{}" already exists'.format(name)
            print line
            return 'running' if 'Up' in line else 'stopped'
    return False

def stop_old_container(name):
    print 'Stopping old container: {}...'.format(name)
    command = ['docker', 'stop', name]
    print subprocess.check_output(command)

def remove_old_container(name):
    print 'Removing old container: {}...'.format(name)
    command = ['docker', 'rm', name]
    print subprocess.check_output(command)

def start_container(name, image, port_mapping, volume_mapping):
    command = ['docker', 'run']
    volumes = ['-v', volume_mapping]
    ports = ['-p', port_mapping]
    name = ['--name', name]
    disconnect = ['-d']
    image = [image]
    
    print subprocess.check_output(command + volumes + ports + name 
                            + disconnect + image)

if __name__ == '__main__':
    container_status = check_for_container(CONTAINER_NAME)
    if container_status:
        if container_status == 'running':
            stop_old_container(CONTAINER_NAME)
        remove_old_container(CONTAINER_NAME)
    start_container(CONTAINER_NAME, IMAGE, PORT_MAPPING, VOLUME_MAPPING)
