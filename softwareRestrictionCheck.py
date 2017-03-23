#!/usr/bin/env python

import os.path

process = "Bluetooth File Exchange.app"
blacklist = "/Library/Application Support/JAMF/.blacklist.xml"

present = os.path.isfile(blacklist)
if present == True:
    for line in open(blacklist):
        if process in line:
            print '<result>Restriction Present</result>'
        else:
            print '<result>Restriction Not Present</result>'
else:
    print '<result>No Restrictions Present</result>'

