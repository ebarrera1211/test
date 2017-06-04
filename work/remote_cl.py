""" Remote Command-line Automation helper library"""

import os.path
import os
import time

TIMESTAMP = time.strftime("%Y_%b_%d_%H,%M,%S",  time.localtime())

LIB_VERSION = "$Revision: 323112 $ - $Date: 2015-07-22 14:24:40 -0500 (Wed, 22 Jul 2015) $"

def lib_version():
    """ Print and return revision and date for Remote CL lib"""
    print 'Remote CL library version: %s' % LIB_VERSION
    return LIB_VERSION

def login(host, user, password):
    """ Performs login via SSH using pxssh helper library"""
    counter = 0
    import time
    # Get local username and clear SSH keys
    local_user = os.popen('whoami').read().strip()
    if local_user == 'root':
        os.system('rm -f /'+local_user+'/.ssh/known_hosts')
        os.system('rm -f /'+local_user+'/.ssh/known_hosts.old')
        time.sleep(3)
    else:
        os.system('rm -f /home/'+local_user+'/.ssh/known_hosts')
        os.system('rm -f /home/'+local_user+'/.ssh/known_hosts.old')
        time.sleep(3)

    # Perform up to 10 retried before failing connection
    while counter < 10:
        counter = counter + 1
        # Catch exception caused by trying to do an SSH connection
        try:
            connection = pxssh.pxssh()
            connection.login(host, user, password, original_prompt='~ [$]|~][#]|[>]')
            break
        except pxssh.ExceptionPxssh as e:
            # If Password Refused exception occurs exit exception handler
            if 'password refused' in e.value:
                print e.value
                exit()
            # If Could Not Synchronize exception occurs allow retry
            elif 'could not synchronize' in e.value:
                print e.value
                print "trying again"
    return connection

def timestamp():
    return TIMESTAMP

def setup_logging(log_path):
    """Sets up logging and returns a touple with a logging object and the log name"""
    import logging
    import time
    import __main__ as main
    script_name = main.__file__.replace('.py','')
    if log_path == '':
        logname = script_name+'_'+ TIMESTAMP +'.log'
    else:
        log_path = log_path.replace('\\', '/')
        path_list = log_path.split('/')
        size = len(path_list)
        if '.' not in path_list[size - 1]:
            logname = log_path + '/' + script_name+'_'+ TIMESTAMP +'.log'
        else:
            logname = log_path
    logging.basicConfig(filename=logname,
                                    filemode ='a',
                                    format = '%(asctime)s,%(msecs)d, %(name)s %(levelname)s %(message)s',
                                    datefmt = '%H:%M:%S',
                                    level=logging.DEBUG)
    return [logging, logname]

def arguments_parser(args_lists, config_file):
    """Creates an arguments parser from a given list"""
    import argparse, ConfigParser
    cfg_file_exists = os.path.isfile(config_file)
    parser = argparse.ArgumentParser(description='Script Command Line Arguments Help')
    for list in args_lists:
        parser.add_argument(list[0], list[1], help = list[2], required = False)
    args = vars(parser.parse_args())
    if cfg_file_exists == True:
        config = ConfigParser.ConfigParser()
        config_section = config_file.split('/')
        config_section = config_section[len(config_section)-1]
        config.read(config_file)
        keys = args.keys()
        for key in keys:
            if args[key] == None:
                args[key] = config.get(config_section, key)
    return args

def execute_remote(cmd, output, connection, pxtimeout):
    """ Function executes a command in a remote systems Linux bash shell"""
    connection.sendline(cmd)
    connection.prompt(timeout=pxtimeout)
    stdout = connection.before
    if output == True:
        print "BEFORE"
        print stdout
    return(stdout)

def execute_remote_nowait(cmd, connection):
    """ Function executes a command in a remote systems Linux bash shell"""
    connection.sendline(cmd)