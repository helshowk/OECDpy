#!/usr/bin/env python2

from oecd import OECDpy

def test_fn(f, *args, **kwargs):
    result = f(*args, **kwargs)
    if result is None:
        return False
    else:
        return True
        
if __name__ == "__main__":
    oecd = OECDpy()
    
    ### TEST WITHOUT FILTERS
    print "test functions without filters"
    # quite large, comment out for faster execution, nicer to test this one with filters
    #if not (test_fn(oecd.get_datasets)):
        #print "oecd.get_datasets\t\tFAIL"
    #else:
        #print "oecd.get_datasets\t\tPASS"
        
    #if not test_fn(f=oecd.get_dimensions, dataset='HS1988'):
        #print "oecd.get_dimensions\t\tFAIL"
    #else:
        #print "oecd.get_dimensions\t\tPASS"
        
    #if not test_fn(oecd.get_dimension_members, dataset='HS1988'):
        #print "oecd.get_dimension_members\t\tFAIL"
    #else:
        #print "oecd.get_dimension_members\t\tPASS"
    
    #if not test_fn(oecd.get_queries, dataset='HS1988'):
        #print "oecd.get_queries\t\tFAIL"
    #else:
        #print "oecd.get_queries\t\tPASS"
    
    #### TEST WITH FILTERS
    #print "test functions with filters"
    #if not test_fn(oecd.get_datasets, filters_and = [ "DatasetCode eq '7IA_A_Q'" ]):
        #print "oecd.get_datasets filters_and\t\tFAIL"
    #else:
        #print "oecd.get_datasets filters_and\t\tPASS"
    
    #if not test_fn(oecd.get_datasets, filters_or = [ "DatasetCode eq '7IA_A_Q'", "DatasetCode eq 'HS1988'" ]):
        #print "oecd.get_datasets filters_or\t\tFAIL"
    #else:
        #print "oecd.get_datasets filters_or\t\tPASS"
    
    #if not test_fn(oecd.get_datasets, filters_or = [ "DatasetCode eq '7IA_A_Q'", "DatasetCode eq 'HS1988'" ]):
        #print "oecd.get_datasets filters_or multiple\t\tFAIL"
    #else:
        #print "oecd.get_datasets filters_or multiple\t\tPASS"    
    
    #if not test_fn(oecd.get_datasets, filters_and = ["DatasetCode eq '7IA_A_Q'" ], filters_or = [ "DatasetCode eq 'HS1988'" ]):
        #print "oecd.get_datasets filters_and filters_or\t\tFAIL"
    #else:
        #print "oecd.get_datasets filters_and filters_or\t\tPASS"    
    
    # test get_data with filters
    # Iron and Steel trade between japan or korea with china in 2013
    #print oecd.get_data(dataset='HS1988', filters_and = ["TIME eq '2013'", "ITCS_COMH0 eq '72'", "PARTNER eq 'CHN'"], filters_or = [ "REPORTER eq 'JPN'", "REPORTER eq 'KOR'"])
    print oecd.get_data(dataset='BTDIXE_I4', filters_and = ["COU eq 'JPN'", "TIME eq '2013'", "IND eq 'DTOTAL'", "VAL eq 'VALUE'", "FLW eq 'EXPO'", "CAT eq 'TOTAL'"], filters_or = [ "PAR eq 'CHN'", "PAR eq 'USA'" ])
        
    
    
