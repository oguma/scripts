#!/usr/bin/env python
import sys
import uuid
from lxml import etree

mm_in = sys.argv[1]
mm_out = sys.argv[2]

xml = etree.parse(open(mm_in, 'r'), parser=etree.XMLParser())

for item in xml.xpath("//attribute[@NAME='uid' or @NAME='gid']"):
    value = item.xpath("@VALUE")[0]
    if (value == ''):
        uid = str(uuid.uuid4()).split('-')[0]
        item.attrib['VALUE'] = uid + '-'

f = open(mm_out, "a")
f.write(etree.tostring(xml).decode())
f.close()
