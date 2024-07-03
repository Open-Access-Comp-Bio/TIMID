from dna_rna_manipulations import get_complementary_dna
from dna_rna_manipulations import transcribe_dna
from dna_rna_manipulations import rev_transcribe_rna
from Convert_MyGene_to_OMIM import get_OMIM
from Convert_MyGene_to_OMIM import convert_MyGene_to_OMIM
from Convert_MyGene_to_OMIM import get_MyGene

def test_get_complementary_dna():
    assert get_complementary_dna('ATG') == 'CAT'
    assert get_complementary_dna('ATG6') == None
    assert get_complementary_dna('gAtT') == 'AATC'

def test_transcribe_dna():
    assert transcribe_dna('ATG') == 'AUG'
    assert transcribe_dna('ATGU') == None
    assert transcribe_dna('ttt') == 'UUU'

def test_rev_transcribe_dna():
    assert rev_transcribe_rna('AUG') == 'ATG'
    assert rev_transcribe_rna('ATG') == None
    assert rev_transcribe_rna('uuug') == 'TTTG'

def test_get_OMIM():
    assert get_OMIM("MC1R") == 155555
    assert get_OMIM("Melanocortin 1 Receptor") == 155555
    assert get_OMIM('invalid gene name') == None
    assert get_OMIM('ALBUMIN') == 103600

def test_convert_MyGene_to_OMIM():
    assert convert_MyGene_to_OMIM(4157) == 155555
    assert convert_MyGene_to_OMIM(213) == 103600
    assert convert_MyGene_to_OMIM(155555) == None
    assert convert_MyGene_to_OMIM("MC1R") == None
    
def test_get_MyGene():
    assert get_MyGene("alb") == 213
    assert get_MyGene("MC1R") == 4157
    assert get_MyGene('invalid gene name') == None
    assert get_MyGene("albumin") == 213
