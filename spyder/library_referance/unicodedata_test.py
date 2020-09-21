# -*- coding: utf-8 -*-
"""
Created on Tue July 8 14:31:24 2019

@author: Rajesh Samui
"""
from unicodedata import ( lookup, name, decimal, digit, numeric, category, 
                         bidirectional, combining, east_asian_width, mirrored, 
                         decomposition, normalize, unidata_version, ucd_3_2_0, )

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
        
        This function looks up for the character by name. If a character with 
        the given name is found in the database, then, the corresponding 
        character is returned otherwise Keyerror is raised.
        
        Changed in version 3.3: Support for name aliases 1 and named sequences 
        2 has been added.
        """
        print("lookup('LEFT CURLY BRACKET'):", lookup('LEFT CURLY BRACKET'))
        print("lookup('RIGHT SQUARE BRACKET'):", lookup('RIGHT SQUARE BRACKET'))
        print("lookup('ASTERISK'):", lookup('ASTERISK'))
        return
    
    def unicodedata_name_test(self):
        """
        Returns the name assigned to the character chr as a string. If no name 
        is defined, default is returned, or, if not given, ValueError is raised.
        
        This function returns the name assigned to the given character as a 
        string. If no name is defined, default is returned by the function 
        otherwise ValueError is raised if name is not given.
        """
        print("name('/'):", name('/'))
        print("name('\\'):", name('\\'))
        print("name('>'):", name('>'))
        print("name('`'):", name('`'))
        print("name('~'):", name('~'))
        print("name('#'):", name('#'))
        print("name('^'):", name('^'))
        print("name('|'):", name('|'))
        print("name(':'):", name(':')) 
        return
    
    def unicodedata_decimal_test(self):
        """
        Returns the decimal value assigned to the character chr as integer. If 
        no such value is defined, default is returned, or, if not given, 
        ValueError is raised.
        This function returns the decimal value assigned to the given character
        as integer. If no value is defined, default is returned by the function
        otherwise ValueError is raised if value is not given.
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
        This function returns the digit value assigned to the given character 
        as integer. If no value is defined, default is returned by the function
        otherwise ValueError is raised if value is not given.
        """
        print("digit('1'):", digit('1')) # Decimal digit one.
        print("digit('١'):", digit('١')) # ARABIC-INDIC digit one
        print("digit('①'):", digit('①'))    
        try:
            print(digit('¼')) # Not a digit, so "ValueError: not a digit" will be generated.
        except Exception as e:
            print(type(e), e)
        
    def unicodedata_numeric_test(self):
        """
        Returns the numeric value assigned to the character chr as float. If no
        such value is defined, default is returned, or, if not given, 
        ValueError is raised.
        """
        print("numeric('Ⅱ'):", numeric('Ⅱ')) # Roman number two.
        print("numeric('¼'):", numeric('¼')) # Fraction to represent one quarter.
        return
    
    def unicodedata_category_test(self):
        """
        Returns the general category assigned to the character chr as string.
        This function returns the general category assigned to the given 
        character as string. For example, it returns ‘L’ for letter and ‘u’ for
        uppercase.
        """
        print("category('A'):", category('A'))  # 'L'etter, 'u'ppercase
        print("category('a'):", category('a'))  # 'L'etter, 'l'ower
        return
    
    def unicodedata_bidirectional_test(self):
        """
        Returns the bidirectional class assigned to the character chr as 
        string. If no such value is defined, an empty string is returned.
        """
        print("bidirectional('\\u0660'):", bidirectional('\u0660')) # 'A'rabic, 'N'umber
        return
    
    def unicodedata_combining_test(chr):
        """
        Returns the canonical combining class assigned to the character chr as 
        integer. Returns 0 if no combining class is defined.
        """
        print("combining('a'):", combining('a'))
        print("combining('\u0327'):", combining('\u0327'))
        return
    
    def unicodedata_east_asian_width_test(self):
        """
        Returns the east asian width assigned to the character chr as string.
        
        # East_Asian_Width (ea)
        ea ; A         ; Ambiguous
        ea ; F         ; Fullwidth
        ea ; H         ; Halfwidth
        ea ; N         ; Neutral
        ea ; Na        ; Narrow
        ea ; W         ; Wide
        """
        string = "你好halloবাংলাहिन्दी"
        for char in string:
            print(char, east_asian_width(char), sep=' -> ')
        return
    
    def unicodedata_mirrored_test(self):
        """
        Returns the mirrored property assigned to the character chr as integer.
        Returns 1 if the character has been identified as a “mirrored” 
        character in bidirectional text, 0 otherwise.
        """
        print("mirrored('A'):", mirrored('A'))
        print("mirrored('<'):", mirrored('<'))
        return
    
    def unicodedata_decomposition_test(self):
        """
        Returns the character decomposition mapping assigned to the character 
        chr as string. An empty string is returned in case no such mapping is 
        defined.
        """
        print("decomposition('⑴'):", decomposition('⑴'))
        print("decomposition('①'):", decomposition('①'))
        print("decomposition('è'):", decomposition('è'))
        return
    
    def unicodedata_normalize_test(self):
        """
        Return the normal form for the Unicode string unistr. Valid values
        for form are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

        The Unicode standard defines various normalization forms of a Unicode 
        string, based on the definition of canonical equivalence and 
        compatibility equivalence. In Unicode, several characters can be 
        expressed in various way. For example, the character U+00C7 (LATIN 
        CAPITAL LETTER C WITH CEDILLA) can also be expressed as the sequence 
        U+0043 (LATIN CAPITAL LETTER C) U+0327 (COMBINING CEDILLA).
    
        For each character, there are two normal forms: normal form C and 
        normal form D. Normal form D (NFD) is also known as canonical 
        decomposition, and translates each character into its decomposed form. 
        Normal form C (NFC) first applies a canonical decomposition, then 
        composes pre-combined characters again.
    
        In addition to these two forms, there are two additional normal forms 
        based on compatibility equivalence. In Unicode, certain characters are 
        supported which normally would be unified with other characters. For 
        example, U+2160 (ROMAN NUMERAL ONE) is really the same thing as U+0049 
        (LATIN CAPITAL LETTER I). However, it is supported in Unicode for 
        compatibility with existing character sets (e.g. gb2312).
    
        The normal form KD (NFKD) will apply the compatibility decomposition, 
        i.e. replace all compatibility characters with their equivalents. The 
        normal form KC (NFKC) first applies the compatibility decomposition, 
        followed by the canonical composition.
    
        Even if two unicode strings are normalized and look the same to a human
        reader, if one has combining characters and the other doesn’t, they may
        not compare equal.
        """
        print("normalize('NFC', '\u0061\u0301'):", 
              normalize('NFC', '\u0061\u0301'))
        print("normalize('NFD', '\u00e1'):", normalize('NFD', '\u00e1'))
        print("normalize('NFC', u'\u2167'):", normalize('NFC', u'\u2167'))  # roman numeral VIII
        print("normalize('NFKC', u'\u2167'):", normalize('NFKC', u'\u2167')) # roman numeral VIII
        return
    
    def unicodedata_unidata_version_test(self):
        """
        The version of the Unicode database used in this module.
        """
        print('unidata_version:', unidata_version)
        return
    
    def unicodedata_ucd_3_2_0_test(self):
        """
        This is an object that has the same methods as the entire module, but 
        uses the Unicode database version 3.2 instead, for applications that 
        require this specific version of the Unicode database (such as IDNA).
        """
        print('ucd_3_2_0.unidata_version:', ucd_3_2_0.unidata_version)
        return
    
    

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
    
#    print('\n# unicodedata.digit(chr[, default])')
#    print(ud.unicodedata_digit_test.__doc__)
#    ud.unicodedata_digit_test()
    
#    print('\n# unicodedata.numeric(chr[, default])')
#    print(ud.unicodedata_numeric_test.__doc__)
#    ud.unicodedata_numeric_test()
    
#    print('\n# unicodedata.category(chr)')
#    print(ud.unicodedata_category_test.__doc__)
#    ud.unicodedata_category_test()
    
#    print('\n# unicodedata.bidirectional(chr)')
#    print(ud.unicodedata_bidirectional_test.__doc__)
#    ud.unicodedata_bidirectional_test()
    
#    print('\n# unicodedata.combining')
#    print(ud.unicodedata_combining_test.__doc__)
#    ud.unicodedata_combining_test()
    
#    print('\n# unicodedata.east_asian_width(chr)')
#    print(ud.unicodedata_east_asian_width_test.__doc__)
#    ud.unicodedata_east_asian_width_test()
    
#    print('\n# unicodedata.mirrored(chr)')
#    print(ud.unicodedata_mirrored_test.__doc__)
#    ud.unicodedata_mirrored_test()
    
#    print('\n# unicodedata.decomposition(chr)')
#    print(ud.unicodedata_decomposition_test.__doc__)
#    ud.unicodedata_decomposition_test()
    
#    print('\n# unicodedata.normalize(form, unistr)')
#    print(ud.unicodedata_normalize_test.__doc__)
#    ud.unicodedata_normalize_test()
    
#    print('\n# unicodedata.unidata_version')
#    print(ud.unicodedata_unidata_version_test.__doc__)
#    ud.unicodedata_unidata_version_test()
    
    print('\n# unicodedata.ucd_3_2_0')
    print(ud.unicodedata_ucd_3_2_0_test.__doc__)
    ud.unicodedata_ucd_3_2_0_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    