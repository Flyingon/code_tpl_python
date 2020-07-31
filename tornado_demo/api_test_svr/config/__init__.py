import os
import configparser

server_port = None
process_num = None
current_path = os.path.dirname(os.path.realpath(__file__))


def init_config(conf_file):
    global server_port
    global process_num

    config = configparser.ConfigParser()
    config.read(conf_file)
    server_port = int(config.get('server_conf', 'server_port'))
    process_num = int(config.get('server_conf', 'process_num'))


def basic_conf_check():
    check_points = [
        ('server_port', server_port),
        ('process_num', process_num),
    ]
    for p in check_points:
        print('%s: %s' % (p[0], p[1]))
        if not p[1]:
            print('ERROR: %s init failed' % p[0])
            return
    print('All preparation init success')
