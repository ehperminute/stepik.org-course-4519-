В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте. Ноды могут не только обозначать какой-то точечный объект, но и входить в состав way (некоторой линии, возможно замкнутой) и не иметь собственных тегов. Для доступного по ссылке https://stepik.org/media/attachments/lesson/245678/map1.osm фрагмента карты посчитайте, сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют. В качестве ответа введите два числа, разделённых пробелом.
  
import xml.etree.ElementTree as E
from urllib.request import urlopen

xmlfile = urlopen('https://stepik.org/media/attachments/lesson/245678/map1.osm')
tree = E.parse(xmlfile)
root = tree.getroot()
nodes = root.findall('node')
nodestag = root.findall('.node/[tag]')
print(len(nodestag), len(nodes) - len(nodestag))
