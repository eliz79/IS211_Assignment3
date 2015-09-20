#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Text Processing"""

#__author__ = 'Erica Liz'

import urllib2


def downloadData(url):
    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
    get_file = urllib2.Request(url)
    response = urllib2.urlopen(get_file)
    html = response.read()
    print html


                
if __name__ == "__main__":
    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
    
