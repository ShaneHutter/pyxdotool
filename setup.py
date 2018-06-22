#!/usr/bin/env python
"""
    Setup script for installing pyxdotool
"""

from distutils.core import setup

setup(
        name                = 'pyxdotool'                           ,
        version             = '0.0.1-1'                             ,
        author              = 'Shane Hutter'                        ,
        author_email        = 'shane.hutter86@gmail.com'            ,
        description         = 'Python wrapper module for xdotool'   ,
        long_description    = open( 'README.md' ).read()            ,
        license             = open( 'LICENSE' ).read()              ,
        packages            = [ 'pyxdotool' , ]                     ,
        )
