# petal.Det.USA.generic.preview.md.v0.0
```yaml
version: petals-v0

model:
  name: petal.Det.USA.generic.preview.md.v0.0
  family: petal.Det.preview
  type: detector
  framework:
    family: mmdeploy
    variant: mmdetection
    version: 3.2.0
  architecture:
    family: RTMDet
    variant: medium  # or tiny

input:
  dims:
    min: [1, 3, 640, 640]
    opt: [1, 3, 640, 640]
    max: [1, 3, 640, 640]
  meta_available: false

output:
  schema: polli_v0
  format: json

providers:
  engine:
    docker_image: frontierkodiak/mmdet:3.2.0.cu11.1
  endpoint:
    docker_image: frontierkodiak/mmdet-serve-3.3:latest

metadata:
  region: generic
  scope: generic
```

# petal.Det.USA.generic.preview.xs.v0.0

```yaml
version: petals-v0

model:
  name: petal.Det.USA.generic.preview.xs.v0.0
  family: petal.Det.preview
  type: detector
  framework:
    family: mmdeploy
    variant: mmdetection
    version: 3.2.0
  architecture:
    family: RTMDet
    variant: tiny

input:
  dims:
    min: [1, 3, 640, 640]
    opt: [1, 3, 640, 640]
    max: [1, 3, 640, 640]
  meta_available: false

output:
  schema: polli_v0
  format: json

providers:
  engine:
    docker_image: frontierkodiak/mmdet:3.2.0.cu11.1
  endpoint:
    docker_image: frontierkodiak/mmdet-serve-3.3:latest

metadata:
  region: generic
  scope: generic
```