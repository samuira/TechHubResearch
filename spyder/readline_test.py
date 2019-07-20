# -*- coding: utf-8 -*-
"""
Created on Tue July 17 14:31:24 2019

@author: Rajesh Samui
"""
import readline

class GNUReadlineInterface:
    """
    The readline module defines a number of functions to facilitate completion 
    and reading/writing of history files from the Python interpreter. This 
    module can be used directly, or via the rlcompleter module, which supports 
    completion of Python identifiers at the interactive prompt. Settings made 
    using this module affect the behaviour of both the interpreter’s 
    interactive prompt and the prompts offered by the built-in input() function.
    
    Readline keybindings may be configured via an initialization file, 
    typically .inputrc in your home directory. See Readline Init File in the 
    GNU Readline manual for information about the format and allowable 
    constructs of that file, and the capabilities of the Readline library in 
    general.
    
    Note:
    The underlying Readline library API may be implemented by the libedit 
    library instead of GNU readline. On macOS the readline module detects which
    library is being used at run time.
    
    The configuration file for libedit is different from that of GNU readline. 
    If you programmatically load configuration strings you can check for the 
    text “libedit” in readline.__doc__ to differentiate between GNU readline 
    and libedit.
    
    If you use editline/libedit readline emulation on macOS, the initialization
    file located in your home directory is named .editrc. For example, the 
    following content in ~/.editrc will turn ON vi keybindings and TAB 
    completion:
    
    python:bind -v
    python:bind ^I rl_complete
    """
    def __init__(self):
        pass
    
    def init_file_test(self):
        """
        The following functions relate to the init file and user configuration:
        """
        print('\n# readline.parse_and_bind(string)')
        print('''
        Execute the init line provided in the string argument. This calls 
        rl_parse_and_bind() in the underlying library.
        ''')
        readline.parse_and_bind('tab: complete')
        readline.parse_and_bind('set editing-mode vi')
        
        while True:
            line = input('Prompt ("stop" to quit): ')
            if line == 'stop':
                break
            print('ENTERED: "%s"' % line)
            
        print('\n# readline.read_init_file([filename])')
        print('''
        Execute a readline initialization file. The default filename is the 
        last filename used. This calls rl_read_init_file() in the underlying 
        library.
        ''')
        
        return
    
    def line_buffer_test(self):
        """
        
        """
        pass
        
    
    
    
    
    
if __name__ == '__main__':
    gri = GNUReadlineInterface()
    print(gri.__doc__)
    
#    print('\n# Init file')
#    print(gri.init_file_test.__doc__)
#    gri.init_file_test()
    
    print('\n# Line buffer')
    print(gri.line_buffer_test.__doc__)
    gri.line_buffer_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    