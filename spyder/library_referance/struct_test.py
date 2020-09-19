# -*- coding: utf-8 -*-
"""
Created on 14/09/2020
@author: Rajesh Samui
"""
import struct
import ctypes

class InterpretByteAsPackedBinaryData:
    """
    This module performs conversions between Python values and C structs represents as Python bytes objects. This can
    be used in handling binary data stored in files or form network connections, among other sources. It uses Format
    Strings as compact descriptions of the layout of the C structs and the intended conversion to/form Python value.
    """
    def __init__(self):
        pass

    def pack_test(self):
        """
        struct.pack(format,v1,v2, ...)
        Return a string containing the values v1, v2, that are packed according to the given format.
        """
        # Format: h is short in C type
        # Format: l is long in C type
        # Format 'hhl' stands for 'short short long'
        var = struct.pack('hhl', 1, 2, 3)
        print("pack('hhl', 1, 2, 3)",var)

        # Format: i is int in C type
        # Format 'iii' stands for 'int int int'
        var = struct.pack('iii', 1, 2, 3)
        print("pack('iii', 1, 2, 3)",var)
        return

    def pack_into_and_unpack_from_test(self):
        """
        pack_into(format, buffer, offset, v1, v2, ...)
        Pack the values v1, v2, ... according to format string and write the packed bytes into the writable buffer
        starting at position offset. Note that offset is a required argument.
        """
        # SIZE of the format is calculated using calcsize()
        siz = struct.calcsize('hhl')
        print("calcsize('hhl')",siz)

        # Buffer 'buff' is created
        buff = ctypes.create_string_buffer(siz)
        print("create_string_buffer(siz)",buff)

        # struct.pack_into() packs data into buff, doesn't return any value
        pi = struct.pack_into('hhl', buff, 0, 2, 2, 3)
        print("struct.pack_into('hhl', buff, 0, 2, 2, 3)",pi)

        # struct.unpack_from() unpacks data from buff, returns a tuple of values
        uf = struct.unpack_from('hhl', buff, 0)
        print("unpack_from('hhl', buff, 0)", uf)
        return

    def unpack_test(self):
        """
        unpack(format, buffer)
        Unpack from the buffer according to the from string format. The result is a tuple even if it contains exactly
        one item.
        """
        # '?' -> _BOOL , 'h' -> short, 'i' -> int and 'l' -> long
        var = struct.pack('?hil', True, 2, 5, 445)
        print("pack('?hil', True, 2, 5, 445)",var)

        # struct.unpack() return a tuples
        # Variables V1, V2, V3,.. are returned as elements of tuple
        tup = struct.unpack('?hil', var)
        print("unpack('?hil', var)",tup)

        # q -> long long int and f -> float
        var = struct.pack('qf', 5, 2.3)
        print("pack('qf', 5, 2.3)",var)
        tup = struct.unpack('qf', var)
        print("unpack('qf', var)",tup)
        return


if __name__ == '__main__':
    ibapbd = InterpretByteAsPackedBinaryData()
    print(ibapbd.__doc__)

    print('\n# pack(format, v1, v2, ...)')
    # ibapbd.pack_test()

    print('\n# pack_into(format, buffer, offset, v1, v2, ...)')
    # ibapbd.pack_into_and_unpack_from_test()

    print('\n# unpack(format, buffer)')
    # ibapbd.unpack_test()
