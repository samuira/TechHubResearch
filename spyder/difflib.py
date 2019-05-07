# -*- coding: utf-8 -*-
"""
Created on Tue Apr 2 14:31:24 2019

@author: Rajesh Samui
"""
from difflib import SequenceMatcher, Differ, HtmlDiff, context_diff
from pprint import pprint

class Difflib:
    """
    This module provides classes and functions for comparing sequences. It can 
    be used for example, for comparing files, and can produce difference 
    information in various formats, including HTML and context and unified 
    diffs. For comparing directories and files, see also, the filecmp module.
    """
    def __init__(self):
        pass
    
    def sequence_matcher_test(self):
        """
        The idea is to find the longest contiguous matching subsequence that 
        contains no “junk” elements; these “junk” elements are ones that are 
        uninteresting in some sense, such as blank lines or whitespace. 
        (Handling junk is an extension to the Ratcliff and Obershelp algorithm.
        ) The same idea is then applied recursively to the pieces of the 
        sequences to the left and to the right of the matching subsequence.
        Timing: 
            The basic Ratcliff-Obershelp algorithm is cubic time in the worst 
            case and quadratic time in the expected case. SequenceMatcher is 
            quadratic time for the worst case and has expected-case behavior 
            dependent in a complicated way on how many elements the sequences 
            have in common; best case time is linear.
        Automatic junk heuristic: 
            SequenceMatcher supports a heuristic that automatically treats 
            certain sequence items as junk. The heuristic counts how many times
            each individual item appears in the sequence. If an item’s 
            duplicates (after the first one) account for more than 1% of the 
            sequence and the sequence is at least 200 items long, this item is 
            marked as “popular” and is treated as junk for the purpose of 
            sequence matching. This heuristic can be turned off by setting the 
            autojunk argument to False when creating the SequenceMatcher. 
               
        """
        s = SequenceMatcher(lambda x: x == " ",
        "private Thread currentThread;",
        "private volatile Thread currentThread;")
        
        print("'{:%}'.format(round(s.ratio(), 3)):",
        '{:%}'.format(round(s.ratio(), 3)))
        
        print('s.get_matching_blocks():',s.get_matching_blocks())
        for block in s.get_matching_blocks():
            print("a[%d] and b[%d] match for %d elements" % block)
            
        s = SequenceMatcher(None, " abcd", "abcd abcd")
        print('s.find_longest_match(0, 5, 0, 9):',
              s.find_longest_match(0, 5, 0, 9))
        """
        Methods:

        __init__(isjunk=None, a='', b='')
            Construct a SequenceMatcher.
            Optional arg isjunk is None (the default), or a one-argument
            function that takes a sequence element and returns true iff the
            element is junk.  None is equivalent to passing "lambda x: 0", i.e.
            no elements are considered to be junk.  For example, pass
            lambda x: x in " \t"
        
        set_seqs(a, b)
            Set the two sequences to be compared.
        
        set_seq1(a)
            Set the first sequence to be compared.
        
        set_seq2(b)
            Set the second sequence to be compared.
        
        find_longest_match(alo, ahi, blo, bhi)
            Find longest matching block in a[alo:ahi] and b[blo:bhi].
        
        get_matching_blocks()
            Return list of triples describing matching subsequences.
        
        get_opcodes()
            Return list of 5-tuples describing how to turn a into b.
        
        ratio()
            Return a measure of the sequences' similarity (float in [0,1]).
        
        quick_ratio()
            Return an upper bound on .ratio() relatively quickly.
        
        real_quick_ratio()
            Return an upper bound on ratio() very quickly.
        """
        print('\n# set_seqs(self, a, b)')
        s = SequenceMatcher()
        s.set_seqs("abcd", "bcde")
        print('s.ratio():',s.ratio())
        
        print('\n# set_seq1(self, a)')
        s = SequenceMatcher(None, "abcd", "bcde")
        print('s.ratio():',s.ratio())
        s.set_seq1("bcde")
        print('s.ratio():',s.ratio())
        
        print('\n# set_seq2(self, b)')
        s = SequenceMatcher(None, "abcd", "bcde")
        print('s.ratio():',s.ratio())
        s.set_seq2("abcd")
        print('s.ratio():',s.ratio())
        
        print('\n# find_longest_match(self, alo, ahi, blo, bhi)')
        a = " abcd"
        b = "abcd abcd"
        s = SequenceMatcher(None, a, b)
        i,j,k = s.find_longest_match(0, 5, 0, 9)
        print('i = {}, j = {}, k = {}'.format(i,j,k))
        print('a[i:i+k]:',a[i:i+k])
        
        a = " abcd"
        b = "abcd abcd"
        # space will be ignor. as isjunk -> lambda x: x==" "
        s = SequenceMatcher(lambda x: x==" ", a, b)
        i,j,k = s.find_longest_match(0, 5, 0, 9)
        print('i = {}, j = {}, k = {}'.format(i,j,k))
        print('a[i:i+k]:',a[i:i+k])
        
        a = "ab"
        b = "c"
        s = SequenceMatcher(None, a, b)
        i,j,k = s.find_longest_match(0, 2, 0, 1)
        print('i = {}, j = {}, k = {}'.format(i,j,k))
        print('a[i:i+k]:',a[i:i+k])
        
        print('\n# get_matching_blocks(self)')
        a = "abxcd"
        b = "abcd"
        s = SequenceMatcher(None, a, b)
        ml = s.get_matching_blocks()
        [print('matched:',a[i:i+k]) for i,j,k in ml]
        
        print('\n# get_opcodes(self)')
        a = "qabxcd"
        b = "abycdf"
        s = SequenceMatcher(None, a, b)
        for tag, i1, i2, j1, j2 in s.get_opcodes():
            print("%7s a[%d:%d] (%s) b[%d:%d] (%s)" %(tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2]))
            
        print('\n# get_grouped_opcodes(self, n=3)')
        a = list(map(str, range(1,40)))
        b = a[:]
        b[8:8] = ['i']     # Make an insertion
        b[20] += 'x'       # Make a replacement
        b[23:28] = []      # Make a deletion
        b[30] += 'y'       # Make another replacement
        print('a =',a)
        print('b =',b)
        ggo = SequenceMatcher(None,a,b).get_grouped_opcodes()
        [print("%7s a[%d:%d] (%s) b[%d:%d] (%s)" %
               (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2])) for obj in ggo 
               for tag,i1,i2,j1,j2 in obj]
               
        print('\n# ratio(self)')
        s = SequenceMatcher(None, "abcd", "bcde")
        print('s.ratio():',s.ratio())
        
        print('\n# quick_ratio(self)')
        print('s.quick_ratio():',s.quick_ratio())
        
        print('\n# real_quick_ratio(self)')
        print('s.real_quick_ratio():',s.real_quick_ratio())
        
    def differ_test(self):
        """
        This is a class for comparing sequences of lines of text, and producing
        human-readable differences or deltas. Differ uses SequenceMatcher both 
        to compare sequences of lines, and to compare sequences of characters 
        within similar (near-matching) lines.
        Each line of a Differ delta begins with a two-letter code:
        Code 	Meaning
        '- ' 	line unique to sequence 1
        '+ ' 	line unique to sequence 2
        '  ' 	line common to both sequences
        '? ' 	line not present in either input sequence
        Lines beginning with ‘?’ attempt to guide the eye to intraline 
        differences, and were not present in either input sequence. These lines
        can be confusing if the sequences contain tab characters.
        """
        text1 = '''  1. Beautiful is better than ugly.
                2. Explicit is better than implicit.
                3. Simple is better than complex.
                4. Complex is better than complicated.'''.splitlines(1)
        print('len(text1):',len(text1))
        print('text1[0][-1]:',repr(text1[0][-1]))
        
        text2 = '''  1. Beautiful is better than ugly.
                3.   Simple is better than complex.
                4. Complicated is better than complex.
                5. Flat is better than nested.'''.splitlines(1)
                
        d = Differ()
        result = list(d.compare(text1, text2))
        pprint(result)
        print(''.join(result))
        
        
        print('\n# __init__(self, linejunk=None, charjunk=None')
        '''
        Construct a text differencer, with optional filters.
        '''
        
        print('\n# compare(self, a, b)')
        '''
        Compare two sequences of lines; generate the resulting delta.
        Each sequence must contain individual single-line strings ending with 
        newlines. Such sequences can be obtained from the `readlines()` method 
        of file-like objects. The delta generated also consists of newline- 
        terminated strings, ready to be printed as-is via the writeline() 
        method of a file-like object.
        '''
        pprint(list(Differ().compare('one\ntwo\nthree\n'.splitlines(1),
        'ore\ntree\nemu\n'.splitlines(1))))
        
        print('\n# _fancy_replace(self, a, alo, ahi, b, blo, bhi)')
        '''
        When replacing one block of lines with another, search the blocks for 
        *similar* lines; the best-matching pair (if any) is used as a synch 
        point, and intraline difference marking is done on the similar pair. 
        Lots of work, but often worth it.
        '''
        d = Differ()
        results = d._fancy_replace(['abcDefghiJkl\n'], 0, 1,['abcdefGhijkl\n'],
                                   0, 1)
        print(''.join(results))
        
        print('\n# _qformat(self, aline, bline, atags, btags)')
        # Format "?" output and deal with leading tabs.
        d = Differ()
        results = d._qformat('\tabcDefghiJkl\n', '\t\tabcdefGhijkl\n',
        '  ^ ^  ^      ', '+  ^ ^  ^      ')
        for line in results: print(repr(line))
        return
        
    def html_diff_test(self):
        """
        This class can be used to create an HTML table (or a complete HTML file
        containing the table) showing a side by side, line by line comparison 
        of text with inter-line and intra-line change highlights. The table can
        be generated in either full or contextual difference mode.
        """
        print('\n# __init__(tabsize=8, wrapcolumn=None, linejunk=None, charjunk=IS_CHARACTER_JUNK)')
        '''
        tabsize is an optional keyword argument to specify tab stop spacing and
        defaults to 8.
        wrapcolumn is an optional keyword to specify column number where lines 
        are broken and wrapped, defaults to None where lines are not wrapped.
        linejunk and charjunk are optional keyword arguments passed into 
        ndiff() (used by HtmlDiff to generate the side by side HTML differences
        ). See ndiff() documentation for argument default values and 
        descriptions.
        '''
        
        print("\n# make_file(fromlines, tolines, fromdesc='', todesc='', context=False, numlines=5, *, charset='utf-8')")
        '''
        Compares fromlines and tolines (lists of strings) and returns a string 
        which is a complete HTML file containing a table showing line by line 
        differences with inter-line and intra-line changes highlighted.
        fromdesc and todesc are optional keyword arguments to specify from/to 
        file column header strings (both default to an empty string).    
        context and numlines are both optional keyword arguments. Set context 
        to True when contextual differences are to be shown, else the default 
        is False to show the full files. numlines defaults to 5. When context 
        is True numlines controls the number of context lines which surround 
        the difference highlights. When context is False numlines controls the 
        number of lines which are shown before a difference highlight when 
        using the “next” hyperlinks (setting to zero would cause the “next” 
        hyperlinks to place the next difference highlight at the top of the 
        browser without any leading context).
        Changed in version 3.5: charset keyword-only argument was added. The 
        default charset of HTML document changed from 'ISO-8859-1' to 'utf-8'.
        '''
        before = ['abc\n', 'def\n', 'mno\n']
        after = ['xyz\n', 'def\n', 'mnop\n']
        print(HtmlDiff().make_file(before, after))
        
        print('\n# make_table(fromlines, tolines, fromdesc='', todesc='', context=False, numlines=5)')
        '''
        Compares fromlines and tolines (lists of strings) and returns a string 
        which is a complete HTML table showing line by line differences with 
        inter-line and intra-line changes highlighted.
        The arguments for this method are the same as those for the make_file()
        method.
        '''
        print(HtmlDiff().make_table(before, after))
        
    def context_diff_test(self):
        """
        Compare a and b (lists of strings); return a delta (a generator 
        generating the delta lines) in context diff format.
        Context diffs are a compact way of showing just the lines that have 
        changed plus a few lines of context. The changes are shown in a 
        before/after style. The number of context lines is set by n which 
        defaults to three.
        By default, the diff control lines (those with *** or ---) are created 
        with a trailing newline. This is helpful so that inputs created from 
        io.IOBase.readlines() result in diffs that are suitable for use with 
        io.IOBase.writelines() since both the inputs and outputs have trailing 
        newlines.
        For inputs that do not have trailing newlines, set the lineterm 
        argument to "" so that the output will be uniformly newline free.

        The context diff format normally has a header for filenames and modification times. Any or all of these may be specified using strings for fromfile, tofile, fromfiledate, and tofiledate. The modification times are normally expressed in the ISO 8601 format. If not specified, the strings default to blanks.
        """
        before = ['abc\n', 'def\n', 'mno\n']
        after = ['xyz\n', 'def\n', 'mnop\n']
        print(context_diff(before, after))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    dl = Difflib()
    print(dl.__doc__)
    
#    print('\n# difflib.SequenceMatcher')
#    print(dl.sequence_matcher_test.__doc__)
#    dl.sequence_matcher_test()

#    print('\n# difflib.Differ')
#    print(dl.differ_test.__doc__)
#    dl.differ_test()

#    print('\n# difflib.HtmlDiff')
#    print(dl.html_diff_test.__doc__)
#    dl.html_diff_test()
    
    print("\n# difflib.context_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\\n')")
    print(dl.context_diff_test.__doc__)
    dl.context_diff_test()