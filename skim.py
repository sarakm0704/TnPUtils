#! /usr/bin/env python

import os
import re
import sys
import time
import commands

from os import listdir
from os.path import isfile, join

postfix = "nJet4more"
typename = "RD"
mypath = "/home/tjkim/work/sourceFiles/tnp/"+typename+"/ReReco/skim/"
#mypath = "/home/tjkim/work/sourceFiles/tnp/"+typename+"/skim/"
#mypath = "/home/tjkim/work/sourceFiles/tnp/"+typename

filenames = ""
if typename is "RD":
  #filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  filenames = ["TnPTree_17Nov2017_SingleMuon_Full_GoldenJSON_skim.root"]
else:
  filenames = ["tnpZ_withNVtxWeights.root"]

for filename in filenames:
  inputfile = mypath + "/" + filename
  names = filename.split(".")
  if os.path.isdir(mypath+postfix) is not True:
    os.system('mkdir '+mypath+postfix)
  outputfile = mypath +"/"+postfix +"/"+ names[0]+"_"+postfix+".root"
  remove_variables = "all"
  keep_variables=""

  if typename is "RD":
    keep_variables= "\"combRelIsoPF03dBeta combRelIsoPF04dBeta pair_nJets30 abseta eta pt mass pair_newTuneP_mass pair_newTuneP_probe_pt tag_combRelIsoPF04dBeta tag_nVertices tag_pt Medium2016 PF Tight2012 dB dzPV\""
  else:
    #use this one when you have "weight" variable
    keep_variables= "\"combRelIsoPF03dBeta combRelIsoPF04dBeta pair_nJets30 abseta eta pt mass pair_newTuneP_mass pair_newTuneP_probe_pt tag_combRelIsoPF04dBeta tag_nVertices tag_pt Medium2016 PF Tight2012 dB dzPV truePU mcTrue mcMass pair_genWeight pair_truePileUp pair_actualPileUp weight\""
    #keep_variables= "\"combRelIsoPF03dBeta combRelIsoPF04dBeta pair_nJets30 abseta eta pt mass pair_newTuneP_mass pair_newTuneP_probe_pt tag_combRelIsoPF04dBeta tag_nVertices tag_pt Medium2016 PF Tight2012 dB dzPV truePU mcTrue mcMass pair_genWeight pair_truePileUp pair_actualPileUp\""

  cuts = "\"((pt > 20 || pair_newTuneP_probe_pt >20) && mass > 69.5 && mass < 130.1  && tag_combRelIsoPF04dBeta < 0.2 && tag_combRelIsoPF04dBeta> -0.5 &&tag_pt > 25 && tag_IsoMu24==1 && abseta <2.401 && pair_probeMultiplicity == 1 && pair_nJets30 >= 4)\""
  os.system('./skimTree '+inputfile+' '+outputfile+' -r '+remove_variables+' -k '+keep_variables+' -c '+cuts)

