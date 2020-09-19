# -*- coding: utf-8 -*-
"""
Created on Tue July 25 14:31:24 2019

@author: Rajesh Samui
"""
import codecs

class CodecsTest:
    """
    Most standard codecs are text encodings, which encode text to bytes, but 
    there are also codecs provided that encode text to text, and bytes to 
    bytes. Custom codecs may encode and decode between arbitrary types, but 
    some module features are restricted to use specifically with text 
    encodings, or with codecs that encode to bytes.
    """
    def __init__(self):
        pass
    
    def codecs_encode_test(self):
        """
        Encodes obj using the codec registered for encoding.

        Errors may be given to set the desired error handling scheme. The 
        default error handler is 'strict' meaning that encoding errors raise 
        ValueError (or a more codec specific subclass, such as 
        UnicodeEncodeError). Refer to Codec Base Classes for more information 
        on codec error handling.
        """
        string = 'This is a test string.'
        e_string = codecs.encode(string, encoding='utf-8')
        print('e_string =', e_string)
        return
        
    def codecs_decode_test(self):
        """
        Decodes obj using the codec registered for encoding.

        Errors may be given to set the desired error handling scheme. The 
        default error handler is 'strict' meaning that decoding errors raise 
        ValueError (or a more codec specific subclass, such as 
        UnicodeDecodeError). Refer to Codec Base Classes for more information 
        on codec error handling.
        """
        string = b'This is a test string.'
        e_string = codecs.encode(string, encoding='base64')
        print('e_string =', e_string)
        d_string = codecs.decode(e_string, encoding='base64')
        print('d_string =', d_string)
        
    def codecs_lookup_test(encoding):
        """
        Looks up the codec info in the Python codec registry and returns a 
        CodecInfo object as defined below.

        Encodings are first looked up in the registry’s cache. If not found, 
        the list of registered search functions is scanned. If no CodecInfo 
        object is found, a LookupError is raised. Otherwise, the CodecInfo 
        object is stored in the cache and returned to the caller.
        """
        e = codecs.lookup('base64').encode(b'abc')
        print('e:', e)
        d = codecs.lookup('base64').decode(e[0])
        print('d:', d)
        return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    ct = CodecsTest()
    print(ct.__doc__)
    
    print("\n# codecs.encode(obj, encoding='utf-8', errors='strict')")
    print(ct.codecs_encode_test.__doc__)
    ct.codecs_encode_test()
    
    print("\n# codecs.decode(obj, encoding='utf-8', errors='strict')")
    print(ct.codecs_decode_test.__doc__)
    ct.codecs_decode_test()
    
    print("\n# codecs.lookup(encoding)")
    print(ct.codecs_lookup_test.__doc__)
    ct.codecs_lookup_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    