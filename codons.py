def create_codon_dict(file_path):
    
    codon_dict = {}
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            # skip empty lines or comments
            if not line or line.startswith("#"):
                continue
            
            parts = line.split()
            codon = parts[0]
            amino_acid = parts[1]
            
            codon_dict[codon] = amino_acid
    
    return codon_dict


