from Ensembl_to_NCBI_AM_061324 import database_search
from Bio import Entrez

Entrez.email = "ouranm@gmail.com"
def test_search():
    test_case_1 = "ENSG0000012048"
    test_case_2 = "ENSG0000012048   " 
    test_case_3 = "   ENSG0000012048" #these two test cases are for formatting errors. 
    test_case_4 = "ENSG00000141510"
    test_case_5 = "ENSG00000133703"
    expected1 = "672" #for test_case 1-3
    expected2 =  "7157"
    expected3 = "3845"
    assert database_search(test_case_1) == expected1, "Test Case 1 Failed"
    assert database_search(test_case_2) == expected1, "Test Case 2 Failed"
    assert database_search(test_case_3) == expected1, "Test Case 3 Failed"
    assert database_search(test_case_4) == expected2, "Test Case 4 Failed"
    assert database_search(test_case_5) == expected3, "Test Case 5 Failed"
    
