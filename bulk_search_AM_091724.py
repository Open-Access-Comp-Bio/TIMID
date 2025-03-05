import pandas as pd
from Ensembl_to_NCBI_AM_061324 import database_search
entries = []

user_input = input("Please enter Ensembl IDs separated by a space \n") #delimiter subject to change 
entries = user_input.split()

print("String List: ", entries)

ncbi_ids = []
for i in range(len(entries)):
    ncbi_ids[i] = database_search(entries[i])
print("NCBI IDs: ",ncbi_ids)
