import FWCore.ParameterSet.Config as cms

process = cms.Process("COC")

#unscheduled mode
process.options = cms.untracked.PSet(allowUnscheduled = cms.untracked.bool(True) )

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring("file:patTuple_standard.root")
)

## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

## load the configuration for the customized COC running
process.load("PhysicsTools.PatExamples.customizedSelection_cff")
process.load("PhysicsTools.PatExamples.customizedCOC_cff")

## define the name and content of the output file
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('cocTuple.root'),
                               outputCommands = cms.untracked.vstring(
                                   'keep *',
                                   'drop *_selectedPatJets_*_*',
                                   'keep *_*_caloTowers_*',
                                   'keep *_*_genJets_*'
                                   )
                                )

process.outpath = cms.EndPath(process.out)

