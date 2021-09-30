import os
from os import listdir
from os.path import isfile, join
mypath = "F:/Thulo Technology Pvt Ltd/Cards/face"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

count = 1

for i in onlyfiles:
    if i !="work.py":
        print(i)
        os.rename(i,str(count)+'.png')
        count+=1