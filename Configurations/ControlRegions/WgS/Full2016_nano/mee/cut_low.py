






supercut = ' (Lepton_eta[0])<2.4 &&  (Lepton_eta[1])<2.1 &&  (Lepton_eta[2])<2.1 && mllTwoThree > 0   \
              '

cuts['preselection'] = '1'

cuts['ZToeeWTom']  = ' Lepton_pt[0] > 15 && Lepton_pt[1] > 6 && Lepton_pt[2] > 6 && PuppiMET_pt > 10\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommpmet']  = ' Lepton_pt[0] > 15 && Lepton_pt[1] > 6 && Lepton_pt[2] > 6 && mpmet > 10\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommtw']  = ' Lepton_pt[0] > 15 && Lepton_pt[1] > 6 && Lepton_pt[2] > 6 && mtw1 > 10\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommet']  = ' Lepton_pt[0] > 15 && Lepton_pt[1] > 6 && Lepton_pt[2] > 6 && MET_pt > 10\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1 '


'''
cuts['ZToeeWTom']  = ' Lepton_pt[0] > 30 && Lepton_pt[1] > 10 && Lepton_pt[2] > 10 && PuppiMET_pt > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommpmet']  = ' Lepton_pt[0] > 30 && Lepton_pt[1] > 10 && Lepton_pt[2] > 10 && mpmet > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommtw']  = ' Lepton_pt[0] > 30 && Lepton_pt[1] > 10 && Lepton_pt[2] > 10 && mtw1 > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommet']  = ' Lepton_pt[0] > 30 && Lepton_pt[1] > 10 && Lepton_pt[2] > 10 && MET_pt > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1 '

##
cuts['ZToeeWTom1']  = ' Lepton_pt[0] > 40 && Lepton_pt[1] > 20 && Lepton_pt[2] > 20 && PuppiMET_pt > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommpmet1']  = ' Lepton_pt[0] > 40 && Lepton_pt[1] > 20 && Lepton_pt[2] > 20 && mpmet > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommtw1']  = ' Lepton_pt[0] > 40 && Lepton_pt[1] > 20 && Lepton_pt[2] > 20 && mtw1 > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommet1']  = ' Lepton_pt[0] > 40 && Lepton_pt[1] > 20 && Lepton_pt[2] > 20 && MET_pt > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1 '

##
cuts['ZToeeWTom2']  = ' Lepton_pt[0] > 40 && Lepton_pt[1] > 10 && Lepton_pt[2] > 10 && PuppiMET_pt > 20\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommpmet2']  = ' Lepton_pt[0] > 40 && Lepton_pt[1] > 10 && Lepton_pt[2] > 10 && mpmet > 20\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommtw2']  = ' Lepton_pt[0] > 40 && Lepton_pt[1] > 10 && Lepton_pt[2] > 10 && mtw1 > 20\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommet2']  = ' Lepton_pt[0] > 40 && Lepton_pt[1] > 10 && Lepton_pt[2] > 10 && MET_pt > 20\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1 '


###

cuts['ZToeeWTom3']  = ' Lepton_pt[0] > 25 && Lepton_pt[1] > 8 && Lepton_pt[2] > 8 && PuppiMET_pt > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommpmet3']  = ' Lepton_pt[0] > 25 && Lepton_pt[1] > 8 && Lepton_pt[2] > 8 && mpmet > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommtw3']  = ' Lepton_pt[0] > 25 && Lepton_pt[1] > 8 && Lepton_pt[2] > 8 && mtw1 > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommet3']  = ' Lepton_pt[0] > 25 && Lepton_pt[1] > 8 && Lepton_pt[2] > 8 && MET_pt > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1 '



cuts['ZToeeWTom4']  = ' Lepton_pt[0] > 25 && Lepton_pt[1] > 8 && Lepton_pt[2] > 8 && PuppiMET_pt > 20\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommpmet4']  = ' Lepton_pt[0] > 25 && Lepton_pt[1] > 8 && Lepton_pt[2] > 8 && mpmet > 20\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommtw4']  = ' Lepton_pt[0] > 25 && Lepton_pt[1] > 8 && Lepton_pt[2] > 8 && mtw1 > 20\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1'

cuts['ZToeeWTommet4']  = ' Lepton_pt[0] > 25 && Lepton_pt[1] > 8 && Lepton_pt[2] > 8 && MET_pt > 20\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightMuon_cut_Tight80x[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1 '

'''



