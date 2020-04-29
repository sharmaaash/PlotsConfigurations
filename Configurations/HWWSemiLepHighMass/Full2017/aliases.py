import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017
configurations = os.path.dirname(configurations) # HM
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]


eleWP    = 'mvaFall17V1Iso_WP90'
muWP     = 'cut_Tight_HWWW'
LepWPCut='(Lepton_isTightElectron_'+eleWP+'[0] > 0.5 \
            || Lepton_isTightMuon_'+muWP+'[0] > 0.5)'

Lep1WPCut='(Alt$(Lepton_isTightElectron_'+eleWP+'[1], 0) > 0.5 \
            || Alt$(Lepton_isTightMuon_'+muWP+'[1], 0) > 0.5)'

aliases['bWP'] = {
    'expr': '0.1522'
}
aliases['LepWPCut'] = {
    'expr': LepWPCut
}
aliases['Lep1WPCut'] = {
    'expr': Lep1WPCut
}

aliases['LepWPSF'] = {
    'expr': '(Lepton_isTightElectron_'+eleWP+'[0] > 0.5) * Lepton_tightElectron_'+eleWP+'_IdIsoSF[0] \
    + (Lepton_isTightMuon_'+muWP+'[0] > 0.5)*Lepton_tightMuon_'+muWP+'_IdIsoSF[0]',
    'samples': mc
}

aliases['WlepMT'] = {
    'expr': 'TMath::Sqrt( 2*Lepton_pt[0]*PuppiMET_pt \
    *( 1-TMath::Cos(Lepton_phi[0]-PuppiMET_phi) ) )'
}
aliases['boostHiggsMT'] = {
    'expr': 'TMath::Sqrt( 2*HM_Wlep_pt_Puppi*Alt$(HM_CleanFatJetPassMBoosted_pt[0], 0) \
    *( 1-TMath::Cos(HM_Wlep_phi_Puppi-Alt$(HM_CleanFatJetPassMBoosted_phi[0], 0)) ) )'
}
aliases['resolvHiggsMT'] = {
    'expr': 'TMath::Sqrt( 2*HM_Wlep_pt_Puppi*HM_Whad_pt \
    *( 1-TMath::Cos(HM_Wlep_phi_Puppi-HM_Whad_phi) ) )'
}

aliases['boosted'] = {
    'expr': 'PuppiMET_pt > 40 \
            && Alt$(HM_CleanFatJetPassMBoosted_pt[0], 0) > 200 \
            && Alt$(HM_CleanFatJetPassMBoosted_WptOvHfatM[0], 0) > 0.4 \
            && Alt$(HM_CleanFatJetPassMBoosted_tau21[0], 999) < 0.45 \
            && Alt$(HM_CleanFatJetPassMBoosted_mass[0], 0) > 40 \
            && abs(Alt$(HM_CleanFatJetPassMBoosted_eta[0], 999)) < 2.4'
}

aliases['idxCleanFatJetW'] = {
    'linesToAdd': ['.L %s/HWWSemiLepHighMass/Full2017/indexWFatJet.cc' % configurations],
    'class': 'FindBoostWIndex'
}

aliases['manualHfatM'] = {
    'linesToAdd': ['.L %s/HWWSemiLepHighMass/Full2017/boostHiggsMass.cc' % configurations],
    'class': 'CalcBoostHiggsMass',
}
aliases['boostedNoTau21'] = {
    'expr': 'PuppiMET_pt > 40 \
            && (int)idxCleanFatJetW != 999 \
            && Alt$(CleanFatJet_pt[(int)idxCleanFatJetW], 0) > 200 \
            && Alt$(CleanFatJet_eta[(int)idxCleanFatJetW], 999) < 2.4 \
            && Alt$(CleanFatJet_mass[(int)idxCleanFatJetW], 0) > 40 \
            && manualHfatM > 0 \
            && Alt$(CleanFatJet_pt[(int)idxCleanFatJetW], 0) / manualHfatM > 0.4 \
            && HM_Wlep_pt_Puppi / manualHfatM > 0.4'
}

aliases['resolved'] = {
    'expr': '!boosted[0] \
            && PuppiMET_pt > 30 \
            && WlepMT > 50 \
            && HM_WptOvHak4M > 0.35 \
            && resolvHiggsMT > 60 \
            && HM_Whad_pt > 30'
}

