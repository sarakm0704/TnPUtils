#! /usr/bin/env python

import os
import re
import sys
import time
import commands

from os import listdir
from os.path import isfile, join

mcname = "/home/tjkim/work/sourceFiles/tnp/MC/skim/TnPTree_DYLL_M50_Madgraph_skim.root" 

mypath = "/home/tjkim/work/sourceFiles/tnp/RD"
filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]

datanames = ""
for filename in filenames:
  inputfile = mypath + "/" + filename
  datanames = datanames+inputfile+" "

print datanames

os.system('root -l -b -q '+mcname+' '+datanames+'addNVtxWeight.cxx+') 

