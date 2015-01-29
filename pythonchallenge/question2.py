'''

@author: duke
'''


with open('level2data.txt', 'r') as file:
    text = file.read()
print ''.join([x for x in text if x.isalpha()]) 
