#!python3
# https://nagios-plugins.org/doc/guidelines.html

# Import required libs for sharepointhealth
from .plugin_check import HealthMonitor
import argparse
import sys


# Return codes expected by Nagios
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

# Return message
message = {
    'status': OK,
    'summary': 'Example summary',
    'perfdata': 'label1=0;;;; '  # 'label'=value[UOM];[warn];[crit];[min];[max] 
}

# For multiple perdata, ensure to add space after each perfdata
# message['perfdata'] = 'label1=x;;;; '
# message['perfdata'] += 'label2=x;;;; '

# Function to parse arguments
def parse_args(args):
    """
    Information extracted from: https://mkaz.com/2014/07/26/python-argparse-cookbook/
    :return: parse.parse_args(args) object
    You can use obj.option, example:
    options = parse_args(args)
    options.user # to read username
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-u', '--user', dest='user', nargs='?', default=None, const=None,
                        help='Username for Ntlm auth like domain\\user \n')
    parser.add_argument('-p', '--password', dest='password', nargs='?', default=None, const=None,
                            help='Password for Ntlm Auth like  \n')
    parser.add_argument('-s', '--site', dest='site_url', nargs='?', default=None, const=None,
                            help='site url for sharepoint HealthMonitor, ex: http://site:9876 \n')

    if not args:
        raise SystemExit(parser.print_help())

    return parser.parse_args(args)

# Function to execute cli commands
def cli_execution(options):
    """
    : param: options: arguments from parse.parse_args(args) (see parse_args function)
    """

    def collect_data():
        # use new object class HealthMonitor
        healthmonitor = HealthMonitor(user=options.user,
                                      password=options.password,
                                      siteurl=options.site_url)
        data = healthmonitor.get_health_monitor_data()
        return data
    
    def format_message():
        return 'Information: {} '.format(options.site_url)

    def check(data):
        pc = len(data)
        if pc >= 2:
            status = CRITICAL
            message['summary'] = 'CRITICAL: '
        elif pc == 1:
            status = WARNING
            message['summary'] = 'WARNING: '
        else:
            status = OK
            message['summary'] = 'OK: '
        return status

    # Check logic starts here
    data = collect_data()
    message['status'] = check(data)
    # Add summary
    message['summary'] += format_message()
    # Add perfdata
    total = len(data)
    message['perfdata'] = "alerts={};1;2;0; ".format(total)

    # Print the message
    print("{summary}|{perfdata}".format(
        summary=message.get('summary'),
        perfdata=message.get('perfdata')
    ))

    # Exit with status code
    raise SystemExit(message['status'])

# Argument parser
# https://docs.python.org/3.5/library/argparse.html

def main():
    """
    Main function
    """
    # Get options with argparse
    options = parse_args(sys.argv[1:])
    # Execute program functions passing the options collected
    cli_execution(options)


if __name__ == "__main__":
    main()
