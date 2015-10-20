#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module for text processing using Regular Expressions"""

#__author__ = 'Erica Liz'


import urllib2
import re
import argparse

def main():
    '''Main function.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='Enter the URL to get the CSV file.')
    args = parser.parse_args()

    if args.url:
        try:
            content = downloadData(args.url)
            imageSearch(content)
        except:
            print 'The URL entered is invalid.'
    else:
        print 'Please enter a URL.'


def downloadData(url):
    """Function to fetch data file."""
    response = urllib2.urlopen(url) #opens file
    html = response.read() #reads file data
    return html #returns file data 
    

def imageSearch(url):
    """Function to retrieve image percentage in file."""
    
    total = 0
    images = 0

    for row in url:
        total += 1
        img_ext = ('([.jpg$]|[.png$]|[.jpeg$]|[.gif$]|[.JPG$]|[.PNG$]|[.JPEG$]|[.GIF$])')
        #characters to search in file
        if re.search(img_ext, row) is not None:
            images += 1

    image_pct = (float(images) / total) * 100 #formula to calculate image % in file
    pct = 'Image requests account for {0:0.1f}% of all requests'.format(image_pct)
    return pct


def browserSearch(url):
    """Function to retrieve most popular browser being used by users."""
    total = 0
    sites = 0

    for line in url:
        browsers = ('([Chrome]|[Firefox]|[Safari]|[MSIE])')
        if re.search(browsers, line) is not None:
            sites +=1
    hits = (total + sites)
    total_hits = 'The most popular browser is {0:0.1f}% of all requests'.format(hits)
    return total_hits

    
                
if __name__ == "__main__":
    #url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
    
    main()
    
