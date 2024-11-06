#!/usr/bin/env python3

# Usage:
# ./src/bin/fillids.py ./src/xml/sim/site1.xml > out.xml

import re
import sys
import uuid

xmlfile = sys.argv[1]

with open(xmlfile, 'r') as f:
    for line in f:
        if ('id=""' in line):
            ele = re.search('<(.+) id=""', line).group(1).strip()
            uid = str(uuid.uuid4()).split('-')[0]
            val = 'id="%s-%s"' % (ele, uid)
            line = line.replace('id=""', val)
        print(line, end="")
