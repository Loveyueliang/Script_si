import os
import xmltodict


def open_xml(xml):
    with open(xml, 'r') as f:
        _xml = xmltodict.parse(f.read())
    return _xml


xml_list = [_ for _ in os.listdir('.') if _.endswith('.xml')]
nums = 0
for xml in xml_list:
    _xml = open_xml(xml)
    image_status = _xml['annotation']['image_status']
    if image_status == '6':
        nums += 1
        print(_xml)

print('跳过图片数量：{}'.format(nums))
