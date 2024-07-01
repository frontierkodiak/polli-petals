# Polli Petals metadata schemas
All 'preview' models output the wrong format-- hClass models output cat_idx, and detectors output supercategories.
  Therefore we have created two types of taxonID_mapping.json files.
  Each hClass model has different taxonomic coverage, and so have their own taxonID_mapping.json files.
  Both detectors share the same taxonID_mapping.json file.
    We also have a version that includes rank_levels. The handler should probably load this one to return rank_level along with taxonID.
New TorchServe handlers will load the taxonID_mapping.json file to convert the model's output into standard `polli-v0` json output schema.
  TODO: Design this schema. Share as much as possible b/w hClass and detector models.

## taxonID_mapping.json (hClass Multitask Model)

The `taxonID_mapping.json` file provides a mapping from the model's output category indices (`cat_idx`) to standardized taxonomic identifiers (`taxonID`). This mapping is used to convert the model's raw output into meaningful taxonomic labels.

### Schema

```json
{
  "rank_level_1": {
    "cat_idx_1": taxonID_1,
    "cat_idx_2": taxonID_2,
    ...
  },
  "rank_level_2": {
    "cat_idx_1": taxonID_1,
    "cat_idx_2": taxonID_2,
    ...
  },
  ...
}
```

- The top-level keys represent the taxonomic rank level, such as "10", "20", "30", etc.
  - Rank level "10" represents species-level labels
  - Higher rank levels represent higher taxonomic ranks (genus, family, etc.)
- Each rank level object contains key-value pairs mapping `cat_idx` to `taxonID`
  - `cat_idx` (key): The category index output by the model, as a string
  - `taxonID` (value): The corresponding standardized taxonomic identifier, as an integer

### Usage

1. Obtain the model's output category indices (`cat_idx`) for a given input
2. Determine the desired taxonomic rank level (e.g., "10" for species-level)
3. Look up the `cat_idx` in the corresponding rank level object of the `taxonID_mapping.json` file
4. The value associated with the `cat_idx` key is the standardized `taxonID` for that taxonomic label

### Notes

- The `taxonID` values are unique integers, each representing a distinct taxonomic unit
- The `taxonID` values can be used to look up additional information about the taxon in other metadata files or databases
- The rank levels are hierarchical, with higher numbers representing more specific taxonomic ranks
- Not all `cat_idx` values may be present at all rank levels, depending on the specificity of the model's training data

## taxonID_mapping.json (supercategory Detector Model)

The detector model `taxonID_mapping.json` file provides a mapping from the model's output supercategories to standardized taxonomic identifiers (`taxonID`).

### Schema

```json
{
  "supercategory_1": taxonID_1,
  "supercategory_2": taxonID_2,
  ...
}
```

- The keys represent the supercategory labels output by the detector model
- The values are the corresponding `taxonID` for each supercategory
  - Some supercategories are mapped to -1, indicating that they should be discarded

### Usage

1. Obtain the detector model's output supercategory for a given input
2. Look up the supercategory in the `taxonID_mapping.json` file
3. If the corresponding `taxonID` is -1, discard the prediction
4. Otherwise, the `taxonID` can be used for further processing or lookup

### Notes

- The detector model maps the supercategories "Arachnida" and "Insecta" to the phylum "Arthropoda" (taxonID: 47120)
- Some supercategories, such as "Plantae", "Fungi", "Mollusca", etc., are mapped to -1, indicating that they should be discarded
- The -1 `taxonID` is a null/discard value and does not represent a valid taxonomic identifier

## taxonID_mapping.json (Detector Model with Rank Levels)

The detector model `taxonID_mapping.json` file with rank levels provides a mapping from the model's output supercategories to standardized taxonomic identifiers (`taxonID`) along with the corresponding taxonomic rank level.

### Schema

```json
{
  "supercategory_1": {
    "taxonID": taxonID_1,
    "rank_level": rank_level_1
  },
  "supercategory_2": {
    "taxonID": taxonID_2,
    "rank_level": rank_level_2
  },
  ...
}
```

- The keys represent the supercategory labels output by the detector model
- The values are objects containing:
  - `taxonID`: The corresponding `taxonID` for the supercategory
  - `rank_level`: The taxonomic rank level of the `taxonID`
    - Some supercategories have a `null` rank level, indicating that they should be discarded

### Usage

1. Obtain the detector model's output supercategory for a given input
2. Look up the supercategory in the `taxonID_mapping.json` file
3. If the corresponding `taxonID` is -1 or the `rank_level` is `null`, discard the prediction
4. Otherwise, the `taxonID` and `rank_level` can be used for further processing or lookup

### Notes

- The detector model maps the supercategories "Arachnida" and "Insecta" to the phylum "Arthropoda" (taxonID: 47120, rank_level: 60)
- Some supercategories, such as "Plantae", "Fungi", "Mollusca", etc., have a `taxonID` of -1 and a `null` rank level, indicating that they should be discarded
- The -1 `taxonID` is a null/discard value and does not represent a valid taxonomic identifier
- Actual mappings can be found in packaging/open-mmlab/mmdet/mappings.md