#!/usr/bin/bash
python2 setup.py bdist && sudo python2 setup.py install
python setup.py bdist && sudo python setup.py install
