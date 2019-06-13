#1
"""
grep Dutch zen.txt

"""

#2

"""
echo Arizona 479, 501, 870. California 209, 213, 650. | grep [[:digit:]]
"""


#3

import re

match = re.findall(".oo", "The ghost that says boo haunts the loo")
print(match)
