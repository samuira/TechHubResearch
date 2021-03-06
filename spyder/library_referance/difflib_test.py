# -*- coding: utf-8 -*-
"""
Created on Tue Apr 2 14:31:24 2019

@author: Rajesh Samui
"""
from difflib import ( SequenceMatcher, Differ, HtmlDiff, context_diff, 
                     get_close_matches, ndiff, restore, unified_diff, 
                     diff_bytes, IS_LINE_JUNK, IS_CHARACTER_JUNK)
from pprint import pprint
import sys
import keyword

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
        return
        
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
        The context diff format normally has a header for filenames and 
        modification times. Any or all of these may be specified using strings 
        for fromfile, tofile, fromfiledate, and tofiledate. The modification 
        times are normally expressed in the ISO 8601 format. If not specified, 
        the strings default to blanks.
        """
        s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
        s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
        sys.stdout.writelines(context_diff(s1, s2, fromfile='before.py', 
                                           tofile='after.py'))
        return
    
    def get_close_matches_test(self):
        """
        Return a list of the best “good enough” matches. word is a sequence for
        which close matches are desired (typically a string), and possibilities
        is a list of sequences against which to match word (typically a list of
        strings).
        Optional argument n (default 3) is the maximum number of close matches 
        to return; n must be greater than 0.
        Optional argument cutoff (default 0.6) is a float in the range [0, 1]. 
        Possibilities that don’t score at least that similar to word are 
        ignored.
        The best (no more than n) matches among the possibilities are returned 
        in a list, sorted by similarity score, most similar first.
        """
        print("get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy']):"
              ,get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy']))
        print("keyword.kwlist:",keyword.kwlist)
        print("get_close_matches('wheel', keyword.kwlist):",
              get_close_matches('wheel', keyword.kwlist))
        print("get_close_matches('pineapple', keyword.kwlist):",
              get_close_matches('pineapple', keyword.kwlist))
        print("get_close_matches('accept', keyword.kwlist):",
              get_close_matches('accept', keyword.kwlist, cutoff=0.6))
        return
    
    def ndiff_test(self):
        """
        Compare a and b (lists of strings); return a Differ-style delta (a 
        generator generating the delta lines).
        Optional keyword parameters linejunk and charjunk are filtering 
        functions (or None):
        linejunk: A function that accepts a single string argument, and returns
        true if the string is junk, or false if not. The default is None. There
        is also a module-level function IS_LINE_JUNK(), which filters out lines
        without visible characters, except for at most one pound character 
        ('#') – however the underlying SequenceMatcher class does a dynamic 
        analysis of which lines are so frequent as to constitute noise, and 
        this usually works better than using this function.
        charjunk: A function that accepts a character (a string of length 1), 
        and returns if the character is junk, or false if not. The default is 
        module-level function IS_CHARACTER_JUNK(), which filters out whitespace
        characters (a blank or tab; it’s a bad idea to include newline in 
        this!).
        Tools/scripts/ndiff.py is a command-line front-end to this function.
        """
        diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
                     'ore\ntree\nemu\n'.splitlines(keepends=True))
        print(''.join(diff), end="")
    
    def restore_test(self):
        """
        Return one of the two sequences that generated a delta.
        Given a sequence produced by Differ.compare() or ndiff(), extract lines
        originating from file 1 or 2 (parameter which), stripping off line 
        prefixes.
        """
        diff = ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
                     'ore\ntree\nemu\n'.splitlines(keepends=True))
        print(diff)
        diff = list(diff) # materialize the generated delta into a list
        print(diff)
        print(''.join(restore(diff, 1)), end="\n")
        print(''.join(restore(diff, 2)), end="")
        return
        
    def unified_diff_test(self):
        """
        Compare a and b (lists of strings); return a delta (a generator 
        generating the delta lines) in unified diff format.

        Unified diffs are a compact way of showing just the lines that have 
        changed plus a few lines of context. The changes are shown in an inline
        style (instead of separate before/after blocks). The number of context 
        lines is set by n which defaults to three.
        
        By default, the diff control lines (those with ---, +++, or @@) are 
        created with a trailing newline. This is helpful so that inputs created
        from io.IOBase.readlines() result in diffs that are suitable for use 
        with io.IOBase.writelines() since both the inputs and outputs have 
        trailing newlines.
        
        For inputs that do not have trailing newlines, set the lineterm 
        argument to "" so that the output will be uniformly newline free.
        
        The context diff format normally has a header for filenames and 
        modification times. Any or all of these may be specified using strings 
        for fromfile, tofile, fromfiledate, and tofiledate. The modification 
        times are normally expressed in the ISO 8601 format. If not specified, 
        the strings default to blanks.
        """
        s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
        s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
        print(s1, s2, sep='\n')
        sys.stdout.writelines(unified_diff(s1, s2, fromfile='before.py', 
                                           tofile='after.py'))
        return
    
    def diff_bytes_test(self):
        """
        Compare a and b (lists of bytes objects) using dfunc; yield a sequence 
        of delta lines (also bytes) in the format returned by dfunc. dfunc must
        be a callable, typically either unified_diff() or context_diff().
        Allows you to compare data with unknown or inconsistent encoding. All 
        inputs except n must be bytes objects, not str. Works by losslessly 
        converting all inputs (except n) to str, and calling dfunc(a, b, 
        fromfile, tofile, fromfiledate, tofiledate, n, lineterm). The output of
        dfunc is then converted back to bytes, so the delta lines that you 
        receive have the same unknown/inconsistent encodings as a and b.
        New in version 3.5.
        """
        a = [b'hello', b'andr\xe9']     # iso-8859-1 bytes
        b = [b'hello', b'andr\xc3\xa9'] # utf-8 bytes
        print(a, b, sep='\n')
        sys.stdout.writelines(diff_bytes(unified_diff, a, b, 
                                         fromfile=b'before.py', 
                                         tofile=b'after.py'))
        print('\n')
        sys.stdout.writelines(diff_bytes(context_diff, a, b, 
                                         fromfile=b'before.py', 
                                         tofile=b'after.py'))
        return
    
    def IS_LINE_JUNK_test(self):
        """
        Return true for ignorable lines. The line line is ignorable if line is 
        blank or contains a single '#', otherwise it is not ignorable. Used as 
        a default for parameter linejunk in ndiff() in older versions.
        """
        diff = ndiff('one\ntwo\nthree\n#\n'.splitlines(keepends=True),
                     'ore\ntree\nemu\n\n'.splitlines(keepends=True), 
                     linejunk=IS_LINE_JUNK)
        print(''.join(diff), end="")
        print("IS_LINE_JUNK('\\n'):",IS_LINE_JUNK('\n'))
        print("IS_LINE_JUNK('  #   \\n'):",IS_LINE_JUNK('  #   \n'))
        print("IS_LINE_JUNK('hello\\n'):",IS_LINE_JUNK('hello\n'))
        return
    
    def IS_CHARACTER_JUNK_test(self):
        """
        Return true for ignorable characters. The character ch is ignorable if 
        ch is a space or tab, otherwise it is not ignorable. Used as a default 
        for parameter charjunk in ndiff().
        """
        diff = ndiff('one\ntwo\nthree\n#\n'.splitlines(keepends=True),
                     'ore\ntree\nemu\n\n'.splitlines(keepends=True), 
                     charjunk=IS_CHARACTER_JUNK)
        print(''.join(diff), end="")
        print("IS_CHARACTER_JUNK(' '):",IS_CHARACTER_JUNK(' '))
        print("IS_CHARACTER_JUNK('\\t'):",IS_CHARACTER_JUNK('\t'))
        print("IS_CHARACTER_JUNK('\\n'):",IS_CHARACTER_JUNK('\n'))
        print("IS_CHARACTER_JUNK('x'):",IS_CHARACTER_JUNK('x'))
        return
    
    def sequence_matcher_objects_test(self):
        """
        # class difflib.SequenceMatcher(isjunk=None, a='', b='', autojunk=True)
        
        Optional argument isjunk must be None (the default) or a one-argument 
        function that takes a sequence element and returns true if and only if 
        the element is “junk” and should be ignored. Passing None for isjunk is
        equivalent to passing lambda x: 0; in other words, no elements are 
        ignored. For example, pass:
        
        lambda x: x in " \t"
        
        if you’re comparing lines as sequences of characters, and don’t want to
        synch up on blanks or hard tabs.
        
        The optional arguments a and b are sequences to be compared; both 
        default to empty strings. The elements of both sequences must be 
        hashable.
        
        The optional argument autojunk can be used to disable the automatic 
        junk heuristic.
        
        New in version 3.2: The autojunk parameter.
        
        SequenceMatcher objects get three data attributes: bjunk is the set of 
        elements of b for which isjunk is True; bpopular is the set of non-junk
        elements considered popular by the heuristic (if it is not disabled); 
        b2j is a dict mapping the remaining elements of b to a list of 
        positions where they occur. All three are reset whenever b is reset 
        with set_seqs() or set_seq2().
        
        New in version 3.2: The bjunk and bpopular attributes.
        
        SequenceMatcher objects have the following methods:
        """
        myStr1 = 'Python Programming'
        myStr2 = ' Python Standard Library'
        print('myStr1 = '+myStr1, 'myStr2 = '+myStr2, sep='\n')
        seq_match = SequenceMatcher()
        print('seq_match:', seq_match)
        
        print('\n# set_seqs(a, b)')
        print('''
        Set the two sequences to be compared.

        SequenceMatcher computes and caches detailed information about the 
        second sequence, so if you want to compare one sequence against many 
        sequences, use set_seq2() to set the commonly used sequence once and 
        call set_seq1() repeatedly, once for each of the other sequences.
        ''')
        seq_match.set_seqs(myStr1, myStr2)
        print('seq_match.find_longest_match(0, len(myStr1), 0, len(myStr2)):',
              seq_match.find_longest_match(0, len(myStr1), 0, len(myStr2)))
    
        print('\n# set_seq1(a)')
        '''
        Set the first sequence to be compared. The second sequence to be 
        compared is not changed.
        '''
        myStr3 = 'Programming in Python'
        print('myStr1 = '+myStr1, 'myStr2 = '+myStr2, 'myStr3 = '+myStr3, 
              sep='\n')
        seq_match.set_seq1(myStr3)
        print('seq_match.find_longest_match(0, len(myStr3), 0, len(myStr2)):',
              seq_match.find_longest_match(0, len(myStr3), 0, len(myStr2)))
        
        print('\n# set_seq2(b)')
        '''
        Set the second sequence to be compared. The first sequence to be 
        compared is not changed.
        '''
        myStr4 = 'A Sexy Programming Language is Python'
        print('myStr1 = '+myStr1, 'myStr2 = '+myStr2, 'myStr3 = '+myStr3, 
              'myStr4 = '+myStr4, sep='\n')
        seq_match.set_seq2(myStr4)
        print('seq_match.find_longest_match(0, len(myStr3), 0, len(myStr4)):',
              seq_match.find_longest_match(0, len(myStr3), 0, len(myStr4)))
        print('\n# find_longest_match(alo, ahi, blo, bhi)')
        print('''
        Find longest matching block in a[alo:ahi] and b[blo:bhi].

        If isjunk was omitted or None, find_longest_match() returns (i, j, k) 
        such that a[i:i+k] is equal to b[j:j+k], where alo <= i <= i+k <= ahi 
        and blo <= j <= j+k <= bhi. For all (i', j', k') meeting those 
        conditions, the additional conditions k >= k', i <= i', and if i == i',
        j <= j' are also met. In other words, of all maximal matching blocks, 
        return one that starts earliest in a, and of all those maximal matching
        blocks that start earliest in a, return the one that starts earliest in
        b.
        ''')
        s = SequenceMatcher(None, " abcd", "abcd abcd")
        print('SequenceMatcher(None, " abcd", "abcd abcd"):', s)
        print('s.find_longest_match(0, 5, 0, 9):', 
              s.find_longest_match(0, 5, 0, 9))
        
        print('''
        If isjunk was provided, first the longest matching block is determined 
        as above, but with the additional restriction that no junk element 
        appears in the block. Then that block is extended as far as possible by
        matching (only) junk elements on both sides. So the resulting block 
        never matches on junk except as identical junk happens to be adjacent 
        to an interesting match.

        Here’s the same example as before, but considering blanks to be junk. 
        That prevents ' abcd' from matching the ' abcd' at the tail end of the 
        second sequence directly. Instead only the 'abcd' can match, and 
        matches the leftmost 'abcd' in the second sequence:
        ''')
        s = SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
        print('SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd"):', s)
        print('s.find_longest_match(0, 5, 0, 9):', 
              s.find_longest_match(0, 5, 0, 9))
        
        print('''
        If no blocks match, this returns (alo, blo, 0).
        This method returns a named tuple Match(a, b, size).
        ''')        
        
        print('\n# get_matching_blocks()')
        print('''
        Return list of triples describing non-overlapping matching 
        subsequences. Each triple is of the form (i, j, n), and means that 
        a[i:i+n] == b[j:j+n]. The triples are monotonically increasing in i and
        j.
        
        The last triple is a dummy, and has the value (len(a), len(b), 0). It 
        is the only triple with n == 0. If (i, j, n) and (i', j', n') are 
        adjacent triples in the list, and the second is not the last triple in 
        the list, then i+n < i' or j+n < j'; in other words, adjacent triples 
        always describe non-adjacent equal blocks.
        ''')
        s = SequenceMatcher(None, "abxcd", "abcd")
        print('SequenceMatcher(None, "abxcd", "abcd"):', s)
        print('s.get_matching_blocks():', s.get_matching_blocks())
        
        print('\n# get_opcodes()')
        print('''
        Return list of 5-tuples describing how to turn a into b. Each tuple is 
        of the form (tag, i1, i2, j1, j2). The first tuple has i1 == j1 == 0, 
        and remaining tuples have i1 equal to the i2 from the preceding tuple, 
        and, likewise, j1 equal to the previous j2.

        The tag values are strings, with these meanings:
            Value               Meaning
            -------------------------------------------------------------------
            'replace'           a[i1:i2] should be replaced by b[j1:j2].
            'delete'            a[i1:i2] should be deleted. Note that j1 == j2 
                                in this case.
            'insert'            b[j1:j2] should be inserted at a[i1:i1]. Note 
                                that i1 == i2 in this case.
            'equal'             a[i1:i2] == b[j1:j2] (the sub-sequences are 
                                equal).
            -------------------------------------------------------------------
        ''')
        a = """qabxcd
