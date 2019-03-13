# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['mll']  = {   'name': 'mll',            #   variable name
                       'range' : (15, 0. ,600),    #   variable range
                       'xaxis' : 'mll [GeV]',  #   x axis name
                       'fold' : 3
                       }

variables['djv_ptl1']  = {   'name': '(std_vector_jet_pt[2]>20)*(std_vector_jet_pt[2]/std_vector_lepton_pt[0])',
                       'range' : (7, -0.25 ,1),    
                       'xaxis' : 'djv(p_{t}^{lep1})',  
                       'fold' : 3
                       } #usually jet_pt > 20 (if not verified, use 0 instead of jet_pt)

variables['djv_mll']  = {   'name': '(std_vector_jet_pt[2]>20)*(std_vector_jet_pt[2]/mll)',
                       'range' : (7, -0.25 ,1),    
                       'xaxis' : 'djv(m_{ll})',
                       'fold' : 3
                       } #usually jet_pt > 20 (if not verified, use 0 instead of jet_pt)

variables['djv_ptll']  = {   'name': '(std_vector_jet_pt[2]>20)*(std_vector_jet_pt[2]/ptll)',
                       'range' : (7, -0.25 ,1),    
                       'xaxis' : 'djv(p_{t}^{ll})',
                       'fold' : 3
                       } #usually jet_pt > 20 (if not verified, use 0 instead of jet_pt)

variables['mjj']  = {  'name': 'mjj',
                      'range': (8,500,2000),
                      'xaxis': 'm_{jj} [GeV]',
                      'fold': 3
                      }

variables['detajj']  = { 'name': 'detajj',
                         'range': (14,2,9),
			 'xaxis': '#Delta#eta_{jj}',
                         'fold': 3
                       }





