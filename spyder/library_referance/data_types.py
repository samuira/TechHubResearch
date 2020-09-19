# -*- coding: utf-8 -*-
"""
Created on Tue August 6 14:31:24 2019

@author: Rajesh Samui
"""
from datetime import datetime

class DataTypes:
    """
    
    """
    def __init__(self):
        pass
    
    def datetime_test(self):
        """
        There are two kinds of date and time objects: “naive” and “aware”.

        An aware object has sufficient knowledge of applicable algorithmic and 
        political time adjustments, such as time zone and daylight saving time 
        information, to locate itself relative to other aware objects. An aware 
        object is used to represent a specific moment in time that is not open 
        to interpretation 1.
    
        A naive object does not contain enough information to unambiguously 
        locate itself relative to other date/time objects. Whether a naive 
        object represents Coordinated Universal Time (UTC), local time, or time
        in some other timezone is purely up to the program, just like it is up 
        to the program whether a particular number represents metres, miles, or
        mass. Naive objects are easy to understand and to work with, at the 
        cost of ignoring some aspects of reality.
        """
        print('datetime.now():', datetime.now())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__=='__main__':
    dt = DataTypes()
    print(dt.__doc__)
    
    print('\n# Basic date and time types')
    print(dt.datetime_test.__doc__)
    dt.datetime_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
