Sharepoint HealthPlugin
=======================

Checks sharepoint HealthMonitor reports list and raise an alert if some is found.

`VERSION  <burp_reports/VERSION>`__

Install
=======

Linux::

    sudo pip3 install sp-health --upgrade

Also is possible to use::

    sudo python3 -m pip install sp-health --upgrade

On windows with python3.5::

    pip install sp-health --upgrade

For proxies add::

    --proxy='http://user:passw@server:port'

Usage
=====

Use the command line::

    sphealth --help
    
    usage: sphealth [-h] [-u [USER]] [-p [PASSWORD]] [-s [SITE_URL]]

    optional arguments:
    -h, --help            show this help message and exit
    -u [USER], --user [USER]
                            Username for Ntlm auth like domain\user
    -p [PASSWORD], --password [PASSWORD]
                            Password for Ntlm Auth like
    -s [SITE_URL], --site [SITE_URL]
                            site url for sharepoint HealthMonitor, ex: http://site:9876

Example usage
=============

Example use::

    > sphealth -u domain\user -p pass -s http://spurl:9876
    Information: http://spurl:9876 |alerts=9;1;2;0;

Example Command and service
===========================

Example host::

    # https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/macros.html#Custom%20Variable%20Macros
    # we use CUSTOM MACRO for these Sharepoint SERVERS
    # ADD _SPURLMON for each host
    # Where _SPURLMON is the name of the root URL for Sharepoint Central Administration (without /HealthReports)
    # Also add _SPUSER and _SPPASSWORD
    # https://github.com/pablodav/sharepoint_health_mon_plugin

    define host
        host_name		HOSTXX1
        alias 			Sharepoint Host XX1
        parents			SOMEDEVICE
        _SPURLMON	    http://spurlfqdn:9876
        _SPUSER         domain\username
        _SPPASSWORD     somepassword
        address			IP.ADD.RR.ESS
        use			    generic-host
    }

Example group::

    define hostgroup {
        hostgroup_name  sharepoint_servers
        alias			Sharepoint servers
        members			HOSTXX1,HOSTXX2
    }

Example command::

    define command{
        command_name  check_sphealth
        command_line  /usr/local/bin/sphealth -u '$ARG1$' -p '$ARG2$' -s '$ARG3$'
    }

Example service::

    define service {
        hostgroup_name          sharepoint_servers
        service_description     Sharepoint_HealthMonitor
        check_command           check_sphealth!$_HOSTSPUSER$!$_HOSTSPPASSWORD$!$_HOSTSPURLMON$
        notes                   Check the alerts from $_HOSTSPURLMON$ for sharepoint HealthMonitor
        use                     generic-service
    }

TODO
====

* Use hash passwords
* Add Unit tests?

Notes
=====

This command is installed and added in project: https://github.com/CoffeeITWorks/ansible_nagios4_server_plugins
