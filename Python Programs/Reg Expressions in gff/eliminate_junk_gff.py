import re

regexes = [
    ('exon:', ''),
    ('mRNA:', ''),
    ('CDS:', ''),
    ('five_prime_UTR:', ''),
    ('three_prime_UTR:', ''),
    ('gene:', ''),
]

def sub_func_2(text):
    for regex, sub in regexes:
        text = re.sub(regex, sub, text)
    return text

inFile = open("ITAG3.2_gene_models.gff", "r")
outFile = open("ITAG3.2_gene_models_CLEAN.gff", "w")

for row in inFile.readlines():
    outFile.writelines(sub_func_2(row))
