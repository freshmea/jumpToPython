import xml.etree.ElementTree as ET


xml_str = '''<?xml version='1.0' encoding='utf-8'?>
<Countries>
    <Country name="Korea">
        <City attr1="value1" attr2="value2">Seoul</City>
    </Country>
    <Country name="Japanese">
        <City attr1="value1" attr2="value2">Tokyo</City>
    </Country>
</Countries>
'''

root = ET.fromstring(xml_str)

for country in root.findall("Country"):
    attr = country.attrib
    name = attr.get("name")
    city = country.find("City")
    city_name = city.text
    city_attr1 = city.attrib.get("attr1")
    city_attr2 = city.attrib.get("attr2")
    print(f"attr : {attr}")
    print(f"name : {name}")
    print(f"attr : {attr}")
    print(f"city_name : {city_name}")
    print(f"city_attr1 : {city_attr1}")
    print(f"city_attr2 : {city_attr2}")