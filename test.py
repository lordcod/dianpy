from dianpy import tofile, fromfile
path = r"./test.xml"

if __name__ == '__main__':
    meet = fromfile(path)
    tofile(meet, "./output.xml", pretty=True)
