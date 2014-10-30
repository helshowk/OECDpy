#!/usr/bin/env python2

import urllib, urllib2, json

#BTDIXE_I4?$filter=(TIME eq '2011') and (COU eq 'JPN') and (IND eq 'D01T32')&$format=json

class StatsOECD():
    def __init__(self, data_format = 'json', language_code = 'en'):
        self.base_url = "http://stats.oecd.org/OECDStatWCF_OData/OData.svc/"
        self.data_format = data_format
        self.header = {
                'User-Agent': "SatsOECDpy/0.1"
            }
        self.language_code = language_code
        
        # format and language url arguments
        self._format_arg = "$format=" + self.data_format
        self._language_code_arg = "LanguageCode='" + self.language_code = "'"
        
        # basic urls
        self._dimension_url = base_url + "GetDimensions?" + self._format_arg + "&" + self._language_code_arg + "&"
        self._datasets_url = base_url + "GetDatasets?" + self._format_arg + "&" + self._language_code_arg + "&"
        self._dimension_member_url = base_url + "GetMember?" + self._format_arg + "&" self._language_code_arg + "&"
    
    # internal helpers
    
    def _url_result(self, url):
        req = urllib2.Request(url, headers=self.header)
        cxn = urllib2.urlopen(req)
        result = json.loads(cxn.read())
        return result
        
    # getters
    
    def get_datasets(self):
        return self._url_result(self._datasets_url)
    
    def get_dimensions(self, dataset):
        url = self._dimension_url + "DatasetCode='" + dataset
        return self._url_result(url)
    
    def get_dimension_members(self, dataset):
        url = self._dimension_member_url + "DatasetCode='" + dataset + "'"
        
