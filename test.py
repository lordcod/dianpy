import os
from dianpy import tofile, fromfile
path = r"./test.xml"
path2 = r"./test2.xml"
output = r"./output.xml"

if __name__ == '__main__':
    meet = fromfile(path2)
    tofile(meet, "./output.xml", pretty=True)
    os.remove(output)
