# PredictDSSP: a PARROT BRNN for predicting DSSP scores

**PredictDSSP** is a Python package that allows prediction of DSSP scores using a PARROT generated BRRN classifier. For more on PARROT see https://github.com/idptools/parrot


PredictDSSP is usable from the command-line or as a Python API.


## Background

PredictDSSP was trained on per-residue DSSP scores. DSSP scores classify secondary structure where 

 0 is helicity

 1 is beta strand/sheet

 2 is coil

For the final network, a balanced dataset of per-residues-scores from 74,777 sequences was used. The dataset consists of 2 layers and a hidden size of 20. The network name is dssp_2022_01_07_CB_thresh_0p8_hs20_nl2.pt. Networks with fewer layers / smaller hidden size were less accurate, but additional layers and increases in hidden size did not improve accuracy above that of this network.

### How accurate is this predictor?

Evaluation of the dataset on 4,352 sequences that were not used for training found that it had an overall accuracy of 74.002% and an MCC of MCC = 0.60345. The breakdown of predictions for helicity (0), beta strand/sheet (1), and coil (2) is as follows:

 percent correct predicting 0 = 75.16%, 

 percent correct predicting 1 = 68.66%, 

 percent correct predicting 2 = 76.954%

We have found that the predictor performs relatively well overall but does not seem to perform well in disordered regions.


## Installation

To install PredictDSSP using PyPi, you can use pip from the command-line. 

	$ pip install PredictDSSP


To clone the GitHub repository and gain the ability to modify a local copy of the code, run

	$ git clone https://github.com/ryanemenecker/PredictDSSP.git
	$ cd PredictDSSP
	$ pip install .


You can now use PredictDSSP from Python or the command-line.


## Usage from Python

First import PredictDSSP:

	import PredictDSSP as dssp

### Predicting DSSP scores

Next, make DSSP score predictions:

	dssp.predict_dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA')

**Additional usage**

You can now get the raw values from the predictions. These are returned as a list of lists. The first element in each list is the helical probability, the second element in each list is the probability to form a beta strand/sheet, and the final element in each list is the probability to be coiled.

Example

	dssp.predict_dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA', raw_vals=True)


### Graphing DSSP scores

To graph DSSP scores:

	dssp.graph_dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA')

*optional arguments*

To get the raw values graphed (the actual probabilities for each secondary structure), set raw_vals=True. Ex:

	dssp.graph_dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA', raw_vals=True)

To set the title, set 'title' equal to your desired title. Ex:

	dssp.graph_dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA', title='mygraph')

To set exclude predictions for regions that are disordered, set exclude_disorder=True. Ex:

	dssp.graph_dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA', exclude_disorder=True)

To set exclude disorder bars from the grpah when excluding disorder, set no_disorder_bars=True. Ex:

	dssp.graph_dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA', exclude_disorder=True, no_disorder_bars=True)

To change the disorder threshhold, set 'dis_threshhold' to your desired threshhold. Disorder scores are calculated using metapredict, and a higher threshhold requires higher confidence to denote a region as disordered. Default is 0.3. Ex:

	dssp.graph_dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA', exclude_disorder=True, dis_threshhold=0.5)

To change DPI of teh generated figure, set 'DPI' to the desired DPI. Default is 150. Ex:

	dssp.graph_dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA', DPI=300)

To save the graph, set output file to the path followed by the output file name. Ex:

	dssp.graph_dssp('MQWESSASSSWQQQQGGGGSAFACACAAFAAAAAA', output_file='/my/file/path/graph_name.png')


### Predicting DSSP scores from fasta

To predict DSSP scores from a fasta file:

	dssp.predict_dssp_fasta('/path/to/my/fasta/file/my_file.fasta')

*optional arguments*

To make an output file instead of returning sequence immediately, set output_file to your filepath followed by the file name. Ex:

	dssp.predict_dssp_fasta('/path/to/my/fasta/file/my_file.fasta', output_file = '/where/to/save/file/my_dssp_predictions.csv')


### Graphing DSSP scores from fasta

To graph DSSP scores from sequences in a FASTA file:

	dssp.graph_dssp_fasta('/path/to/my/fasta/file/my_file.fasta')

By default it will return individual graphs. **If you have a large fasta file, you will want to save the graphs or you will have to close each graph individually as it is generated**.

*optional arguments*

To save the graphs to a specified directory, specifiy 'output_dir' = file path to your director. Ex:

	dssp.graph_dssp_fasta('/path/to/my/fasta/file/my_file.fasta', output_dir = '/where/to/save/files/')

To set exclude predictions for regions that are disordered, set exclude_disorder=True. Ex:

	dssp.graph_dssp_fasta('/path/to/my/fasta/file/my_file.fasta', exclude_disorder=True)

To set exclude disorder bars from the grpah when excluding disorder, set no_disorder_bars=True. Ex:

	dssp.graph_dssp_fasta('/path/to/my/fasta/file/my_file.fasta', exclude_disorder=True, no_disorder_bars=True)

To change the disorder threshhold, set 'dis_threshhold' to your desired threshhold. Disorder scores are calculated using metapredict, and a higher threshhold requires higher confidence to denote a region as disordered. Default is 0.3. Ex:

	dssp.graph_dssp_fasta('/path/to/my/fasta/file/my_file.fasta', exclude_disorder=True, dis_threshhold=0.5)

