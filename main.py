#!/usr/bin/python3

from functions import *
import logging
import os

# setup proper uri to the cron file.
#
# Note: the cron file is a text file where each line represents a command
#       that this script is going to execute.
#
cron_file =  '/cron_jobs'
cron_file = get_this_dir() + cron_file

# setup proper uri to the log file.
log_file = '/cron.log'
log_file = get_this_dir() + log_file

commands = get_commands(cron_file)

# execute the given commands.
# assigns a list of tuples that contain (error_code, command_string).
code = commands.apply(lambda command: (os.system(command), command))

# log all codes. 
logging.basicConfig(filename=log_file ,level=logging.INFO)
logging.info(code)
