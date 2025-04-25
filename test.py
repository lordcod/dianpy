from typing import Literal
import lxml.etree as ET
from dianpy import Meet, tofile, fromfile
import lenexpy

path = r"C:\Users\2008d\OneDrive\Документы\Соревнования\20.04.25 Кубок Главы Власиха\Кубок_ГЛАВЫ_г_о_В_ХА_ФИНАЛ,_20_04_2025.Swimming"
path_lenex = r"C:\Users\2008d\OneDrive\Документы\Соревнования\20.04.25 Кубок Главы Власиха\lenex.lxf"

if __name__ == '__main__':
    lenex = lenexpy.fromfile()
    dian = fromfile(path)

    tofile(meet, 'test.xml')
