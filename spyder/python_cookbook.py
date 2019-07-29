# -*- coding: utf-8 -*-
"""
Created on Tue July 11 14:31:24 2019

@author: Rajesh Samui
"""
from collections import deque
import heapq
from pprint import pprint

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
        print('shares = {}, price = {}, _ = {}'.format(shares, price, _))
        
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
            
        print('*'*50)
        
        name, *_, (*_, year) = data
        print(data, 'name = {}, year = {}'.format(name, year), sep='\n')
        
        print('*'*50)
        
        items = [1, 10, 7, 4, 5, 9]
        head, *tail = items
        print('head: {}\ntail: {}'.format(head, tail))
        
        print('*'*50)
        def sum(items):
            head, *tail = items
            return head + sum(tail) if tail else head
        print(sum(items))
        
        print('\n# 1.3. Keeping the Last N Items')
        print('''
        Problem:
            You want to keep a limited history of the last few items seen 
            during iteration or during some other kind of processing.
        ''')
        def search(lines, pattern, history=5):
            previous_lines = deque(maxlen=history)
            for line in lines:
                if pattern in line:
                    yield line, previous_lines
                previous_lines.append(line)
                
        # Example use on a file
        with open('some_file.txt') as f:
            for line, prevlines in search(f, 'python', 5):
                for pline in prevlines:
                    print(pline, end='')
                print(line, end='')
                print('-'*20)
        print('*'*50)
        q = deque(maxlen=3)
        print('deque(maxlen=3):', q)
        [q.append(i) for i in range(3)]
        print('deque(maxlen=3):', q)
        q.append(3)
        print('deque(maxlen=3):', q)
        q.append(4)
        print('deque(maxlen=3):', q)
        print('*'*50)
        q = deque()
        print('deque():', q)
        [q.append(i) for i in range(3)]
        print('deque():', q)
        q.appendleft(4)
        print('deque():',q)
        print('q.pop():', q.pop())
        print('deque():',q)
        print('q.popleft():', q.popleft())
        print('deque():', q)
        print('''
        Adding or popping items from either end of a queue has O(1) complexity.
        This is unlike a list where inserting or removing items from the front 
        of the list is O(N).
        ''')
        print('\n# 1.4. Finding the Largest or Smallest N Items')
        print('''
        Problem:
            You want to make a list of the largest or smallest N items in a 
            collection.
        ''')
        nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
        print('heapq.nlargest(3, nums):', heapq.nlargest(3, nums)) # Prints [42, 37, 23]
        print('heapq.nsmallest(3, nums):', heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
        portfolio = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
        ]
        cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
        pprint(cheap)
        expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
        pprint(expensive)
        





if __name__ == '__main__':
    pcb = PythonCookBook()
    print(pcb.__doc__)
    
    print('\n# Data Structures and Algorithms')
    print(pcb.data_structures_algorithms.__doc__)
    pcb.data_structures_algorithms()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    