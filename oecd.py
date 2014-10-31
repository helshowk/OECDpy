
#!/usr/bin/env python2

import urllib, urllib2, json

#BTDIXE_I4?$filter=(TIME eq '2011') and (COU eq 'JPN') and (IND eq 'D01T32')&$format=json

class OECDpy():
    def __init__(self, data_format = 'json', language_code = 'en'):
        self.base_url = "http://stats.oecd.org/OECDStatWCF_OData/OData.svc/"
        self.data_format = data_format
        self.header = {
                'User-Agent': "SatsOECDpy/0.1"
            }
        self.language_code = language_code
        
        # format and language url arguments
        self._format_arg = "$format=" + self.data_format
        self._language_code_arg = "LanguageCode=" + self.language_code
        
        # basic urls
        self._dimension_url = self.base_url + "GetDimension?" + self._format_arg + "&" + self._language_code_arg
        self._datasets_url = self.base_url + "GetDatasets?" + self._format_arg + "&" + self._language_code_arg 
        self._dimension_member_url = self.base_url + "GetMember?" + self._format_arg + "&" + self._language_code_arg 
        self._queries_url = self.base_url + "GetQuery?" + self._format_arg + "&" + self._language_code_arg 
    
    # internal helpers
    def _url_result(self, url):
        try:
            req = urllib2.Request(url, headers=self.header)
            cxn = urllib2.urlopen(req)
            result = json.loads(cxn.read())
            return result
        except urllib2.HTTPError, e:
            print "Problem retrieving url: "
            print url
            return None
        except:
            raise
        
    def _build_filters(self, filters_and, filters_or):
        # filters are just strings as expected by OECD stats, e.g. (TIME eq '2011') etc... later this can be touched up and more flexible but for now it's just a simple wrapper
        # filter_and is of course combined with ANDs and filter_or is combined with OR
        
        filters_and = [ "(" + urllib.quote_plus(f) + ")" for f in filters_and ]
        filters_or = [ "(" + urllib.quote_plus(f) + ")" for f in filters_or ]
        
        str_filters_and = "(" + ('%20and%20').join(filters_and) + ")"
        str_filters_or = "(" + ('%20or%20').join(filters_or) + ")"
        
        filters = ''
        if str_filters_and <> '()' and str_filters_or <> '()':
            filters = "(" + str_filters_and + ")%20and%20(" + str_filters_or + ")"
        elif str_filters_and <> '()':
            filters = str_filters_and
        elif str_filters_or <> '()':
            filters = str_filters_or
            
        return ("&$filter=" + filters) if filters <> '' else ''
        
    # getters
    def get_datasets(self, filters_and=list(), filters_or=list()):
        url = self._datasets_url + self._build_filters(filters_and, filters_or)
        return self._url_result(url)
    
    def get_dimensions(self, dataset, filters_and=list(), filters_or=list()):
        url = self._dimension_url + "&DatasetCode=" + dataset + self._build_filters(filters_and, filters_or)
        return self._url_result(url)
    
    def get_dimension_members(self, dataset, filters_and=list(), filters_or=list()):
        url = self._dimension_member_url + "&DatasetCode=" + dataset + self._build_filters(filters_and, filters_or)
        return self._url_result(url)
        
    def get_queries(self, dataset, filters_and=list(), filters_or=list()):
        url = self._queries_url + "&DatasetCode=" + dataset + self._build_filters(filters_and, filters_or)
        return self._url_result(url)

    def get_data(self, dataset, filters_and=list(), filters_or = list()):
        url = self.base_url + dataset + "?" + self._format_arg + "&" + self._language_code_arg + self._build_filters(filters_and, filters_or)
        print url
        return self._url_result(url)
