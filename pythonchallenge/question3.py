'''
@author: duke
'''

import re
with open('level3data.txt', 'r') as afile:
    text = afile.read()
lst = re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', text)  
print lst
