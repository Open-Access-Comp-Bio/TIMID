#!/usr/bin/env python3

# Gene symbol to MyGene ID function, MyGene ID to OMIM ID converter function, and Gene symbol to OMIM ID function

# Modules required:
import requests
import logging

# Function to retrieve MyGene ID from Gene common symbol:
def get_MyGene(gene):
    '''This function takes a gene symbol as an input, and returns the MyGene ID number for the gene.
    If there is not a match in the MyGene database, an error message is logged that the symbol is not valid.'''
    r = requests.get(f"https://mygene.info/v3/query?q={gene}&fields=all&size=10&from=0&fetch_all=false&facet_size=10&entrezonly=false&ensemblonly=false&dotfield=false")
    r = r.json()
    try: 
        MyGene_ID = r["hits"][0]["_id"]
        MyGene_ID = int(MyGene_ID)
        return MyGene_ID
    except:
        logging.error("Error: Invalid Gene Symbol or Name")
        return None


def convert_MyGene_to_OMIM(mygeneid):
    '''This function takes a MyGene ID number as an input, and prints the OMIM ID number as an output.
    If there is not a match in the MyGene database, an error message is logged that the ID is not valid.
    Note: This function cannot obtain the OMIM ID from the common gene symbol, only convert the MyGene ID number to it.'''
    r = requests.get(f"https://mygene.info/v3/gene/{mygeneid}?fields=all&dotfield=false&size=10")
    r = r.json()
    try: 
        OMIM_ID = r["MIM"]
        OMIM_ID = int(OMIM_ID)
        return OMIM_ID
    except:
        logging.error("Error: Invalid MyGene ID or Gene Not Found in OMIM Database")
        return None


def get_OMIM(gene):
    '''This function takes a gene symbol as an input, and returns the OMIM ID number for the gene.
    This function uses the previous two functions, so an appropriate error message is logged at any step that fails.'''
    try:
        mygeneid = get_MyGene(gene)
        omimid = convert_MyGene_to_OMIM(mygeneid)
        omimid = int(omimid)
        return omimid
    except: 
        logging.error("Error: Invalid Gene or Gene Not Found in OMIM Database")
        return None
