import sys
import os
cwd = os.getcwd()

sys.path.append(cwd)
#print (sys.path)

#Test the module: generate_list

from generate_list import printIt

for x in range(0,1000):
    printIt()