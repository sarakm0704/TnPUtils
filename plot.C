#include "tnptools.h"

void plot(){

  TFile * f_Iso_MC = new TFile("Efficiencytest/MC_mc_2017/TnP_MC_NUM_LooseRelIso_DEN_TightIDandIPCut_PAR_pt.root");
  TFile * f_Iso_RD = new TFile("Efficiencytest/DATA_data_2017/TnP_MC_NUM_LooseRelIso_DEN_TightIDandIPCut_PAR_pt.root");

  TString dir_pt = "tpTree/LooseIso4_NUM_LooseRelIso_DEN_TightIDandIPCut_PAR_pt/fit_eff_plots";
  TString plot_pt = "pt_PLOT_Tight2012_pass";
 
  RooHist* h1 = getHist(f_Iso_MC, dir_pt, plot_pt, 2, 2);
  RooHist* h2 = getHist(f_Iso_RD, dir_pt, plot_pt, 4, 1);

  TCanvas * c = new TCanvas("c","c",1);
  h1->Draw("");
  h2->Draw("same");

  TLegend *leg = new TLegend(.68,.25 ,.88,.40 );
  leg->AddEntry(h2, "Data", "LP");
  leg->AddEntry(h1, "MC", "LP");
  leg->SetFillColor(0);
  leg->SetTextSize(0.04);
  leg->SetLineColor(0);
  leg->Draw();
 
}
