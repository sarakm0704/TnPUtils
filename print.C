void print(){

 TFile * f = new TFile("/home/luulan/Zbosons/TnPTree_SingleMuon_Run2017Bv1_294927_to_297723_GoldenJSON.root");

 TTree * t = (TTree*) f->Get("tpTree/fitter_tree");

 t->Print();

}
