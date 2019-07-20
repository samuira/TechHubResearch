# -*- coding: utf-8 -*-
"""
Created on Tue July 11 14:31:24 2019

@author: Rajesh Samui
"""

class PythonCookBook:
    """
    
    """
    def __init__(self):
        pass
    
    def data_structures_algorithms(self):
        """
        Python provides a variety of useful built-in data structures, such as 
        lists, sets, and dictionaries. For the most part, the use of these 
        structures is straightforward. However, common questions concerning 
        searching, sorting, ordering, and filtering often arise. Thus, the goal
        of this chapter is to discuss common data structures and algorithms
        involving data. In addition, treatment is given to the various data 
        structures contained in the collections module.
        """
        print('\n# 1.1. Unpacking a Sequence into Separate Variables')
        print('''
        Problem:
            You have an N-element tuple or sequence that you would like to 
            unpack into a collection of N variables.
        ''')
        p = (4, 5)
        x, y = p
        print('x = {}, y = {}'.format(x,y))
        data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
        name, shares, price, date = data
        print('name: {}'.format(name))
        print('data: {}'.format(date))
        name, shares, price, (year, month, day) = data
        print('name: {}'.format(name))
        print('day: {}'.format(day))
        try:
            x, y, z = p
        except Exception as e:
            print(type(e), e)
            
        s = 'Hello'
        a, b, c, d, e = s
        print('a = {}'.format(a))
        _, shares, price, _ = data
        print('shares = {}, price = {}'.format(shares, price))
        
        print('\n# 1.2. Unpacking Elements from Iterables of Arbitrary Length')
        print('''
        Problem:
            You need to unpack N elements from an iterable, but the iterable 
            may be longer than N elements, causing a “too many values to 
            unpack” exception.
        ''')
        record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
        name, email, *phone_number = record
        print('name = {}, phone_number = {}'.format(name, phone_number))
            





if __name__ == '__main__':
    pcb = PythonCookBook()
    print(pcb.__doc__)
    
    print('\n# Data Structures and Algorithms')
    print(pcb.data_structures_algorithms.__doc__)
    pcb.data_structures_algorithms()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    