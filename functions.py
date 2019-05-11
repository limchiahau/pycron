import pandas as pd
import os
import inspect

# return the commands that are to be executed as a panda Series.
def get_commands(cron_file_uri):
    commands = read_lines(cron_file_uri)
    return pd.Series(commands)

# returns a list of string that represents each line in a file.
# The file is derived from the given uri.
def read_lines(uri):
    with open(uri, 'r') as file:
        return file.readlines()

# returns a string that represents the directory this file is contained in.
def get_this_dir():
	return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))