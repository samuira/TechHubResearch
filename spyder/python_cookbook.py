# -*- coding: utf-8 -*-
"""
Created on Tue July 11 14:31:24 2019

@author: Rajesh Samui
"""
from collections import deque, defaultdict, OrderedDict
import heapq
from pprint import pprint
import json

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
        pprint(portfolio)
        print()
        cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
        pprint(cheap)
        print()
        expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
        pprint(expensive)
        
        print('*'*50)
        print('nums =', nums)
        heapq.heapify(nums)
        print('nums =', nums)
        print('heapq.heappop(nums):', heapq.heappop(nums))
        print('nums =', nums)
        print('heapq.heappop(nums):', heapq.heappop(nums))
        print('nums =', nums)
        print('heapq.heappop(nums):', heapq.heappop(nums))
        print('nums =', nums)
        print('heapq.heappop(nums):', heapq.heappop(nums))
        print('nums =', nums)
        print('heapq.heappop(nums):', heapq.heappop(nums))
        print('''
        The most important feature of a heap is that heap[0] is always the 
        smallest item. Moreover, subsequent items can be easily found using the
        heapq.heappop() method, which pops off the first item and replaces it 
        with the next smallest item (an operation that requires O(log N) 
        operations where N is the size of the heap). For example, to find the
        three smallest items, you would do this.
        ''')
        print('\n# 1.5. Implementing a Priority Queue')
        print('''
        Problem:
            You want to implement a queue that sorts items by a given priority 
            and always returns the item with the highest priority on each pop 
            operation.
        ''')
        class PriorityQueue:
            def __init__(self):
                self._queue = []
                self._index = 0
            def push(self, item, priority):
                heapq.heappush(self._queue, (-priority, self._index, item))
                self._index += 1
            def pop(self):
                return heapq.heappop(self._queue)[-1]
            
        class Item:
            def __init__(self, name):
                self.name = name
            def __repr__(self):
                return 'Item({!r})'.format(self.name)
        
        q = PriorityQueue()
        print('PriorityQueue():', PriorityQueue())
        q.push(Item('foo'), 1)
        q.push(Item('bar'), 5)
        q.push(Item('spam'), 4)
        q.push(Item('grok'), 1)
        print('q.pop():', q.pop())
        print('q.pop():', q.pop())
        print('q.pop():', q.pop())
        print('q.pop():', q.pop())
        
        print('*'*50)
        a = Item('foo')
        b = Item('bar')
        print(a, b, 'a < b', sep='\n')
        try:
            a < b
        except Exception as e:
            print(type(e), e)
        
        print('*'*50)
        a = (1, Item('foo'))
        b = (5, Item('bar'))
        print(a, b, sep='\n')
        print('a < b:', a < b)
        c = (1, Item('grok'))
        try:
            print('a < c:', a < c)
        except Exception as e:
            print(type(e), e)
            
        print('*'*50)
        a = (1, 0, Item('foo'))
        b = (5, 1, Item('bar'))
        c = (1, 2, Item('grok'))
        print(a, b, c, sep='\n')
        print('a < b', a<b)
        print('a < c', a<c)
        
        print('\n# 1.6. Mapping Keys to Multiple Values in a Dictionary')
        print('''
        Problem:
            You want to make a dictionary that maps keys to more than one value
            (a so-called “multidict”).
        ''')
        d = defaultdict(list)
        print('defaultdict(list):', d)
        d['a'].append(1)
        d['a'].append(2)
        d['b'].append(4)
        print('defaultdict(list):', d)
        
        print('*'*50)
        
        d = defaultdict(set)
        print('defaultdict(set):', d)
        d['a'].add(1)
        d['a'].add(2)
        d['b'].add(4)
        print('defaultdict(set):', d)
        
        print('*'*50)
        d = {}    # A regular dictionary
        print('d =', d)
        d.setdefault('a', []).append(1)
        d.setdefault('a', []).append(2)
        d.setdefault('b', []).append(4)
        print('d =', d)
        
        print('*'*50)
        
        print('\n# 1.7. Keeping Dictionaries in Order')
        print('''
        Problem:
            You want to create a dictionary, and you also want to control the 
            order of items when iterating or serializing.
        ''')
        d = OrderedDict()
        print('d =', d)
        d['foo'] = 1
        d['bar'] = 2
        d['spam'] = 3
        d['grok'] = 4
        print('d =', d)
        [print(k, v, sep=':') for k, v in d.items()]
        print('''
        An OrderedDict can be particularly useful when you want to build a 
        mapping that you may want to later serialize or encode into a different
        format. For example, if you want to precisely control the order of 
        fields appearing in a JSON encoding, first building the data in an 
        OrderedDict will do the trick.
        ''')
        print('json.dumps(d):', json.dumps(d))
        print('''
        An OrderedDict internally maintains a doubly linked list that orders 
        the keys according to insertion order. When a new item is first 
        inserted, it is placed at the end of this list. Subsequent reassignment
        of an existing key doesn’t change the order.
        ''')
        
        print('\n# 1.8. Calculating with Dictionaries')
        print('''
        Problem:
            You want to perform various calculations (e.g., minimum value, 
            maximum value, sort‐ing, etc.) on a dictionary of data.
        ''')
        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }
        print('prices =',prices)
        print('min(zip(prices.values(), prices.keys())):', 
              min(zip(prices.values(), prices.keys())))
        print('max(zip(prices.values(), prices.keys())):', 
              max(zip(prices.values(), prices.keys())))
        pprint(sorted(zip(prices.values(), prices.keys())))
        print('''
        When doing these calculations, be aware that zip() creates an iterator 
        that can only be consumed once.
        ''')
        prices_and_names = zip(prices.values(), prices.keys())
        print(min(prices_and_names)) # OK
        try:
            print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
        except Exception as e:
            print(type(e), e)
            
        print('min(prices):', min(prices))
        print('max(prices):', max(prices))
        print('min(prices.values()):', min(prices.values()))
        print('max(prices.values()):', max(prices.values()))
        
        print('min(prices, key=lambda k: prices[k]):', 
                   min(prices, key=lambda k: prices[k]))
        print('max(prices, key=lambda k: prices[k]):', 
                   max(prices, key=lambda k: prices[k]))
        min_value = prices[min(prices, key=lambda k: prices[k])]
        print('min_value:', min_value)
        print('''
        It should be noted that in calculations involving (value, key) pairs, 
        the key will be used to determine the result in instances where 
        multiple entries happen to have the same value. For instance, in 
        calculations such as min() and max() , the entry with the smallest or 
        largest key will be returned if there happen to be duplicate values.
        ''')
        prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
        pprint(prices)
        print('min(zip(prices.values(), prices.keys())):', 
              min(zip(prices.values(), prices.keys())))
        print('max(zip(prices.values(), prices.keys())):', 
              max(zip(prices.values(), prices.keys())))
        
        print('\n# 1.9. Finding Commonalities in Two Dictionaries')
        print('''
        Problem:
            You have two dictionaries and want to find out what they might have
            in common (same keys, same values, etc.).
        ''')
        a = {'x' : 1, 'y' : 2, 'z' : 3}
        b = {'w' : 10, 'x' : 11, 'y' : 2}
        print('a.keys() & b.keys():', a.keys() & b.keys())
        print('a.keys() | b.keys():', a.keys() | b.keys())
        print('a.keys() - b.keys():', a.keys() - b.keys())
        print('a.items() & b.items():', a.items() & b.items())
        c = {key:a[key] for key in a.keys() - {'z', 'w'}}
        pprint(c)
        
        print('\n# 1.10. Removing Duplicates from a Sequence while Maintaining Order')
        print('''
        Problem:
            You want to eliminate the duplicate values in a sequence, but 
            preserve the order of the remaining items.
        ''')
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)
                    
        a = [1, 5, 2, 1, 9, 1, 5, 10]
        print(list(dedupe(a)))
        
        
        
        

if __name__ == '__main__':
    pcb = PythonCookBook()
    print(pcb.__doc__)
    
    print('\n# Data Structures and Algorithms')
    print(pcb.data_structures_algorithms.__doc__)
    pcb.data_structures_algorithms()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    