import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatExamples.MyPatJets_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
process = cms.Process("Test")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
    "file:patTuple_standard.root"
   #"file:patTuple_addBTagging.root"
  )
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.MessageLogger = cms.Service("MessageLogger")

## This is an example of the use of the BasicAnalyzer concept used to exploit C++ classes to do anaysis
## in full framework or FWLite using the same class. You can find the implementation of this module in
## PhysicsTools/PatExamples/plugins/PatMuonEDAnlyzer.cc. You can find the EDAnalyzerWrapper.h class in
## PhysicsTools/UtilAlgos/interface/EDAnalyzerWrapper.h. You can find the implementation of the
## PatMuonAnalyzer class in PhysicsTools/PatExamples/interface/PatMuonAnlyzer.h. You will also find
## back the input parameters to the module.
#process.MyPatJetEDAnalyzer = cms.EDAnalyzer("MyPatJetEDAnalyzer",
#  jets = cms.InputTag("selectedPatJets"),
#  electrons = cms.InputTag("selectedPatElectrons"),                                             
#)
process.bJets = selectedPatJets.clone(
src = "selectedPatJets",
cut = "pt > 60"
)
process.TFileService = cms.Service("TFileService",
  fileName = cms.string('analyzeMyPatJets_2.root')
)
process.MyPatJetAnalyzer = MyPatJetEDAnalyzer.clone(
)


process.MyBJetAnalyzer = MyPatJetEDAnalyzer.clone(
jets = "bJets"
)
process.p = cms.Path(process.bJets*process.MyBJetAnalyzer*process.MyPatJetAnalyzer)

