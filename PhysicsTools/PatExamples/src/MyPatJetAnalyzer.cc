#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "PhysicsTools/PatExamples/interface/MyPatJetAnalyzer.h"
#include "DataFormats/Math/interface/deltaR.h"

/// default constructor
MyPatJetAnalyzer::MyPatJetAnalyzer(const edm::ParameterSet& cfg, TFileDirectory& fs):
  edm::BasicAnalyzer::BasicAnalyzer(cfg, fs),
  jets_(cfg.getParameter<edm::InputTag>("jets")),
  electrons_(cfg.getParameter<edm::InputTag>("electrons"))
{
  //hists_["leadingJetPt"  ] = fs.make<TH1F>("leadingJetPt"  , "pt"  ,  100,  0., 300.);
  //hists_["JetEleDR" ] = fs.make<TH1F>("JetEleDR" , "#Delta R" ,  100, 0.,   5.);
  hists_["NJets"] = fs.make<TH1F>("NJets","Number of Jets",25,-0.5,24.5);
  hists_["JetPt"  ] = fs.make<TH1F>("JetPt"  , "pt"  ,  100,  0., 300.);
  hists_["JetEta" ] = fs.make<TH1F>("JetEta" , "#eta" ,  50, -3.,   3.);
}
MyPatJetAnalyzer::MyPatJetAnalyzer(const edm::ParameterSet& cfg, TFileDirectory& fs, edm::ConsumesCollector&& iC):
  edm::BasicAnalyzer::BasicAnalyzer(cfg, fs),
  jets_(cfg.getParameter<edm::InputTag>("jets"))  ,
  jetsToken_(iC.consumes<std::vector<pat::Jet> >(jets_)),
  electrons_(cfg.getParameter<edm::InputTag>("electrons"))  ,
  electronsToken_(iC.consumes<std::vector<pat::Electron> >(electrons_))

{
  //hists_["leadingJetPt"  ] = fs.make<TH1F>("leadingJetPt"  , "pt"  ,  100,  0., 300.);
  //hists_["JetEleDR" ] = fs.make<TH1F>("JetEleDR" , "#Delta R" ,  100, 0.,   5.);
  hists_["NJets"] = fs.make<TH1F>("NJets","Number of Jets",25,-0.5,24.5);
  hists_["JetPt"  ] = fs.make<TH1F>("JetPt"  , "pt"  ,  100,  0., 300.);
  hists_["JetEta" ] = fs.make<TH1F>("JetEta" , "#eta" ,  50, -3.,   3.);
}

/// everything that needs to be done during the event loop
void
MyPatJetAnalyzer::analyze(const edm::EventBase& event)
{
  // define what muon you are using; this is necessary as FWLite is not
  // capable of reading edm::Views
  using pat::Jet;
  using pat::Electron;

  // Handle to the muon collection
  edm::Handle<std::vector<Jet> > jets;
  event.getByLabel(jets_, jets);
    edm::Handle<std::vector<Electron> > electrons;
  event.getByLabel(electrons_, electrons);

  hists_["NJets"] -> Fill(jets->size());
for(std::vector<Jet>::const_iterator jet1=jets->begin(); jet1!=jets->end(); ++jet1){
    hists_["JetEta"  ]->Fill(jet1->eta());
}

  // loop muon collection and fill histograms
 /* for(std::vector<Jet>::const_iterator jet1=jets->begin(); jet1!=jets->end(); ++jet1){
        if (jet1 == jets->begin()){
	hists_["leadingJetPt"  ]->Fill(jet1->pt());
	if (electrons->size() > 0){
	hists_["JetEleDR"] ->Fill(deltaR(jet1->p4(),electrons->begin()->p4()));
  	}
}
}*/
  }

