#Ensembl to NCBI Accession Codes for homo sapiens. 
#This is just my first attempt at this kind of project and am only aiming to print out the ID's for NCBI. 
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

user_input = input("Please enter Ensembl IDs separated by a space \n") #delimiter subject to change 
entries = user_input.split()

print("String List: ", entries)

ncbi_ids = []

#For future scripts, will try to have this be a list or data frame column to loop through 
# but let's just focus on getting this to work with one for now. - 061324

def database_search(gene_id):
    
    url = f"https://rest.ensembl.org/lookup/id/{gene_id}?content-type=application/json"
    summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi" 
    response = requests.get(url)
    
    if response.status_code==200:
        data = response.json()
        #print(f"Ensembl data: {data}") This is only for current troubleshooting and will be taken out later 
        
        display_name = data.get("display_name", "No display name found.")
        print(f"Gene name is {display_name}")
        search_term = f"{display_name}[Gene] AND Homo sapiens[Organism]"
        
        handle = Entrez.esearch(db="gene", term=search_term)
        record = Entrez.read(handle)
        handle.close()
        
        if record["IdList"]:
            
            gene_id = record["IdList"][0]
            print(f"NCBI Gene ID:{gene_id}")
            
            summary_handle = Entrez.esummary(db="gene", id=gene_id)
            summary_record = Entrez.read(summary_handle)
            summary_handle.close()
        
            gene_info = summary_record["DocumentSummarySet"]["DocumentSummary"][0]
            #print(f"NCBI Gene Info: {gene_info}")
            #Works up to this point - 061724
            accession_codes = [i['ChrAccVer'] for i in gene_info.get("GenomicInfo", []) if "ChrAccVer" in i]
            print(f"NCBI Accession Codes: {accession_codes}")
        else:
            print(f"No accession code was found for {display_name} in NCBI")

    else:
        print(f"Failed to retrieve data: {response.status_code}")
    print(accession_codes)
    return accession_codes

#Check if ID is good. "ENSG" for humans otherwise, 
# there is a three letter code for the species then a 11 number code with a period followed by the version. 
#For now, this script will only look at human sequences. 
e_id_format = r"^ENSG\d{10}\.\d$"
e_id_format2 = r"^ENSG\d{11}$"

for i in range(len(entries)):
    if re.match(e_id_format, entries[i]) or re.match(e_id_format2, entries[i]):
        print("Valid ID has been entered")
        #continue on inputting e_id into the first function. 
        ncbi_ids.append(database_search(entries[i]))

    else:
        print("Invalid ID")
    
print("NCBI IDs: ", ncbi_ids)
#Still need to add error handling and figure out what format we want the output to be now that I am able to produce a result. - 061724
    