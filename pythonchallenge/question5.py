'''
Created on 2015-1-29

@author: duke
'''
import pickle

f = open(r"banner.p")
banner_list = pickle.load(f)
def printer(banner_list):
    print ''.join(banner[0] * banner[1] for banner in banner_list)
map(printer, banner_list)