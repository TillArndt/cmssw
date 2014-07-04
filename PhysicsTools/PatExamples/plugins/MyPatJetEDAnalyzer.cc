#include "FWCore/Framework/interface/MakerMacros.h"

/*
  This is an example of using the PatMuonAnalyzer class to do a simple analysis of muons 
  using the full framework and cmsRun. You can find the example to use this code in 
  PhysicsTools/PatExamples/test/....
*/
#include "PhysicsTools/UtilAlgos/interface/EDAnalyzerWrapper.h"
#include "PhysicsTools/PatExamples/interface/MyPatJetAnalyzer.h"

typedef edm::AnalyzerWrapper<MyPatJetAnalyzer> MyPatJetEDAnalyzer;
DEFINE_FWK_MODULE(MyPatJetEDAnalyzer);


