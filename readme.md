# PYCRON

Pycron is a cron job scheduler written in python.

The advantage over just plain old cron is that the results of running the commands will be logged into a log file.
That is located in the pycron folder.

## Setup

To setup pycron you will first have to add an entry to your cron file. Enter the following lines into the terminal.

[code]crontab -e[code]

Than paste the following line at the end.

Please make sure to replace:

1. username with your own username.

2. path_to_pycron with the path where pycron is located.

[code]0 * * * * {username} python '{path_to_pycron}/main.py'[code]

## Create new cron jobs

To create a new cron job just insert a new line into the cron_jobs file. Where each line represents a command.