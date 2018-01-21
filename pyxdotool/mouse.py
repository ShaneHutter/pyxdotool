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


MOUSE_CLICK_COMMAND = 'xdotool click '
MOUSE_MOVE_COMMAND = 'xdotool mousemove --sync '



def moveMouse( 
        x = 0 , 
        y = 0 ,
        ):
    """ Move mouse to x, y coordinates. """
    
    try:
        return shell(
                MOUSE_MOVE_COMMAND + 
                str(x) +
                ' ' +
                str(y)
                )
    except:
        return False



def clickMouse( button = 0 ):
    """ Click a mouse key with xdotool. """
    
    MINIMUM_MOUSE_BUTTON = 1
    MAXIMUM_MOUSE_BUTTON = 5

    '''
        buttons:
                1 = left
                2 = middle
                3 = right
                4 = wheel up
                5 = wheel down
    '''
    
    if not(button):
        return False
    elif button in range(
            MINIMUM_MOUSE_BUTTON, 
            MAXIMUM_MOUSE_BUTTON
            ):
        return shell(
                MOUSE_CLICK_COMMAND + 
                str(button)
                )
    else:
        return False
