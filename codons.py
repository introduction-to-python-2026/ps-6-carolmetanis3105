def create_codon_dict(file_path):
    
    # Step 1: open the file
    file = open(file_path)
    
    # Step 2: read all rows
    rows = file.readlines()
    
    # Step 3: close the file
    file.close()
    
    # Step 4: create empty dictionary
    codon_dict = {}
    
    # Step 5: process each row
    for row in rows:
        row = row.strip()          # remove \n
        parts = row.split('\t')    # split by tab
        
        # Expected format: ["AAA", "Lys", "K", "Lysine"]
        codon = parts[0]           # first column
        amino_acid = parts[2]      # third column (the abbreviation, e.g., "K")
        
        codon_dict[codon] = amino_acid
    
    return codon_dict   



