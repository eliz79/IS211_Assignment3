#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Text Processing"""

#Erica Liz

import urllib2


url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
get_file = urllib2.Request(url)
response = urllib2.urlopen(get_file)
html = response.read()
print html










#url to use - 'http://s3.amazonaws.com/cuny- is211-spring2015/weblog.csv'
    
