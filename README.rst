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
      CRITICAL: Information: http://l224srv43:9876 |alerts=9;1;2;0;

TODO
====

* Use hash passwords
* Add Unit tests?
