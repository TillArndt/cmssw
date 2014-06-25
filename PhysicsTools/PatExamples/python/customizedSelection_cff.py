import FWCore.ParameterSet.Config as cms


isolatedPatElectrons = cms.EDFilter("PATElectronSelector",
                                        src = cms.InputTag("selectedPatElectrons"),
                                        cut = cms.string("pt>10 & abs(eta)<2.5 & (trackIso+caloIso)/pt<0.05")
                                    )

isolatedPatMuons = cms.EDFilter("PATMuonSelector",
                                src = cms.InputTag("selectedPatMuons"),
                                cut = cms.string("pt>10 & abs(eta)<2.5 & (trackIso+caloIso)/pt<0.05")
                                )

customSelection = cms.Sequence(
    isolatedPatElectrons *isolatedPatMuons
    )
