Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить количество заправок в интересующем его районе. Вася скачал интересующий его кусок карты OSM https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать, сколько на нём отмечено точечных объектов (node), являющихся заправкой. В качестве ответа вам необходимо вывести одно число - количество АЗС.

"Как обозначается заправка в OpenStreetMap" - пример хорошего запроса чтобы узнать, как обозначается заправка в OpenStreetMap.

import xml.etree.ElementTree as E
from urllib.request import urlopen

xmlfile = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
tree = E.parse(xmlfile)
root = tree.getroot()
gasstations = root.findall('node/tag[@k="amenity"][@v="fuel"]')
#parent nodes (если нужны родительские ноды):
#gasstations = root.findall('./node/tag[@k="amenity"][@v="fuel"]/..')
#for i in gasstations:
#    print(E.tostring(i, encoding='unicode'))
print(len(gasstations))
