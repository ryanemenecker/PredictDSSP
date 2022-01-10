import os 
from PredictDSSP import py_predictor_v2

def dssp(sequence, predictor=2):

    # get path to network
    PATH = os.path.dirname(os.path.realpath(__file__))
    
    # possible networks:
    possible_networks = ['dssp_2021_12_20_CB_mf_0p8.pt', 'dssp_2021_12_20_default_CB.pt', 'dssp_2021_12_20_no_CB.pt']
    
    # if predictor set to help, remind user what each predictor is.
    if predictor == 'help':
        # message telling user what each possible predictor value corresponds to
        help_message = f'0 = {possible_networks[0]}, 1 = {possible_networks[1]}, 2 = {possible_networks[2]}'
        # return help message
        return help_message
    
    # if user selects a network, proceed
    else:
        # get the chosen network
        used_predictor = possible_networks[predictor]
        # set location of chosen network
        predictor_path = f'{PATH}/networks/{used_predictor}'
        # set predictor value using py_predictor_V2
        my_predictor = py_predictor_v2.Predictor(predictor_path, 
                                                dtype="residues")    
        # get values of prediction
        value = my_predictor.predict(sequence)
        # make empty list to hold values
        final_vals = []
        # append values to the list depending on the probabilities for each value
        for i in value:
            highest_val = max(i)
            if highest_val == i[0]:
                final_vals.append(0)
            elif highest_val == i[1]:
                final_vals.append(1)
            else:
                final_vals.append(2)
        # return the final values based on the probabilities returned from the network
        return final_vals




