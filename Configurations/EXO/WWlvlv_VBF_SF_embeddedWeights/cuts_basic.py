# cuts

#cuts = {}

                           


supercut = 'mll>70  \
            && std_vector_lepton_pt[0]>20 && std_vector_lepton_pt[1]>20 \
            && std_vector_lepton_pt[2]<10 \
            && metPfType1 > 20 \
            && ptll > 30 \
            '
#      __.....__                      __.....__                     
#   .-''         '.                .-''         '.                   
#  /     .-''"'-.  `.     .-.     /     .-''"'-.  `.                 
# /     /________\   \    | |    /     /________\   \ ,.----------.  
# |                  |,---| |---.|                  |//            \ 
# \    .-------------'`---| |---'\    .-------------'\\            / 
#  \    '-.____...---.    | |     \    '-.____...---. `'----------'  
#   `.             .'     `-'      `.             .'                 
#     `''-...... -'                  `''-...... -'                   
                                                                   


cuts['e_e']  = 'std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11 \
                '

# __  __   ___               __  __   ___                   
#|  |/  `.'   `.            |  |/  `.'   `.                 
#|   .-.  .-.   '    .-.    |   .-.  .-.   '                
#|  |  |  |  |  |    | |    |  |  |  |  |  | ,.----------.  
#|  |  |  |  |  |,---| |---.|  |  |  |  |  |//            \ 
#|  |  |  |  |  |`---| |---'|  |  |  |  |  |\\            / 
#|  |  |  |  |  |    | |    |  |  |  |  |  | `'----------'  
#|__|  |__|  |__|    `-'    |__|  |__|  |__|                
                                                           

cuts['mu_mu']  = 'std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13 \
                 ' 
