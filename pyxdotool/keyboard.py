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
KEY_DOWN_COMMAND = 'xdotool keydown '
KEY_UP_COMMAND = 'xdotool keyup '



def xdotoolKey( key = '' ):
    """Retun an xdotool key name from an ascii key"""
    
    xdotoolKeys = {}
    if len(key) == len(key[0]):
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

    if len(key) == len(key[0]):
        if key in xdotoolKeys:
            return xdotoolKeys[key]
        else:
            return key
    else:
        return ''



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

	typeUpKey( amount = 1 )
	holdUpKey()
	releaseUpKey()

	typeDownKey( amount = 1 )
	holdDownKey()
	releaseDownKey()

	typeLeftKey( amount = 1 )
	holdLeftKey()
	releaseLeftKey()

	typeRightKey( amount = 1 )
	holdRightKey()
	releaseRightKey()

'''


'''
    It may be a better idea to build these functions by iterating through
        a list of actons (type, hold, release), and the key (ctrl, alt, super...)
        because much of the code in the methods are very similar, except for 
        a few lines.

    F key functions should be built seperately
'''

## Build special key functions

# Special key constants
MINIMUM_FKEY_NUMBER = 1
MAXIMUM_FKEY_NUMBER = 12

# Special keys Function name to xdotool command
specialKeys = {
        'Alt':      'alt' ,
        'Ctrl':     'ctrl' ,
        'Enter':    'Return' ,
        'Super':    'super' ,
        'Meta':     'meta' ,
        }

arrowKeys = {
        'Right':    'Right' ,
        'Left':     'Left' ,
        'Up':       'Up' ,
        'Down':     'Down' ,
        }

# Key actions list
keyActions = [ 
        'type' ,
        'hold' ,
        'release' ,
        'combine' ,
        ]

# Combinations for F keys
fKeyCombine = [
        'alt' ,
        'ctrl' ,
        'meta' ,
        'super' ,
        ]


for function in specialKeys:
    '''
        Notes:
            xdotool keydown Return
                Doesn't seem to hold the enter key down

            xdotool key super+[key]
                Sometimes only types the key, instead of the super+key combo
    '''

    # Build and execute typeKey function
    buildFunction = ''
    buildFunction += 'def type' + function + 'Key( amount = 1 ):\n'
    buildFunction += '  """ Type the ' + function + ' key a certain amount of times. """\n'
    buildFunction += '  keyTyped = []\n'
    buildFunction += '  for press in range(amount):\n'
    buildFunction += '      keyTyped.append(\n'
    buildFunction += '          shell(\n'
    buildFunction += '              KEY_COMMAND + \n'
    buildFunction += '              "' + specialKeys[function] + '"\n'
    buildFunction += '              )\n'
    buildFunction += '          )\n'
    buildFunction += '  if False in keyTyped:\n'
    buildFunction += '      return False\n'
    buildFunction += '  else:\n'
    buildFunction += '      return True\n'
    exec(buildFunction)

    # Build and execute holdKey functions
    buildFunction = ''
    buildFunction += 'def hold' + function + 'Key():\n'
    buildFunction += '  """ Hold down the ' + function + ' Key. """\n'
    buildFunction += '  return shell(\n'
    buildFunction += '      KEY_DOWN_COMMAND + \n'
    buildFunction += '      "' + specialKeys[function] + '"\n'
    buildFunction += '      )\n'
    exec(buildFunction)

    # Build and execute releaseKey functions
    buildFunction = ''
    buildFunction += 'def release' + function + 'Key():\n'
    buildFunction += '  """ Release the ' + function + ' Key. """\n'
    buildFunction += '  return shell(\n'
    buildFunction += '      KEY_UP_COMMAND + \n'
    buildFunction += '      "' + specialKeys[function] + '"\n'
    buildFunction += '      )\n'
    exec(buildFunction)

    # Build and execute combineKey functions
    buildFunction = ''
    buildFunction += 'def combine' + function + 'Key( key = "" ):\n'
    buildFunction += '  """ Combine the ' + function + ' key with another key. """\n'
    buildFunction += '  return shell(\n'
    buildFunction += '      KEY_COMMAND + \n'
    buildFunction += '      "' + specialKeys[function] + '+" + \n'
    buildFunction += '      key\n'
    buildFunction += '      )\n'
    exec(buildFunction)





### ----- F Key Methods --------------------------------------

def typeFKey( fKeyNumber = 0 ):
    """ Use xdotool to press an F key """
    
    
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
    
    MINIMUM_FKEY_NUMBER = 1
    MAXIMUM_FKEY_NUMBER = 12
    
    if fKeyNumber in range(
            MINIMUM_FKEY_NUMBER, 
            MAXIMUM_FKEY_NUMBER, 
            ):
        return shell(
                KEY_DOWN_COMMAND +
                'F' +
                str(fKeyNumber)
                )
    else:
        return False
    pass
    return



def releaseFKey( fKeyNumber = 0 ):
    """ Use xdotool to release an F key. """
    
    MINIMUM_FKEY_NUMBER = 1
    MAXIMUM_FKEY_NUMBER = 12
    
    if fKeyNumber in range(
            MINIMUM_FKEY_NUMBER, 
            MAXIMUM_FKEY_NUMBER, 
            ):
        return shell(
                KEY_UP_COMMAND +
                'F' +
                str(fKeyNumber)
                )
    else:
        return False
    pass
    return



def altFKey( fKeyNumber = 0 ):
    """ Use xdotool to combine the ALT key with an F key. """
    
    MINIMUM_FKEY_NUMBER = 1
    MAXIMUM_FKEY_NUMBER = 12
    
    if fKeyNumber in range(
            MINIMUM_FKEY_NUMBER, 
            MAXIMUM_FKEY_NUMBER, 
            ):
        return shell(
                KEY_COMMAND +
                'alt+' +
                'F' +
                str(fKeyNumber)
                )
    else:
        return False
    pass
    return



def ctrlFKey( fKeyNumber = 0 ):
    """ Use xdotool to combine the CTRL key with an F key. """
    
    MINIMUM_FKEY_NUMBER = 1
    MAXIMUM_FKEY_NUMBER = 12
    
    if fKeyNumber in range(
            MINIMUM_FKEY_NUMBER, 
            MAXIMUM_FKEY_NUMBER, 
            ):
        return shell(
                KEY_COMMAND +
                'ctrl+' +
                'F' +
                str(fKeyNumber)
                )
    else:
        return False
    pass
    return



def metaFKey( fKeyNumber = 0 ):
    """ Use xdotool to combine the Meta key with an F key """
    
    MINIMUM_FKEY_NUMBER = 1
    MAXIMUM_FKEY_NUMBER = 12
    
    if fKeyNumber in range(
            MINIMUM_FKEY_NUMBER, 
            MAXIMUM_FKEY_NUMBER, 
            ):
        return shell(
                KEY_COMMAND +
                'meta+' +
                'F' +
                str(fKeyNumber)
                )
    else:
        return False
    pass
    return



def superFKey( fKeyNumber = 0 ):
    """ Use xdotool to combine the Super key with an F key. """
    
    MINIMUM_FKEY_NUMBER = 1
    MAXIMUM_FKEY_NUMBER = 12
    
    if fKeyNumber in range(
            MINIMUM_FKEY_NUMBER, 
            MAXIMUM_FKEY_NUMBER, 
            ):
        return shell(
                KEY_COMMAND +
                'super+' +
                'F' +
                str(fKeyNumber)
                )
    else:
        return False
    pass
    return



### ------------------------------------------------------------------


