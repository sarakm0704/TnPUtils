#! /usr/bin/env python

import os
import re
import sys
import time
import commands

from os import listdir
from os.path import isfile, join

typename = "MC"
mypath = "/home/tjkim/work/sourceFiles/tnp/"+typename

filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for filename in filenames:
  inputfile = mypath + "/" + filename
  names = filename.split(".")
  outputfile = mypath +"/skim/" + names[0]+"_skim.root"
  remove_variables = "all"
  keep_variables=""

  if typename is "RD":
    keep_variables= "\"combRelIsoPF03dBeta combRelIsoPF04dBeta pair_nJets30 abseta eta pt mass pair_newTuneP_mass pair_newTuneP_probe_pt tag_combRelIsoPF04dBeta tag_nVertices tag_pt Medium2016 PF Tight2012 dB dzPV\""
  else:
    keep_variables= "\"combRelIsoPF03dBeta combRelIsoPF04dBeta pair_nJets30 abseta eta pt mass pair_newTuneP_mass pair_newTuneP_probe_pt tag_combRelIsoPF04dBeta tag_nVertices tag_pt Medium2016 PF Tight2012 dB dzPV truePU mcTrue mcMass pair_genWeight pair_truePileUp pair_actualPileUp\""

  cuts = "\"((pt > 20 || pair_newTuneP_probe_pt >20) && mass > 69.5 && mass < 130.1  && tag_combRelIsoPF04dBeta < 0.2 && tag_combRelIsoPF04dBeta> -0.5 &&tag_pt > 25 && tag_IsoMu24==1 && abseta <2.401 && pair_probeMultiplicity == 1)\""
  os.system('./skimTree '+inputfile+' '+outputfile+' -r '+remove_variables+' -k '+keep_variables+' -c '+cuts)