xyaz
mnrp
eflh
ijpl
dfer
sdwe
mnrp
eflh
ijpl
dfer"""
        b = """abycd
xybz
mnsp
epmh
ijql
dftr
sdqe
mnsp
epmh
ijql
dftr"""
        print('a = '+ a, 'b = '+ b, sep='\n')
        s = SequenceMatcher(None, a, b)
        print('SequenceMatcher(None, a, b):', s)
        print('s.get_opcodes():', s.get_opcodes())
        for tag, i1, i2, j1, j2 in s.get_opcodes():
            print('{:10}   a[{:2}:{:2}] --> b[{:2}:{:2}] {!r:>7} --> {!r}'
                  .format(tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
            
        print('\n# get_grouped_opcodes(n=3)')
        print('''
        Return a generator of groups with up to n lines of context.

        Starting with the groups returned by get_opcodes(), this method splits 
        out smaller change clusters and eliminates intervening ranges which 
        have no changes.
    
        The groups are returned in the same format as get_opcodes().
        ''')
        s_gen0 = s.get_grouped_opcodes(n=0)
        [print('opcode0 l_{}:{}'.format(i, opcode0)) for i, opcode0 in 
         enumerate(s_gen0)]
        print()
        s_gen1 = s.get_grouped_opcodes(n=1)
        [print('opcode1 l_{}:{}'.format(i, opcode1)) for i, opcode1 in 
         enumerate(s_gen1)]
        print()
        s_gen2 = s.get_grouped_opcodes(n=2)
        [print('opcode2 l_{}:{}'.format(i, opcode2)) for i, opcode2 in 
         enumerate(s_gen2)]
        print()
        s_gen3 = s.get_grouped_opcodes(n=3)
        [print('opcode3 l_{}:{}'.format(i, opcode3)) for i, opcode3 in 
         enumerate(s_gen3)]
        print()
        s_gen4 = s.get_grouped_opcodes(n=4)
        [print('opcode4 l_{}:{}'.format(i, opcode4)) for i, opcode4 in 
         enumerate(s_gen4)]
        
        print('\n# ratio()')
        print('''
        Return a measure of the sequences’ similarity as a float in the range 
        [0, 1].

        Where T is the total number of elements in both sequences, and M is 
        the number of matches, this is 2.0*M / T. Note that this is 1.0 if the 
        sequences are identical, and 0.0 if they have nothing in common.

        This is expensive to compute if get_matching_blocks() or get_opcodes() 
        hasn’t already been called, in which case you may want to try 
        quick_ratio() or real_quick_ratio() first to get an upper bound.
        ''')
        sm = SequenceMatcher(None, "abcd", "bcde")
        print('SequenceMatcher(None, "abcd", "bcde"):', sm)
        print('sm.ratio():', sm.ratio())
        
        print('\n# quick_ratio()')
        print('''
        Return an upper bound on ratio() relatively quickly.
        ''')
        print('sm.quick_ratio():', sm.quick_ratio())
        
        print('\n# real_quick_ratio()')
        print('''
        Return an upper bound on ratio() very quickly.
        ''')
        print('sm.real_quick_ratio():',sm.real_quick_ratio())
    
    def sequence_matcher_examples(self):
        """
        This example compares two strings, considering blanks to be “junk”:
        """
        str1 = "private Thread currentThread;"
        str2 = "private volatile Thread currentThread;"
        print('str1 = '+str1, 'str2 = '+str2, sep='\n')
        sm = SequenceMatcher(lambda x: x == " ", str1, str2)
        print('SequenceMatcher(lambda x: x == " ", str1, str2):', sm)
        
        print('''
        ratio() returns a float in [0, 1], measuring the similarity of the 
        sequences. As a rule of thumb, a ratio() value over 0.6 means the 
        sequences are close matches:
        ''')
        print('round(sm.ratio(), 3):', round(sm.ratio(), 3))
        
        print('''
        If you’re only interested in where the sequences match, 
        get_matching_blocks() is handy:
        ''')
        print('sm.get_matching_blocks():', sm.get_matching_blocks())
        for block in sm.get_matching_blocks():
            print("block: a[%d] and b[%d] match for %d elements" % block)
        
        print('''
        Note that the last tuple returned by get_matching_blocks() is always a 
        dummy, (len(a), len(b), 0), and this is the only case in which the last
        tuple element (number of elements matched) is 0.

        If you want to know how to change the first sequence into the second, 
        use get_opcodes():
        ''')
        print('sm.get_opcodes():', sm.get_opcodes())
        for opcode in sm.get_opcodes():
            print("%6s a[%d:%d] b[%d:%d]" % opcode)
        return
    
    def differ_objects_test(self):
        """
        Note that Differ-generated deltas make no claim to be minimal diffs. To
        the contrary, minimal diffs are often counter-intuitive, because they 
        synch up anywhere possible, sometimes accidental matches 100 pages 
        apart. Restricting synch points to contiguous matches preserves some 
        notion of locality, at the occasional cost of producing a longer diff.

        The Differ class has this constructor:
        """
        print('\n# difflib.Differ(linejunk=None, charjunk=None)')
        print('''
        Optional keyword parameters linejunk and charjunk are for filter 
        functions (or None):
        
        linejunk: A function that accepts a single string argument, and returns
        true if the string is junk. The default is None, meaning that no line 
        is considered junk.
        
        charjunk: A function that accepts a single character argument (a string
        of length 1), and returns true if the character is junk. The default is
        None, meaning that no character is considered junk.
        
        These junk-filtering functions speed up matching to find differences 
        and do not cause any differing lines or characters to be ignored. Read 
        the description of the find_longest_match() method’s isjunk parameter 
        for an explanation.
        
        Differ objects are used (deltas generated) via a single method:
        ''')
        print('\n# compare(a, b)')
        print('''
        Compare two sequences of lines, and generate the delta (a sequence of 
        lines).

        Each sequence must contain individual single-line strings ending with 
        newlines. Such sequences can be obtained from the readlines() method of
        file-like objects. The delta generated also consists of 
        newline-terminated strings, ready to be printed as-is via the 
        writelines() method of a file-like object.
        ''')
        print('''
        This example compares two texts. First we set up the texts, sequences 
        of individual single-line strings ending with newlines (such sequences 
        can also be obtained from the readlines() method of file-like objects):
        ''')
        text1 = '''  1. Beautiful is better than ugly.
        2. Explicit is better than implicit.
        3. Simple is better than complex.
        4. Complex is better than complicated.'''.splitlines(keepends=True)
        print('text1 =', text1)
        print('len(text1):', len(text1))
        print('text1[0][-1]:', repr(text1[0][-1]))
        text2 = '''  1. Beautiful is better than ugly.
        3.   Simple is better than complex.
        4. Complicated is better than complex.
        5. Flat is better than nested.'''.splitlines(keepends=True)
        print('text2 =', text2)
        d = Differ()
        print('Differ():', d)
        print('''
        Note that when instantiating a Differ object we may pass functions to 
        filter out line and character “junk.” See the Differ() constructor for 
        details.

        Finally, we compare the two:
        ''')
        print('d.compare(text1, text2):', d.compare(text1, text2), end='\n\n')
        result = list(d.compare(text1, text2))
        print('list(d.compare(text1, text2)):', result)
        pprint(result)
        sys.stdout.writelines(result)
    
    
    
    
    
    
    
    
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
    
#    print("\n# difflib.context_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\\n')")
#    print(dl.context_diff_test.__doc__)
#    dl.context_diff_test()
    
#    print("\n# difflib.get_close_matches(word, possibilities, n=3, cutoff=0.6)")
#    print(dl.get_close_matches_test.__doc__)
#    dl.get_close_matches_test()
    
#    print("\n# difflib.ndiff(a, b, linejunk=None, charjunk=IS_CHARACTER_JUNK)")
#    print(dl.ndiff_test.__doc__)
#    dl.ndiff_test()
    
#    print("\n# difflib.restore(sequence, which)")
#    print(dl.restore_test.__doc__)
#    dl.restore_test()
    
#    print("\n# difflib.unified_diff(a, b, fromfile='', tofile='', fromfiledate='', tofiledate='', n=3, lineterm='\\n')")
#    print(dl.unified_diff_test.__doc__)
#    dl.unified_diff_test()
    
#    print("\n# difflib.diff_bytes(dfunc, a, b, fromfile=b'', tofile=b'', fromfiledate=b'', tofiledate=b'', n=3, lineterm=b'\\n')")
#    print(dl.diff_bytes_test.__doc__)
#    dl.diff_bytes_test()
    
#    print("\n# difflib.IS_LINE_JUNK(line)")
#    print(dl.IS_LINE_JUNK_test.__doc__)
#    dl.IS_LINE_JUNK_test()
#    
#    print("\n# difflib.IS_CHARACTER_JUNK(ch)")
#    print(dl.IS_CHARACTER_JUNK_test.__doc__)
#    dl.IS_CHARACTER_JUNK_test()
    
#    print('\n# SequenceMatcher Objects')
#    print(dl.sequence_matcher_objects_test.__doc__)
#    dl.sequence_matcher_objects_test()
    
#    print('\n# SequenceMatcher Examples')
#    print(dl.sequence_matcher_examples.__doc__)
#    dl.sequence_matcher_examples()
    
    print('\n# Differ Objects')
    print(dl.differ_objects_test.__doc__)
    dl.differ_objects_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    