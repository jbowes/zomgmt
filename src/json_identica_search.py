#!/usr/bin/python

# Copyright (c) 2010 Corey Welton <cswiii@gmail.com>

"""
json_identica_search.py 

This is a quick and dirty python script that parses JSON query
results from identi.ca.  A sample query has been included 
below, but is quite obviously modular and extensible
enough to be used with any string you throw at it.

This script could conceivably be used as a widget on some front
page to see what the hottest news is on (dent_query), according
to those keen folks at identi.ca 
"""

__author__ = "Corey Welton"
__copyright__ = "Copyright 2010, Corey Welton"
__credits__ = ["Corey Welton"]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Corey Welton"
__email__ = "cswiii@gmail.com"
__status__ = "Prototype"

import simplejson, urllib

dent_query = "enterprisey"

def parse_query(q):
  url= "http://identi.ca/api/search.json?q=" + q
  returned_query = simplejson.load(urllib.urlopen(url))
  dent_results=[]
  if "results" in returned_query:
    dent_results = returned_query['results'] 
    for dent in dent_results:
      dent_who = dent['from_user']
      dent_img = dent['profile_image_url']       
      dent_text = dent['text']  
      dent_date = dent['created_at']
      print '<img src="' + dent_img + '" alt="identi.ca icon"> <strong>' + dent_who + '</strong> <br />\n' + dent_text + '<br />\n' + '<small>' + dent_date + '</small> <br />\n'
  else: 
    print "Error returning identi.ca query"

print "Content-Type: text/html\n\n"
parse_query(dent_query)

 
