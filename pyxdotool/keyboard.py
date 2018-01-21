#!/usr/bin/env python
"""
    pyxdotool
        pyxdotool is a python wrapper for using xdotool as a
        python module.

        Written by: Shane Hutter
        
        Required Dependancies: python >= 3.5, xdotool

        This python script, and all of pyxdotool is licensed
        under the GNU GPL version 3

        pyxdotool is free software; you can redistribute it and/or modify
        it under the terms of the GNU Lesser General Public License as published
        by the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        pyxdotool is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
        GNU Lesser General Public License for more details.
        You should have received a copy of the GNU Lesser General Public License
        along with this program. If not, see <http://www.gnu.org/licenses/>.  
"""

from . import shell



# Declare constants
KEY_COMMAND = 'xdotool key --delay 1 '



def xdotoolKey( key = '' ):
    """Retun an xdotool key name from an ascii key"""

    # Dictionary of char to xdotool key
    xdotoolKeys = {
        '@':    'at' ,
        '&':    'ampersand' ,
        '^':    'asciicircum' , # Caret
        '~':    'asciitilde' ,
        '*':    'asterisk' ,
        '\\':   'backslash' ,
        '\b':   'BackSpace' ,
        '|':    'bar' ,         # Pipe
        '{':    'braceleft' ,
        '}':    'braceright' ,
        '[':    'bracketleft' ,
        ']':    'bracketright' ,
        ',':    'comma' ,
        ':':    'colon' ,
        '$':    'dollar' ,
        '=':    'equal' ,
        '!':    'exclam' ,
        '>':    'greater' ,
        '<':    'less' ,
        '-':    'minus' ,
        '#':    'numbersign' ,
        '(':    'parenleft' ,
        ')':    'parenright' ,
        '%':    'percent' ,
        '.':    'period' ,
        '+':    'plus' ,
        '?':    'question' ,
        '\"':   'quotedbl' ,
        '\'':   'quoteright' ,
        '`':    'quoteleft' ,   # Backtick
        '\n':   'Return' ,
        ';':    'semicolon' ,
        '/':    'slash' ,
        ' ':    'space' ,
        '\t':   'Tab' ,
        '_':    'underscore' ,
        }

    if key in xdotoolKeys:
        return xdotoolKeys[key]
    else:
        return key



def typeKeys( keyString = "" ):
    """ Convert a string into xdotool key commands"""
    
    # Type the keys in the string with xdotool
    keyTyped = []
    for key in keyString:
        keyTyped.append(
                shell(
                    KEY_COMMAND + 
                    xdotoolKey(key)
                    )
                )

    # Return true if all keystrokes are a success
    if False in keyTyped:
        return False
    else:
        return True

'''
    Create these functions:
        typeFKey( fKeyNumber = 0 )
        holdFKey( fKeyNumber = 0 )
        releaseFKey( fKeyNumber = 0 )
        altFKey( fKeyNumber = 0 )
        ctrlFKey( fKeyNumber = 0 )
        metaFKey( fKeyNumber = 0 )
        superFKey( fKeyNumber = 0 )
        
        typeAltKey( amount = 1 )
        holdAltKey()
        releaseAltKey()
        combineAltKey( key = '' )
        
        typeCtrlKey( amount = 1 )
        holdCtrlKey()
        releaseCtrlKey()
        combineCtrlKey( key = '' )
        
        typeEnterKey( amount = 1 )
        holdEnterKey()
        releaseEnterKey()

        typeMetaKey( amount = 1 )
        holdMetaKey()
        releaseMetaKey()
        combineMetaKey( key = '' )
        
        typeSuperKey( amount = 1 )
        holdSuperKey
        releaseSuperKey
        combineSuperKey( key = '' )


        etc...
'''


def typeFKey( fKeyNumber = 0 ):
    """ Use xdotool to press an F key """
    
    MINIMUM_FKEY_NUMBER = 1
    MAXIMUM_FKEY_NUMBER = 12
    
    if fKeyNumber in range(
            MINIMUM_FKEY_NUMBER, 
            MAXIMUM_FKEY_NUMBER, 
            ):
        return shell(
                KEY_COMMAND +
                'F' +
                str(fKeyNumber)
                )
    else:
        return False



def holdFKey( fKeyNumber = 0 ):
    """ Use xdotool to hold an F key. """
    pass
    return



def releaseFKey( fKeyNumber = 0 ):
    """ Use xdotool to release an F key. """
    pass
    return



def altFKey( fKeyNumber = 0 ):
    """ Use xdotool to combine the ALT key with an F key. """
    pass
    return



def ctrlFKey( fKeyNumber = 0 ):
    """ Use xdotool to combine the CTRL key with an F key. """
    pass
    return



def metaFKey( fKeyNumber = 0 ):
    """ Use xdotool to combine the Meta key with an F key """
    pass
    return



def superFKey( fKeyNumber = 0 ):
    pass
    return



def typeEnterKey( amount = 1 ):
    """ Use xdotool to press the Enter key a certain amount of times. """
    
    enterKeyPresses = []
    for loop in range(amount):
        enterKeyPresses.append(
                shell(
                    KEY_COMMAND +
                    'Return'
                    )
                )
    
    if False in enterKeyPresses:
        return False
    else:
        return True



def holdEnterKey():
    pass
    return



def releaseEnterKey():
    pass
    return

