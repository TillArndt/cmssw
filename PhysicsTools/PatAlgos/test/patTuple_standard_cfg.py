## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *
## switch to uncheduled mode
process.options.allowUnscheduled = cms.untracked.bool(True)
#process.Tracer = cms.Service("Tracer")

process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
#   process.GlobalTag.globaltag =  ...    ##  (according to https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions)
#                                         ##
from PhysicsTools.PatAlgos.patInputFiles_cff import filesRelValProdTTbarAODSIM
process.source.fileNames = filesRelValProdTTbarAODSIM
#                                         ##
process.maxEvents.input = 100
#                                         ##
#   process.out.outputCommands = [ ... ]  ##  (e.g. taken from PhysicsTools/PatAlgos/python/patEventContent_cff.py)
#                                         ##
process.out.fileName = 'edmTuple_standard.root'
#                                         ##
#   process.options.wantSummary = False   ##  (to suppress the long output at the end of the job)

process.patMuons.userData.userFunctions = cms.vstring('((trackIso+caloIso)/pt)')
process.patMuons.userData.userFunctionLabels = cms.vstring('relIso')
#process.selectedPatMuons.cut = cms.string('pt > 20. & abs(eta) < 2.1 & userFloat("relIso") >= 0')
process.patMuonAnalyzer = cms.EDProducer( "CandViewNtpProducer", src = cms.InputTag("selectedPatMuons"), lazyParser = cms.untracked.bool(True), prefix = cms.untracked.string(""), eventInfo = cms.untracked.bool(True), variables = cms.VPSet( cms.PSet( tag = cms.untracked.string("pt"), quantity = cms.untracked.string("pt") ), cms.PSet( tag = cms.untracked.string("eta"), quantity = cms.untracked.string("eta") ), cms.PSet( tag = cms.untracked.string("phi"), quantity = cms.untracked.string("phi") ), ) )

process.out.outputCommands = ['drop *', 'keep *_patMuonAnalyzer_*_*']
