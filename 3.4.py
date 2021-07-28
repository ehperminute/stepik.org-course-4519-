Вася, открывший заправку в прошлом уроке, разорился. Конкуренция оказалась слишком большой. Вася предполагает, что это произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре. Определите, сколько заправок на самом деле (не только обозначенных точкой) есть на фрагменте карты https://stepik.org/media/attachments/lesson/245681/map2.osm


import xml.etree.ElementTree as E
from urllib.request import urlopen

xmlfile = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
tree = E.parse(xmlfile)
root = tree.getroot()
gasstations = root.findall('*/tag[@k="amenity"][@v="fuel"]')
print(len(gasstations)) 
