# plugin_check.py file with classes or functions to collect data or format messages
from shareplum import Site
from requests_ntlm import HttpNtlmAuth
import datetime

class HealthMonitor:
    def __init__(self, user, password, siteurl,
                 report_list=None):
        """
        param: report: list to check from healthMonitor, example: 'Review problems and solutions'
        """
        self.report_list = report_list or 'Review problems and solutions'
        self.user = user
        self.password = password
        self.siteurl = siteurl
    
    def _connect_site(self):
        cred = HttpNtlmAuth(self.user, self.password)
        return Site(self.siteurl, auth=cred)

    def get_health_monitor_data(self):
        """
        return: example: 
            [{'Failing Servers': 'server1 \n',
            'Failing Services': 'SPTimerService (SPTimerV4)',
            'Modified': datetime.date(2018, 3, 11),
            'Severity': '2 - Warning',
            'Title': 'The paging file size should exceed the amount of physical RAM in '
                    'the system.'},
            {'Failing Services': 'UserProfileService',
            'Modified': datetime.date(2018, 3, 12),
            'Severity': '1 - Error',
            'Title': 'Verify that the critical User Profile Application and User Profile '
                    'Proxy Application timer jobs are available and have not been '
                    'mistakenly deleted.'}]
        """
        site = self._connect_site()
        sp_list = site.List(self.report_list) # List ex arg: 'Review Problems and solutions'
        return sp_list.GetListItems('All Reports')
