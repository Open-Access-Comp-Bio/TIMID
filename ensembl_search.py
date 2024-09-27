import pandas as pd
from bulk_search_functions import chromosome_location_search, uniprot_search
entries = []

user_input = input("Please enter Ensembl IDs separated by a space \n") #delimiter subject to change 
entries = user_input.replace(","," ").replace("\t"," ").split()

#print("String List: ", entries)

chr_locations = []
gene_names = []
gene_ids = []
uniprot_ids = []
omim_ids = []
alpha_ids = []

for i in entries:
    try:
        gene_name, chr_location, gene_id = chromosome_location_search(i)
        chr_locations.append(chr_location)
        gene_names.append(gene_name)
        gene_ids.append(gene_id)

    except Exception as e: 
        gene_names.append("N/A")
        chr_locations.append("N/A")
        gene_ids.append("N/A")
        uniprot_ids.append("N/A")
for i in gene_names:
    uniprot_id = uniprot_search(i)
    uniprot_ids.append(uniprot_id)

flat_locations = []        
for i in chr_locations:
    for j in i:
        flat_locations.append(j)
        
print("Gene Names: ", gene_names)
print("Chromosome Locations: ",flat_locations)
print("NCBI IDs: ", gene_ids)
print("Uniprot IDs: ", uniprot_ids)

info_df = pd.DataFrame(
    {"Gene Name" : gene_names,
     "NCBI ID" : gene_ids,
    "Chromosome Location" : flat_locations,
    "Uniprot ID" : uniprot_ids
}
)

print(info_df)