import FWCore.ParameterSet.Config as cms

## This is an example of the use of the BasicAnalyzer concept used to exploit C++ classes to do anaysis
## in full framework or FWLite using the same class. You can find the implementation of this module in
## PhysicsTools/PatExamples/plugins/PatMuonEDAnlyzer.cc. You can find the EDAnalyzerWrapper.h class in
## PhysicsTools/UtilAlgos/interface/EDAnalyzerWrapper.h. You can find the implementation of the
## PatMuonAnalyzer class in PhysicsTools/PatExamples/interface/PatMuonAnlyzer.h. You will also find
## back the input parameters to the module.
MyPatJetEDAnalyzer = cms.EDAnalyzer("MyPatJetEDAnalyzer",
  jets = cms.InputTag("selectedPatJets"),
  electrons = cms.InputTag("selectedPatElectrons"),                                             
)


