# -*- coding: utf-8 -*-
"""
Created on 14/09/2020
@author: Rajesh Samui
"""
import rlcompleter


class CompletionFunctionForGNU:
    """
    The rlcompleter module defines a completion function suitable for the readline module by completing valid python
    identifiers and keywords.
    When this module is imported on a unix platform with the readline module available, an instance of the Completer
    class is automatically created and its complete() method is set as the readline completer.
    """

    def __init__(self):
        pass


if __name__ == '__main__':
    cffgnu = CompletionFunctionForGNU()
    print(cffgnu.__doc__)
