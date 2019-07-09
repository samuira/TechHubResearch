# -*- coding: utf-8 -*-
"""
Created on Tue July 8 14:31:24 2019

@author: Rajesh Samui
"""
from unicodedata import ( lookup, name, decimal, digit, )

class UnicodeDatabase:
    """
    This module provides access to the Unicode Character Database (UCD) which 
    defines character properties for all Unicode characters. The data contained
    in this database is compiled from the UCD version 11.0.0.

    The module uses the same names and symbols as defined by Unicode Standard 
    Annex #44, “Unicode Character Database”. It defines the following functions:
    """
    def __init__(self):
        pass
    
    def unicodedata_lookup_test(name):
        """
        Look up character by name. If a character with the given name is found,
        return the corresponding character. If not found, KeyError is raised.

        Changed in version 3.3: Support for name aliases 1 and named sequences 
        2 has been added.
        """
        print("lookup('LEFT CURLY BRACKET'):", lookup('LEFT CURLY BRACKET'))
        print("lookup('RIGHT SQUARE BRACKET'):", lookup('RIGHT SQUARE BRACKET'))
        return
    
    def unicodedata_name_test(self):
        """
        Returns the name assigned to the character chr as a string. If no name 
        is defined, default is returned, or, if not given, ValueError is raised.
        """
        print("name('/'):", name('/'))
        print("name('\\'):", name('\\'))
        print("name('>'):", name('>'))
        print("name('`'):", name('`'))
        print("name('~'):", name('~'))
        print("name('#'):", name('#'))
        print("name('^'):", name('^'))
        print("name('|'):", name('|'))
        return
    
    def unicodedata_decimal_test(self):
        """
        Returns the decimal value assigned to the character chr as integer. If 
        no such value is defined, default is returned, or, if not given, 
        ValueError is raised.
        """
        print("decimal('9'):", decimal('9'))
        try:
            decimal('a')
        except Exception as e:
            print(type(e),e)
        return
    
    def unicodedata_digit_test(self):
        """
        Returns the digit value assigned to the character chr as integer. If no
        such value is defined, default is returned, or, if not given, 
        ValueError is raised.
        """
        print("digit('9'):", digit('9'))
    
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    ud = UnicodeDatabase()
    print(ud.__doc__)
    
#    print('\n# unicodedata.lookup(name)')
#    print(ud.unicodedata_lookup_test.__doc__)
#    ud.unicodedata_lookup_test()

#    print('\n# unicodedata.name(chr[, default])')
#    print(ud.unicodedata_name_test.__doc__)
#    ud.unicodedata_name_test()
    
#    print('\n# unicodedata.decimal(chr[, default])')
#    print(ud.unicodedata_decimal_test.__doc__)
#    ud.unicodedata_decimal_test()
    
    print('\n# unicodedata.digit(chr[, default])')
    print(ud.unicodedata_digit_test.__doc__)
    ud.unicodedata_digit_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    