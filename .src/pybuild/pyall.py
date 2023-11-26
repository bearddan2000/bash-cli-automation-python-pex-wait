import os
import logging
import yaml

logging.basicConfig(level=logging.INFO)

def redo_docker_compose(dir):
    FILE = os.path.join(dir, 'docker-compose.yml')
    content = None
    with open(FILE, 'r') as fi:
        content = yaml.safe_load(fi)
    
    content['services']['py-srv']['command'] = 'sh -c "/wait && ./example.pex"'

    with open(FILE, 'w') as fo:
        yaml.dump(content, fo)

def main():
    import sys
    dir = sys.argv[1]
    if dir is None:
        for x in sys.argv:
            logging.info(x)
        logging.error('No directory sent, exiting.')
        exit(1)
    
    redo_docker_compose(dir)

if __name__ == "__main__":
    main()