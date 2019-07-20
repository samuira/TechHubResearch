# -*- coding: utf-8 -*-
"""
Created on Tue July 18 14:31:24 2019

@author: Rajesh Samui
"""
import struct
import ctypes


class BinaryDataServices:
    """
    The modules described in this chapter provide some basic services 
    operations for manipulation of binary data. Other operations on binary 
    data, specifically in relation to file formats and network protocols, are 
    described in the relevant sections.

    Some libraries described under Text Processing Services also work with 
    either ASCII-compatible binary formats (for example, re) or all binary data
    (for example, difflib).
    
    In addition, see the documentation for Python’s built-in binary data types 
    in Binary Sequence Types — bytes, bytearray, memoryview.
    """
    def __init__(self):
        pass
    
    def struct_test(self):
        """
        Several struct functions (and methods of Struct) take a buffer argument.
        This refers to objects that implement the Buffer Protocol and provide 
        either a readable or read-writable buffer. The most common types used 
        for that purpose are bytes and bytearray, but many other types that can
        be viewed as an array of bytes implement the buffer protocol, so that 
        they can be read/filled without additional copying from a bytes object.
        """
        print('\n# exception struct.error')
        '''
        Exception raised on various occasions; argument is a string describing 
        what is wrong.
        '''
        
        print('\n# struct.pack(format, v1, v2, ...)')
        print('''
        Return a bytes object containing the values v1, v2, … packed according 
        to the format string format. The arguments must match the values 
        required by the format exactly.
        ''')
        # Format: h is short in C type 
        # Format: l is long in C type 
        # Format 'hhl' stands for 'short short long' 
        var = struct.pack('hhl',1,2,3) 
        print("struct.pack('hhl',1,2,3):", var) 

        # Format: i is int in C type 
        # Format 'iii' stands for 'int int int' 
        var = struct.pack('iii',1,2,3) 
        print("struct.pack('iii',1,2,3):", var)      
        
        print('\n# struct.pack_into(format, buffer, offset, v1, v2, ...)')
        print('''
        Pack the values v1, v2, … according to the format string format and 
        write the packed bytes into the writable buffer buffer starting at 
        position offset. Note that offset is a required argument.
        ''')
        # SIZE of the format is calculated using calcsize() 
        siz = struct.calcsize('hhl') 
        print("struct.calcsize('hhl'):", siz) 
          
        # Buffer 'buff' is created 
        buff = ctypes.create_string_buffer(siz) 
        print('ctypes.create_string_buffer(siz):', buff)
        
        # struct.pack() returns packed data 
        # struct.unpack() returns unpacked data 
        x = struct.pack('hhl', 2, 2, 3) 
        print("struct.pack('hhl', 2, 2, 3):", x) 
        print("struct.unpack('hhl', x):", struct.unpack('hhl', x)) 
          
        # struct.pack_into() packs data into buff, doesn't return any value 
        # struct.unpack_from() unpacks data from buff, returns a tuple of values 
        struct.pack_into('hhl', buff, 0, 2, 2, 3) 
        print(struct.unpack_from('hhl', buff, 0)) 
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    bds = BinaryDataServices()
    print(bds.__doc__)
    
    print('\n# struct — Interpret bytes as packed binary data')
    print(bds.struct_test.__doc__)
    bds.struct_test()