aliases['boostedSignalWMass'] = {
    'expr': '(65 < Alt$(HM_CleanFatJetPassMBoosted_mass[0], 0) \
            && Alt$(HM_CleanFatJetPassMBoosted_mass[0], 999) < 105)'
}
aliases['boostedSignalWMassNoTau21'] = {
    'expr': '(65 < Alt$(CleanFatJet_mass[(int)idxCleanFatJetW], 0) \
            && Alt$(CleanFatJet_mass[(int)idxCleanFatJetW], 999) < 105)'
}

aliases['resolvedSignalWMass'] = {
    'expr': '(65 < HM_Whad_mass && HM_Whad_mass < 105)'
}

aliases['boostedSidebandWMass'] = {
    'expr': '(40 < Alt$(HM_CleanFatJetPassMBoosted_mass[0], 0) \
            && Alt$(HM_CleanFatJetPassMBoosted_mass[0], 999) < 250)'
}
aliases['boostedSidebandWMassNoTau21'] = {
    'expr': '(40 < Alt$(CleanFatJet_mass[(int)idxCleanFatJetW], 0) \
            && Alt$(CleanFatJet_mass[(int)idxCleanFatJetW], 999) < 250)'
}

aliases['lowBoostedSidebandWMass'] = {
    'expr': '(40 < Alt$(HM_CleanFatJetPassMBoosted_mass[0], 0) \
            && Alt$(HM_CleanFatJetPassMBoosted_mass[0], 999) < 65)'
}

aliases['highBoostedSidebandWMass'] = {
    'expr': '(105 < Alt$(HM_CleanFatJetPassMBoosted_mass[0], 0) \
            && Alt$(HM_CleanFatJetPassMBoosted_mass[0], 999) < 250)'
}


aliases['resolvedSidebandWMass'] = {
    'expr': '(40 < HM_Whad_mass && HM_Whad_mass < 250)'
}

aliases['lowResolvedSidebandWMass'] = {
    'expr': '(40 < HM_Whad_mass && HM_Whad_mass < 65)'
}

aliases['highResolvedSidebandWMass'] = {
    'expr': '(105 < HM_Whad_mass && HM_Whad_mass < 250)'
}

aliases['resolvedQCDcr'] = {
    'expr': '(   65 < HM_Whad_mass && HM_Whad_mass < 105 \
                && WlepMT < 50 && 0 < resolvHiggsMT \
                && resolvHiggsMT < 60 && HM_WptOvHak4M < 0.35 )'
}

aliases['boostedQCDcr'] = {
    'expr': '(65 < Alt$(HM_CleanFatJetPassMBoosted_mass[0], 0) \
            && Alt$(HM_CleanFatJetPassMBoosted_mass[0], 999) < 105 \
            && WlepMT < 50 \
            && Alt$(HM_CleanFatJetPassMBoosted_tau21[0], 0) > 0.4\
            && Alt$(HM_CleanFatJetPassMBoosted_WptOvHfatM[0], 9) < 0.4)'
}

aliases['tau21DDT'] = {
    'expr': 'Alt$(CleanFatJet_tau21[(int)idxCleanFatJetW], -999) + 0.080 * TMath::Log( Alt$(CleanFatJet_mass[(int)idxCleanFatJetW]*CleanFatJet_mass[(int)idxCleanFatJetW], 0) / Alt$(CleanFatJet_pt[(int)idxCleanFatJetW], 1) )'
}






aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}


# aliases['oldmjjGen'] = {
#     'linesToAdd': [
#         'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
#         '.L %s/src/PlotsConfigurations/Configurations/HighMass/oldmjjGen/deltaRMatch.C+' % os.getenv('CMSSW_BASE'),
#         '.L %s/src/PlotsConfigurations/Configurations/HighMass/oldmjjGen/mjjGen.C+' % os.getenv('CMSSW_BASE')
#     ],
#     'expr': 'mjjGen(  Alt$(GenJet_pt[abs(Jet_genJetIdx[CleanJet_jetIdx[0]])],-1), \
#                       Alt$(GenJet_eta[abs(Jet_genJetIdx[CleanJet_jetIdx[0]])],-1), \
#                       Alt$(GenJet_phi[abs(Jet_genJetIdx[CleanJet_jetIdx[0]])],-1), \
#                       Alt$(GenJet_pt[abs(Jet_genJetIdx[CleanJet_jetIdx[1]])],-1), \
#                       Alt$(GenJet_eta[abs(Jet_genJetIdx[CleanJet_jetIdx[1]])],-1), \
#                       Alt$(GenJet_phi[abs(Jet_genJetIdx[CleanJet_jetIdx[1]])],-1), \
#                       Jet_genJetIdx[CleanJet_jetIdx[0]], \
#                       Jet_genJetIdx[CleanJet_jetIdx[1]])',
#     'samples': ['qqWWqq', 'WW2J'] + [skey for skey in samples if 'QQHSBI' in skey]
# }

