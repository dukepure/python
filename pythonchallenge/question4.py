'''
Created on 2015-1-25

@author: duke
'''

import urllib

str_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
str_req = "12345"

for x in range(1, 400):
    str_text = urllib.urlopen(str_url + str_req).read()
    print str_text
    list_req = str_text.split()
    try:
        str_req = filter(lambda x: x.isdigit(), list_req)[0]
    except:
        if str_text.find("html") > 0: break
        str_req = str_text
