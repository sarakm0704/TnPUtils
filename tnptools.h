RooHist* getHist(TFile *f, const TString &dir, const TString &plot, int color, int style){
  cout << "getHist" << endl;
  cout << dir.Data() << endl;
  f->cd(dir.Data());
  TCanvas* c = (TCanvas*) gDirectory->FindKey(plot)->ReadObj();
  TString objname="";
  if(dir.Contains("cnt")) objname = "hxy_cnt_eff";
  else objname = "hxy_fit_eff";

  //TObject *obj; 
  //TIter next(c->GetListOfPrimitives());
  //while ((obj=next())) {
  //  cout << "Reading: " << obj->GetName() << endl;
  //  if (obj->InheritsFrom("TH1")) {
  //    cout << "histo: " << obj->GetName() << endl;
  //  }
  //}  

  RooHist* h = (RooHist*) c->FindObject(objname);

  h->SetLineWidth(2);
  h->SetLineColor(color);
  h->SetLineStyle(style);
  h->SetMarkerColor(color);
  h->SetMarkerStyle(color+19);
  h->SetMarkerSize(0.7);
  h->GetYaxis()->SetTitleSize(0.0);

  return h;
}
