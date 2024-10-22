#!/usr/bin/env python

# executing script for dssp predictor in command line.

# import stuff for making CLI
import os
import argparse

import PredictDSSP as dssp


def main():

    # Parse command line arguments.
    parser = argparse.ArgumentParser(description='Generate dssp scores for all sequences in a FASTA file.')

    parser.add_argument('data_file', help='Path to fasta file containing sequences to be predicted.')

    parser.add_argument('-o', '--output-file', help='Filename for where to save the csv dssp scores. Default = dssp_scores.csv ', default='dssp_scores.csv')

    parser.add_argument('--invalid-sequence-action', help="For parsing FASTA file, defines how to deal with non-standard amino acids. See https://protfasta.readthedocs.io/en/latest/read_fasta.html for details. Default='convert' ", default='convert')

    args = parser.parse_args()

    
    if not os.path.isfile(args.data_file):
        print('Error: Could not find passed fasta file [%s]'%(args.data_file))


    # run predict disorder fasta
    dssp.predict_dssp_fasta(filepath=args.data_file, 
                                output_file = args.output_file,
                                invalid_sequence_action=args.invalid_sequence_action)
