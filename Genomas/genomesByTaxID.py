#def to download all complete genomes from NCBI of a given taxon id
def download_genomes(taxon_id, email):
    import os
    from Bio import Entrez
    Entrez.email = email
    handle = Entrez.esearch(db="nucleotide", term=taxon_id, retmax=1)
    record = Entrez.read(handle)
    handle.close()
    handle = Entrez.efetch(db="nucleotide", id=record["IdList"], rettype="gb", retmode="text")
    records = Entrez.read(handle)
    handle.close()
    for record in records:
        if "complete genome" in record["GBSeq_feature-table"]:
            print("Downloading genome: " + record["GBSeq_locus"])
            #Download fasta file
            handle = Entrez.efetch(db="nucleotide", id=record["GBSeq_primary-accession"], rettype="fasta", retmode="text")
            out_file = open(record["GBSeq_locus"] + ".fasta", "w")
            out_file.write(handle.read())
            out_file.close()
            handle.close()
            
