#! /usr/bin/env python
s = input("Enter an app name: ")

txt = """
cd /media/oguma/microSD/reqos/git/
mkdir APPNAME.git
cd APPNAME.git
git init --bare --shared

cd /var/apps/APPNAME
git init
git add .
git commit -m \"first commit\"
git remote add origin /media/oguma/microSD/reqos/git/APPNAME.git
git push -u origin master
"""

print(txt.replace("APPNAME", s))
