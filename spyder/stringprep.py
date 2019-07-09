# -*- coding: utf-8 -*-
"""
Created on Tue July 9 14:31:24 2019

@author: Rajesh Samui
"""

class InternetStringPreparation:
    """
    When identifying things (such as host names) in the internet, it is often 
    necessary to compare such identifications for “equality”. Exactly how this 
    comparison is executed may depend on the application domain, e.g. whether 
    it should be case-insensitive or not. It may be also necessary to restrict 
    the possible identifications, to allow only identifications consisting of 
    “printable” characters.
    
    RFC 3454 defines a procedure for “preparing” Unicode strings in internet 
    protocols. Before passing strings onto the wire, they are processed with 
    the preparation procedure, after which they have a certain normalized form.
    The RFC defines a set of tables, which can be combined into profiles. Each 
    profile must define which tables it uses, and what other optional parts of 
    the stringprep procedure are part of the profile. One example of a 
    stringprep profile is nameprep, which is used for internationalized domain 
    names.
    
    The module stringprep only exposes the tables from RFC 3454. As these 
    tables would be very large to represent them as dictionaries or lists, the 
    module uses the Unicode character database internally. The module source 
    code itself was generated using the mkstringprep.py utility.
    
    As a result, these tables are exposed as functions, not as data structures. There are two kinds of tables in the RFC: sets and mappings. For a set, stringprep provides the “characteristic function”, i.e. a function that returns true if the parameter is part of the set. For mappings, it provides the mapping function: given the key, it returns the associated value. Below is a list of all functions available in the module.
    """
    def __init__(self):
        pass
    
    def stringprep_in_table_a1_test(self):
        """
        Determine whether code is in tableA.1 (Unassigned code points in 
        Unicode 3.2).
        """
        pass
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    isp = InternetStringPreparation()
    print(isp.__doc__)

    print('\n# stringprep.in_table_a1(code)')
    print(isp.stringprep_in_table_a1_test.__doc__)
    isp.stringprep_in_table_a1_test()


















































































