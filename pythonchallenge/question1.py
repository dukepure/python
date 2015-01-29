'''
@author: duke
'''

import string

source_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

frm_str = string.letters[0:26]
to_str = string.letters[2:28].lower()
table = string.maketrans(frm_str, to_str)
result = source_str.translate(table)
print result