#Ensembl to NCBI Accession Codes for homo sapiens. 
#Goal: To take in a list of Ensembl IDs and obtain the gene name and NCBI accession codes and append these to a pandas dataframe.
#Example: ENSG00000012048 
import requests
import re
from Bio import Entrez
import urllib.parse
import json
import xml.etree.ElementTree as ET
import pandas as pd

Entrez.email = input("In compliance with NCBI policy, please input your email:") 
entries = []

#user_input = input("Please enter Ensembl IDs separated by a space \n") #delimiter subject to change 
#entries = user_input.split()

#print("String List: ", entries)
e_id_format = r"^ENSG\d{9}\.\d$"
e_id_format1 = r"^ENSG\d{11}$"

#For future scripts, will try to have this be a list or data frame column to loop through 

def chromosome_location_search(gene_id):
    
    if re.match(e_id_format, str(gene_id)) or re.match(e_id_format1, str(gene_id)):
        url = f"https://rest.ensembl.org/lookup/id/{gene_id}?content-type=application/json"
        summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi" 
        response = requests.get(url)
        
        if response.status_code==200:
            data = response.json()
            #print(f"Ensembl data: {data}") This is only for current troubleshooting and will be taken out later 
            
            display_name = data.get("display_name", "No display name found.")
            #print(f"Gene name is {display_name}")
            search_term = f"{display_name}[Gene] AND Homo sapiens[Organism]"
            
            handle = Entrez.esearch(db="gene", term=search_term)
            record = Entrez.read(handle)
            handle.close()
            
            if record["IdList"]:
                
                gene_id = record["IdList"][0]
                #print(f"NCBI Gene ID:{gene_id}")
                
                summary_handle = Entrez.esummary(db="gene", id=gene_id)
                summary_record = Entrez.read(summary_handle)
                summary_handle.close()
            
                gene_info = summary_record["DocumentSummarySet"]["DocumentSummary"][0]
                #print(f"NCBI Gene Info: {gene_info}")
                #Works up to this point - 061724
                accession_codes = [i['ChrAccVer'] for i in gene_info.get("GenomicInfo", []) if "ChrAccVer" in i]
                #print(f"NCBI Accession Codes: {accession_codes}")
            else:
                print(f"No accession code was found for {display_name} in NCBI")
            

        else:
            print(f"Failed to retrieve data: {response.status_code}")
        #print(accession_codes)
        
    else:
        print("Invalid ID")
    return display_name, accession_codes,gene_id 

#For now this is only able to handle human sequences, but hope to expand to other species later on. 

def uniprot_search(display_name): #searches only for human 092724
    uniprot_id = []
    url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{display_name}+AND+organism_id:9606&format=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        for i in data["results"]:
            uniprot_id.append(i['primaryAccession'])
    else:
        print("Failed to retrieve data from Uniprot API.")
    return uniprot_id