To change DPI of teh generated figure, set 'DPI' to the desired DPI. Default is 150. Ex:

	dssp.graph_dssp_fasta('/path/to/my/fasta/file/my_file.fasta', DPI=300)

To set the output file type, set 'output_filetype' to your desired filetype. Ex:

	dssp.graph_dssp_fasta('/path/to/my/fasta/file/my_file.fasta', output_filetype='pdf')


### Predicting DSSP scores from uniprot ID

You can get DSSP score predictions by just inputting a Uniprot ID. 

	dssp.predict_dssp_uniprot('UniprotID')

Ex:

	dssp.predict_dssp_uniprot('Q8RYC8')

*optional arguments*

To get raw probability values, simply set raw_vals=True. Ex.

	dssp.predict_dssp_uniprot('Q8RYC8', raw_vals=True)


### Graphing DSSP scores from uniprot ID

You can generate DSSP score graphs using a uniprot ID. 

	dssp.graph_dssp_uniprot('UniprotID')

Ex:

	dssp.graph_dssp_uniprot('Q8RYC8')

*optional arguments*

To graph raw probability values, simply set raw_vals=True. Ex.

	dssp.graph_dssp_uniprot('Q8RYC8', raw_vals=True)

To set the title, set 'title' equal to your desired title. Ex:

	dssp.graph_dssp_uniprot('Q8RYC8', title='mygraph')

To set exclude predictions for regions that are disordered, set exclude_disorder=True. Ex:

	dssp.graph_dssp_uniprot('Q8RYC8', exclude_disorder=True)

To set exclude disorder bars from the grpah when excluding disorder, set no_disorder_bars=True. Ex:

	dssp.graph_dssp_uniprot('Q8RYC8', exclude_disorder=True, no_disorder_bars=True)

To change the disorder threshhold, set 'dis_threshhold' to your desired threshhold. Disorder scores are calculated using metapredict, and a higher threshhold requires higher confidence to denote a region as disordered. Default is 0.3. Ex:

	dssp.graph_dssp_uniprot('Q8RYC8', exclude_disorder=True, dis_threshhold=0.5)

To change DPI of teh generated figure, set 'DPI' to the desired DPI. Default is 150. Ex:

	dssp.graph_dssp_uniprot('Q8RYC8', DPI=300)

To save the graph, set output file to the path followed by the output file name. Ex:

	dssp.graph_dssp_uniprot('Q8RYC8', output_file='/my/file/path/graph_name.png')



## Usage from the command-line

### Graphing DSSP scores from the command-line using a Uniprot ID

``dssp-uniprot`` generates a graph from a uniprot ID. 

**Example:**

	$ dssp-uniprot Q8RYC8

*optional arguments*

``-D`` or ``--dpi`` lets you set the DPI of the generated graph.

	$ dssp-uniprot Q8RYC8 -D


``-e`` or ``--exclude_disorder`` lets you exclude disordered regions from predictions.

	$ dssp-uniprot Q8RYC8 -e


``-o`` or ``--output-file`` lets you save the graph to a specific location.

	$ dssp-uniprot Q8RYC8 -o /my/path/to/file/my_graph.png


``-t`` or ``--title`` lets you set the title of the graph.

	$ dssp-uniprot Q8RYC8 -t MyCoolGraph

``-c`` or ``--cutoff`` lets you set cutoff value for something to be considered disordered.

	$ dssp-uniprot Q8RYC8 -c 0.5

``-r`` or ``--raw_vals`` lets you graph raw value probabilities

	$ dssp-uniprot Q8RYC8 -r


### Graphing DSSP scores from the command-line using a protein name

``dssp-name`` generates a graph from a protien and / or organism name

**Example:**

	$ dssp-name p53 human

*optional arguments*

``-D`` or ``--dpi`` lets you set the DPI of the generated graph.

	$ dssp-name p53 -D


``-e`` or ``--exclude_disorder`` lets you exclude disordered regions from predictions.

	$ dssp-name p53 -e


``-o`` or ``--output-file`` lets you save the graph to a specific location.

	$ dssp-name p53 -o /my/path/to/file/my_graph.png


``-t`` or ``--title`` lets you set the title of the graph.

	$ dssp-name p53 -t MyCoolGraph

``-c`` or ``--cutoff`` lets you set cutoff value for something to be considered disordered.

	$ dssp-name p53 -c 0.5

``-r`` or ``--raw_vals`` lets you graph raw value probabilities

	$ dssp-name p53 -r



### Generating DSSP scores from a FASTA file form the command-line

``dssp-fasta`` generates dssp scores from a specified FASTA file. By default will save the scores to your current directory as dssp_scores.csv

**Example:**

	$ dssp-fasta /path/to/my/file/sequences_file.fasta

*optional arguments*

``-o`` or ``--output-file`` lets you save the scores to a specific location.

	$ dssp-fasta /path/to/my/file/sequences_file.fasta -o /where/to/save/these/scores/dssp_scores.csv


## Changes

### 1.3.0 (October 2024)
* Finally started tracking versions
* Newest version is PEP517 compliant.

