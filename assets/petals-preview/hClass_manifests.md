### Aves

```yaml
version: petals-v0

model:
  name: petal.hClass.USA.aves.preview.xs.v0.0
  family: petal.hClass.preview
  type: hierarchical_classifier
  framework:
    family: mmdeploy
    variant: mmpretrain
    version: 1.0.3
  architecture:
    family: mobileone
    variant: s2

taxonomy:
  root_taxon_id: 3
  root_rank_level: 50
  output_rank_levels: [10, 20, 30, 40]

input:
  dims:
    min: [1, 3, 224, 224]
    opt: [1, 3, 224, 224]
    max: [1, 3, 224, 224]
  meta_available: false

output:
  schema: polli_v0
  format: json

providers:
  engine:
    docker_image: frontierkodiak/mmpre:1.0.3
  endpoint:
    docker_image: frontierkodiak/mmpre-serve-1.x:latest

metadata:
  region: USA
  clade: aves
```

### Arthropoda

```yaml
version: petals-v0

model:
  name: petal.hClass.USA.arthro.preview.xs.v0.0
  family: petal.hClass.preview
  type: hierarchical_classifier
  framework:
    family: mmdeploy
    variant: mmpretrain
    version: 1.0.3
  architecture:
    family: mobileone
    variant: s2

taxonomy:
  root_taxon_id: 47120
  root_rank_level: 60
  output_rank_levels: [10, 20, 30, 40, 50]

input:
  dims:
    min: [1, 3, 224, 224]
    opt: [1, 3, 224, 224]
    max: [1, 3, 224, 224]
  meta_available: false

output:
  schema: polli_v0
  format: json

providers:
  engine:
    docker_image: frontierkodiak/mmpre:1.0.3
  endpoint:
    docker_image: frontierkodiak/mmpre-serve-1.x:latest

metadata:
  region: USA
  clade: arthropoda
```

### Reptilia

```yaml
version: petals-v0

model:
  name: petal.hClass.USA.reptilia.preview.xs.v0.0
  family: petal.hClass.preview
  type: hierarchical_classifier
  framework:
    family: mmdeploy
    variant: mmpretrain
    version: 1.0.3
  architecture:
    family: mobileone
    variant: s2

taxonomy:
  root_taxon_id: 26036
  root_rank_level: 50
  output_rank_levels: [10, 20, 30, 40]

input:
  dims:
    min: [1, 3, 224, 224]
    opt: [1, 3, 224, 224]
    max: [1, 3, 224, 224]
  meta_available: false

output:
  schema: polli_v0
  format: json

providers:
  engine:
    docker_image: frontierkodiak/mmpre:1.0.3
  endpoint:
    docker_image: frontierkodiak/mmpre-serve-1.x:latest

metadata:
  region: USA
  clade: reptilia
```

### Angiospermae

```yaml
version: petals-v0

model:
  name: petal.hClass.USA.angio.preview.sm.v0.0
  family: petal.hClass.preview
  type: hierarchical_classifier
  framework:
    family: mmdeploy
    variant: mmpretrain
    version: 1.0.3
  architecture:
    family: mobileone
    variant: s3

taxonomy:
  root_taxon_id: 47125
  root_rank_level: 57
  output_rank_levels: [10, 20, 30, 40, 50]

input:
  dims:
    min: [1, 3, 224, 224]
    opt: [1, 3, 224, 224]
    max: [1, 3, 224, 224]
  meta_available: false

output:
  schema: polli_v0
  format: json

providers:
  engine:
    docker_image: frontierkodiak/mmpre:1.0.3
  endpoint:
    docker_image: frontierkodiak/mmpre-serve-1.x:latest

metadata:
  region: USA
  clade: angiospermae
```

### Mammalia

```yaml
version: petals-v0

model:
  name: petal.hClass.USA.mammalia.preview.xs.v0.0
  family: petal.hClass.preview
  type: hierarchical_classifier
  framework:
    family: mmdeploy
    variant: mmpretrain
    version: 1.0.3
  architecture:
    family: mobileone
    variant: s2

taxonomy:
  root_taxon_id: 40151
  root_rank_level: 50
  output_rank_levels: [10, 20, 30, 40]

input:
  dims:
    min: [1, 3, 224, 224]
    opt: [1, 3, 224, 224]
    max: [1, 3, 224, 224]
  meta_available: false

output:
  schema: polli_v0
  format: json

providers:
  engine:
    docker_image: frontierkodiak/mmpre:1.0.3
  endpoint:
    docker_image: frontierkodiak/mmpre-serve-1.x:latest

metadata:
  region: USA
  clade: mammalia
```

### Amphibia

```yaml
version: petals-v0

model:
  name: petal.hClass.USA.amphibia.preview.xs.v0.0
  family: petal.hClass.preview
  type: hierarchical_classifier
  framework:
    family: mmdeploy
    variant: mmpretrain
    version: 1.0.3
  architecture:
    family: mobileone
    variant: s2

taxonomy:
  root_taxon_id: 20978
  root_rank_level: 50
  output_rank_levels: [10, 20, 30, 40]

input:
  dims:
    min: [1, 3, 224, 224]
    opt: [1, 3, 224, 224]
    max: [1, 3, 224, 224]
  meta_available: false

output:
  schema: polli_v0
  format: json

providers:
  engine:
    docker_image: frontierkodiak/mmpre:1.0.3
  endpoint:
    docker_image: frontierkodiak/mmpre-serve-1.x:latest

metadata:
  region: USA
  clade: amphibia
```

These manifest files follow the structure and details provided in the original example.