aliases['GenLHE'] = {
'expr': '(Sum$(LHEPart_pdgId == 21) == 0)',
'samples': ['qqWWqq', 'WW2J']
}


# # B-Stuff
aliases['bVetoBoosted'] = {
    'expr': 'Sum$(Jet_btagDeepB[CleanJet_jetIdx[CleanJetNotFat_jetIdx]] > bWP[0] \
                    && CleanJet_pt[CleanJetNotFat_jetIdx] > 20 \
                    && abs(CleanJet_eta[CleanJetNotFat_jetIdx]) < 2.5 \
                ) == 0'
}
aliases['bVetoResolved'] = {
    'expr': 'Sum$(Jet_btagDeepB[CleanJet_jetIdx] > bWP[0] \
                    && CleanJet_pt > 20 \
                    && abs(CleanJet_eta) < 2.5 \
                    && CleanJet_jetIdx != HM_idx_j1 \
                    && CleanJet_jetIdx != HM_idx_j2 \
                ) == 0'
}
aliases['bVeto'] = {
    'expr': '((boosted[0] && bVetoBoosted) || (!boosted[0] && bVetoResolved))'
    # 'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'
}

aliases['bReq'] = {
    'expr': '!bVeto[0]'
    # 'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1'
}

# Temporary patch for BTV postprocessor bug (no SF for eta < 0, <= 102X_nAODv5_Full2018v5)
btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_102XSF_V1.csv' % os.getenv('CMSSW_BASE')

aliases['Jet_btagSF_shapeFix'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/src/PlotsConfigurations/Configurations/patches/btagsfpatch.cc+' % os.getenv('CMSSW_BASE')
    ],
    'class': 'BtagSF',
    'args': (btagSFSource,),
    'samples': mc
}

aliases['bVetoSF'] = {
    #'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagnSF'] = {
    #'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx] + (CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx] + (CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': 'bVetoSF[0]*bVeto[0] + btagnSF[0]*!bVeto[0]',
    'samples': mc
}

for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
    aliases['Jet_btagSF_shapeFix_up_%s' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'up_' + shift),
        'samples': mc
    }
    aliases['Jet_btagSF_shapeFix_down_%s' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'down_' + shift),
        'samples': mc
    }

    for targ in ['bVeto', 'btagn']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        #alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)
        alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        #alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)
        alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': '(bVetoSF{shift}up*bVeto + btagnSF{shift}up*!bVeto[0])'.format(shift = shift),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': '(bVetoSF{shift}down*bVeto + btagnSF{shift}down*!bVeto)'.format(shift = shift),
        'samples': mc
    }








# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['puWeight', 'TriggerEffWeight_1l', 'Lepton_RecoSF[0]', 'EMTFbug_veto','PrefireWeight','LepWPSF[0]','btagSF[0]']),
    'samples': mc
}
# # variations of tight lepton WP
aliases['SFweightEleUp'] = {
    'expr': 'Lepton_tightElectron_'+eleWP+'_IdIsoSF_Up[0]',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'Lepton_tightElectron_'+eleWP+'_IdIsoSF_Down[0]',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'Lepton_tightMuon_'+muWP+'_IdIsoSF_Up[0]',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'Lepton_tightMuon_'+muWP+'_IdIsoSF_Down[0]',
    'samples': mc
}







# FIXME top stuff
# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}

aliases['topGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}

aliases['antitopGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}

aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPtOTF) * TMath::Exp(0.0615 - 0.0005 * antitopGenPtOTF))) + isSingleTop',
    'samples': ['top']
}
# # Dennis Roy for 2017/2018 -> also update nuisances
# aliases['Top_pTrw'] = {
#     'expr': '(TMath::Sqrt(TMath::Exp(4.14819e-02 - 3.67734e-04*topGenPt + 7.60587e-08*topGenPt*topGenPt + 1.29362/(topGenPt+22.8537)) * TMath::Exp(4.14819e-02 - 3.67734e-04*antitopGenPt + 7.60587e-08*antitopGenPt*antitopGenPt + 1.29362/(antitopGenPt+22.8537))))',
#     'samples': ['top']
# }



# PU jet Id SF

puidSFSource = '%s/src/LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root' % os.getenv('CMSSW_BASE')

aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L %s/src/PlotsConfigurations/Configurations/patches/pujetidsf_event.cc+' % os.getenv('CMSSW_BASE')
    ],
    'class': 'PUJetIdEventSF',
    'args': (puidSFSource, '2017', 'loose'),
    'samples': mc
}
