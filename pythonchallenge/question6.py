'''
Created on 2015-1-29

@author: duke
'''
import urllib,zipfile,re

#download zip file
url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
urllib.urlretrieve(url, "channel.zip")

# get filename, content and zip comments
with zipfile.ZipFile("channel.zip", 'r') as outfile:    
    all_content_dict = dict((f.filename, (outfile.open(f.filename).read(), f.comment)) for f in outfile.filelist)

comment_list = []
def get_next(file_num):
    file_name = "%s.txt" % file_num
    mresult = re.search('(\d+)', all_content_dict[file_name][0])
    next_num = mresult.group() if mresult else ""
    print next_num
    comment_list.append(all_content_dict[file_name][1])
    
    return next_num

next_num = "90052"
for x in range(len(all_content_dict) - 1):
    next_num = get_next(next_num)

print "".join(comment_list)