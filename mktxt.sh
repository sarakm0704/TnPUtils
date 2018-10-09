./makeEffPlot EfficiencynJet0/tight_config/configEffPlot_pt.json > log_nJet0_pt
./makeEffPlot EfficiencynJet1/tight_config/configEffPlot_pt.json > log_nJet1_pt
./makeEffPlot EfficiencynJet2/tight_config/configEffPlot_pt.json > log_nJet2_pt
./makeEffPlot EfficiencynJet3/tight_config/configEffPlot_pt.json > log_nJet3_pt
./makeEffPlot EfficiencynJet3/tight_config/configEffPlot_pt.json > log_nJet3_pt
./makeEffPlot EfficiencynJet4/tight_config/configEffPlot_pt.json > log_nJet4_pt
./makeEffPlot EfficiencynJet4more/tight_config/configEffPlot_pt.json > log_nJet4more_pt
./makeEffPlot EfficiencynJet5more/tight_config/configEffPlot_pt.json > log_nJet5more_pt

./makeEffPlot EfficiencynJet0/tight_config/configEffPlot_eta.json > log_nJet0_eta
./makeEffPlot EfficiencynJet1/tight_config/configEffPlot_eta.json > log_nJet1_eta
./makeEffPlot EfficiencynJet2/tight_config/configEffPlot_eta.json > log_nJet2_eta
./makeEffPlot EfficiencynJet3/tight_config/configEffPlot_eta.json > log_nJet3_eta
./makeEffPlot EfficiencynJet4/tight_config/configEffPlot_eta.json > log_nJet4_eta
./makeEffPlot EfficiencynJet4more/tight_config/configEffPlot_eta.json > log_nJet4more_eta
./makeEffPlot EfficiencynJet5more/tight_config/configEffPlot_eta.json > log_nJet5more_eta

mv log_nJet0_* EfficiencynJet0/plot
mv log_nJet1_* EfficiencynJet1/plot
mv log_nJet2_* EfficiencynJet2/plot
mv log_nJet3_* EfficiencynJet3/plot
mv log_nJet4_* EfficiencynJet4/plot
mv log_nJet4more_* EfficiencynJet4more/plot
mv log_nJet5more_* EfficiencynJet5more/plot

cp -r EfficiencynJet0/plot ~/public/forTnP/Oct6/tightiso/nJet0
cp -r EfficiencynJet1/plot ~/public/forTnP/Oct6/tightiso/nJet1
cp -r EfficiencynJet2/plot ~/public/forTnP/Oct6/tightiso/nJet2
cp -r EfficiencynJet3/plot ~/public/forTnP/Oct6/tightiso/nJet3
cp -r EfficiencynJet4/plot ~/public/forTnP/Oct6/tightiso/nJet4
cp -r EfficiencynJet4more/plot ~/public/forTnP/Oct6/tightiso/nJet4more
cp -r EfficiencynJet5more/plot ~/public/forTnP/Oct6/tightiso/nJet5more
