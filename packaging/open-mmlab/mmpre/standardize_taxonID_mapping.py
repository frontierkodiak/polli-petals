import json
import os

def convert_legacy_mapping(input_file):
    with open(input_file, 'r') as f:
        legacy_data = json.load(f)
    
    converted_data = {}
    n_classes = {}
    for key, value in legacy_data.items():
        new_key = key.lstrip('L')
        converted_data[new_key] = {str(k): int(v) for k, v in value.items()}
        n_classes[new_key] = len(value)

    output_dir = os.path.dirname(input_file)
    meta_dir = os.path.join(output_dir, 'meta')
    os.makedirs(meta_dir, exist_ok=True)
    
    output_file = os.path.join(meta_dir, 'taxonID_mapping.json')
    with open(output_file, 'w') as f:
        json.dump(converted_data, f, indent=2)

    n_classes_file = os.path.join(meta_dir, 'n_classes.txt')
    with open(n_classes_file, 'w') as f:
        for rank, count in sorted(n_classes.items(), key=lambda x: int(x[0])):
            f.write(f"{rank}: {count}\n")

    print(f"Converted {input_file} -> {output_file}")
    print(f"Wrote n_classes to {n_classes_file}")

input_files = [
    "/pond/modelZoo/petals/raw/E24.1.4.aves/cat_idx_to_taxonID_mapping.json",
    "/pond/modelZoo/petals/raw/E24.1.4.arthro/cat_idx_to_taxonID_mapping.json", 
    "/pond/modelZoo/petals/raw/E24.1.5.reptilia/cat_idx_to_taxonID_mapping.json",
    "/pond/modelZoo/petals/raw/E24.4.3.angio/cat_idx_to_taxonID_mapping.json"
]

for file in input_files:
    convert_legacy_mapping(file)
    
'''
Standardize legacy 'cat_idx_to_taxonID_mapping.json' files into new 'taxonID_mapping.json' schema.

Required transformations:
- Convert taxonID values to ints.
- Remove "L" prefix from top-level keys (e.g. "L10" -> "10".)
- Generate an n_classes.txt file from the number of top-level keys.

Input files:
- /pond/modelZoo/petals/raw/E24.1.4.aves/cat_idx_to_taxonID_mapping.json
- /pond/modelZoo/petals/raw/E24.1.4.arthro/cat_idx_to_taxonID_mapping.json
- /pond/modelZoo/petals/raw/E24.1.5.reptilia/cat_idx_to_taxonID_mapping.json
- /pond/modelZoo/petals/raw/E24.4.3.angio/cat_idx_to_taxonID_mapping.json

Output all files into a new 'meta' subdir in the same directory as the input files.
'''