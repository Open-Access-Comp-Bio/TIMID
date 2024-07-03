#!/usr/bin/env python3

import logging


def get_complementary_dna(sequence):
    '''Function to return the complementary sequence of a given DNA sequence.
    The function logs an error if there are invalid DNA characters present in
    the string passed through the function.'''
    sequence = sequence.upper()
    reverse_sequence = sequence[::-1]
    reverse_sequence_list = list(reverse_sequence)
    for n in range(len(reverse_sequence_list)):
        if reverse_sequence_list[n] == "A":
            reverse_sequence_list[n] = "T"
        elif reverse_sequence_list[n] == "T":
            reverse_sequence_list[n] = "A"
        elif reverse_sequence_list[n] == "C":
            reverse_sequence_list[n] = "G"
        elif reverse_sequence_list[n] == "G":
            reverse_sequence_list[n] = "C"
    complementary_sequence = "".join(reverse_sequence_list)
    invalidbasecount = 0
    for n in range(len(reverse_sequence_list)):
        if complementary_sequence[n] not in ["A","G","T","C"]:
            invalidbasecount = invalidbasecount + 1
        else:
            pass
    if invalidbasecount > 0:
        logging.error("Error: Invalid DNA Sequence")
        return None
    else:
        return complementary_sequence



def transcribe_dna(sequence):
    '''Function to return the transcribed RNA sequence of a given DNA sequence.
    The function logs an error if there are invalid DNA characters present in
    the string passed through the function. The function assumes that the DNA 
    passed through is the sense strand and returns the RNA transcribed from the
    antisense strand, and so the RNA has the same directionality.'''
    sequence = sequence.upper()
    sequence_list = list(sequence)
    for n in range(len(sequence_list)):
        if sequence_list[n] == "T":
            sequence_list[n] = "U"
    rna_sequence = "".join(sequence_list)
    invalidbasecount = 0
    for n in range(len(sequence_list)):
        if sequence[n] not in ["A","G","T","C"]:
            invalidbasecount = invalidbasecount + 1
        else:
            pass
    if invalidbasecount > 0:
        logging.error("Error: Invalid DNA Sequence")
        return None
    else:
        return rna_sequence



def rev_transcribe_rna(sequence):
    '''Function to return the reverse-transcribed DNA sequence of a given RNA sequence.
    The function logs an error if there are invalid RNA characters present in
    the string passed through the function.'''
    sequence = sequence.upper()
    sequence_list = list(sequence)
    for n in range(len(sequence_list)):
        if sequence_list[n] == "U":
            sequence_list[n] = "T"
    dna_sequence = "".join(sequence_list)
    invalidbasecount = 0
    for n in range(len(sequence_list)):
        if sequence[n] not in ["A","G","U","C"]:
            invalidbasecount = invalidbasecount + 1
        else:
            pass
    if invalidbasecount > 0:
        logging.error("Error: Invalid RNA Sequence")
        return None
    else:
        return dna_sequence
    


