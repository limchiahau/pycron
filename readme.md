# PYCRON

Pycron is a cron job scheduler written in python.

The advantage over just plain old cron is that the results of running the commands will be logged into a log file.
That is located in the pycron folder.

## Requirements

1. Python 3.6 >

## Setup

To setup pycron you will first have to add an entry to your cron file. Enter the following lines into the terminal.

`crontab -e`

Than paste the following line at the end.

Please make sure to replace:

1. username with your own username.

2. path_to_pycron with the path where pycron is located.

`0 * * * * {path_to_pycron}/main.py`

Than delete all existings lines from the cron_jobs file.

## Create new cron jobs

To create a new cron job just insert a new line into the cron_jobs file. Where each line represents a command.