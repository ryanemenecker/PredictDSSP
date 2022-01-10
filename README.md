# PredictDSSP: a PARROT BRNN for predicting DSSP scores

**PredictDSSP** is a quickly written Python package that allows prediction of DSSP scores using a PARROT generated BRRN classifier. 


## Background

PredictDSSP was trained on per-residue DSSP scores. DSSP scores classify secondary structure where 
 0 is helicity
 1 is beta strand/sheet
 2 is coil

## Installation

To clone the GitHub repository and gain the ability to modify a local copy of the code, run

	$ git clone https://github.com/idptools/PredictDSSP.git
	$ cd PredictDSSP
	$ pip install .

## Usage

Right now PredictDSSP is only usable from Python because I made it really quickly. 

First import PredictDSSP:

	from PredictDSSP import predict

Next, make DSSP score predictions:

	predict.dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA')

By default, the predictor uses the dssp_2021_12_20_no_CB.pt netowork. However, you can change the network from within the function. For more info on the networks available see 'About the networks' section below.

To use a different network, simply specify a number after the sequence when using predict.dssp(). For example...

	predict.dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA', 0)

will use the dssp_2021_12_20_CB_mf_0p8.pt network. 

The numbers corresponding to each network are as follows:
 0 = dssp_2021_12_20_CB_mf_0p8.pt, 
 1 = dssp_2021_12_20_default_CB.pt, 
 2 = dssp_2021_12_20_no_CB.pt

Additional networks will be added sequentially here as new networks are developed. 

**What if I forget the numbers that correspond to each network?**

If you ever do not have the documentation and you forget the networks, simply specify 'help' in the second argument of predict.dssp(). For example:

	predict.dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA', 'help')

would return

	0 = dssp_2021_12_20_CB_mf_0p8.pt, 1 = dssp_2021_12_20_default_CB.pt, 2 = dssp_2021_12_20_no_CB.pt


## About the networks

All networks were trained using idptools-parrot version 1.6.1
 The parameters used in PARROT were: dtype = classifier, number_classes = 3, LR 0.001, 1 layer, 10 hidden size, batch size of 64, 100 epochs

PARROT returned results on the accuracy for each network. Becaues the networks had more/less data and were more/less balanced, their capacity to make accurate predictions from their own testing set *might not correspond to their overall accuracy*. There is more on the specific balance/data amount below. Once I have a better grasp on overall accuracy by testing the networks on a balanced dataset, I will update this documenation with that information. In the mean time the results were as follows (output from PARROT):

dssp_2021_12_20_CB_mf_0p8.pt -- most balanced, least data total -- 
Matthews Correlation Coef : 0.512
F1 Score : 0.679
Accuracy : 0.679


dssp_2021_12_20_default_CB.pt -- second most balanced, second most amount of data --
Matthews Correlation Coef : 0.556
F1 Score : 0.721
Accuracy : 0.723

dssp_2021_12_20_no_CB.pt -- Least balance, ost data. No filtering.
Matthews Correlation Coef : 0.596
F1 Score : 0.758
Accuracy : 0.761

As noted after each network, 
 dssp_2021_12_20_no_CB.pt had no filtering and had the least balanced data. However, it had the most amount of data. 
 dssp_2021_12_20_default_CB.pt was filtered less stringently than dssp_2021_12_20_CB_mf_0p8.pt but did have some filtering applied. It had the second most amount of data and was the 'second most balanced'.
 dssp_2021_12_20_CB_mf_0p8.pt had the most stringent filtering and therefore the most balanced data. However, it had the least overall amount of data.



