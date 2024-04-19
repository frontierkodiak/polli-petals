

<p align="center">
  <img width="400" alt="PodOS v0 0 t 1044w@2x" src="assets/Polli Petals stack.jpg">
</p>

# Polli Petals

Polli Petals are the world's finest open taxonomic models. Petal models are standalone hierarchical taxonomic models released with vision-only and vision + context variants.

Petals models are trained on exclusively public data (primarily via [iNaturalist Open Data](https://github.com/inaturalist/inaturalist-open-data)). We provide tunes per-region and per-clade.

Training code, deployment utils, and additional variants will be made available as time permits. All models will be available for one-click deployment via our optimized cross-platform inference engine, [Polli Engine](https://polli.ai/software), upon its release in late 2024/early 2025.

We're currently developing an evaluation framework and will be publishing model performance metrics later this year. Let me know if you're interested in collaborating on this!

# Support Polli Petals
Developing and maintaining Polli Petals requires significant resources. If you'd like to support our mission of supercharging ecological research, please consider [contributing](https://donate.stripe.com/bIYaHPbZogMB2TC8ww) to Polli Petals. Your donation will be used to buy more GPUs, improve model quality, and accelerate our release roadmap.

Please contact us if you are interested in contributing data, especially for underrepresented regions or taxa.

# Model details

Unless otherwise specified, all models:
- Take static 224x224px image inputs.
- Were trained from scratch (no pretrained backbone/checkpoint).

Versioning:
- Taxa: Root clade of the model
- Region: Geographic region of the model
- Context: Whether the model includes context information
- Size: Parameter count.
- Quantization: Quantization level of the model (int8, fp16). If not specified, the model is in fp32.
- Major version: changes to the model architecture or training pipeline
- Minor version: changes to the model weights or hyperparameters
- Patch version: bug fixes or minor improvements

ex. `liliopsida.usa-l48.context.md.v1.0.0.pth`

Note that parameter count is an imperfect measure of inference costs. In practice, other factors (e.g. memory access costs) are more common bottlenecks. We will eventually provide standardized VRAM/latency benchmarks for common target platforms.

## Using Petals models
We provide Petals models in PyTorch format. Select models will also available as `.onnx` files with MMDeploy conversion configs, or occassionally in other platform-specific formats (e.g. CoreML, TensorRT). [Polli Engine](https://polli.ai/software) deployment (coming soon) will abstract this away by automatically detecting & pulling the best model format for your target platform.

Contact us if you need a model in a specific format and can't wait for Polli Engine.

Sample code for loading and using Petals models in PyTorch coming soon! Hierarchical/context models need particular code for tokenization & postprocessing, so we'll provide examples for those as well.


### Model metadata

Model metadata is stored in each model's release folder. Metadata is stored in different files depending on the model type, we're working on standardizing this.

All models include the following metadata:
- `taxonID`: iNaturalist taxonID of the model's root taxon
- `taxon`: common name of the model's root taxon
- 'levels': taxonomic levels (>1 for hierarchical models) for which the model provides predictions
- 'taxa': list of taxonIDs for which the model provides predictions (coming soon)


### Taxonomic predictions

We use iNaturalist's taxonID encodings. TaxonIDs are unique identifiers for each taxon in the iNaturalist taxonomy. You can find the iNaturalist taxonID for a given taxon by searching for it on the [iNaturalist website](https://www.inaturalist.org/).

We provide a sqlite database with the iNaturalist taxa name:taxonID mappings for all of primary taxonomic levels (kingdom, phylum, class, order, family, genus, species). This database is available in the `taxonomy` directory of this repository. Instructions & sample code for using this database coming soon! Polli Engine will automatically handle taxonID -> taxon name lookups for you.

# Classifiers

## Hierarchical vs. Single-level classifiers
Both single-level and hierarchical classifiers are available via Petals. Single-level classifiers return predictions for a single taxonomic level (ex. genus, species), while hierarchical classifiers return predictions for all levels in the taxonomic hierarchy below that model's root taxon. 

Hierarchical classifiers can be useful for suppressing false positives and sanity-checking the model's predictions. There are a lot of creative things you can do with these models, so we encourage you to experiment! 🙂

## Vision-only models

Vision-only Petals models are based on Apple's [MobileOne](https://machinelearning.apple.com/research/mobileone) architecture and are designed to be particularly lightweight. Most models target the S2 (8M), S3 (10M), or S4 (15M) size classes, which can be executed in <2ms on an iPhone 12. Some taxa are also available in our custom S5 (30M) size class.

Petals MobileOne models are trained with an in-house [MMPretrain](https://github.com/open-mmlab/mmpretrain/tree/main) fork. We do not yet have efficient (training) implementations of S0 (2M) and S1 (5M), although these may be provided in the future.

## Vision + context models

Vision + context Petals models are based on a custom fork of the [Metaformer](https://arxiv.org/abs/2111.11418) mixed-token transformer. These models take into account both visual and spatiotemporal context to make more informed predictions. Vision + context models are larger and slower than vision-only models, but they are more accurate and can provide more detailed information about the input. We currently release models based on the MetaFG_0 (28M), MetaFG_1 (45M), and MetaFG_2 (81M) architectures.

Vision + context models are currently only available as single-level models. Hierarchical vision + context releases are planned for later this year. [Polli Bouquet](https://polli.ai/software) employs a SOTA in-house mixed-token transformer architecture. Lagging versions are likely to be open-sourced in the future.

## Routers

Routing models are high-level classifiers used to select the best Petals model for a given input. We are not currently planning to release dedicated router models before Polli Engine is available, but we may consider releasing some upon request.

Routers are unnecessary when feeding hierarchical classifiers with Polli Detector models. We recommend using this approach for most applications.

# Detectors

Petals Detectors are object detection models, used to feed downstream classifiers. Some detectors also provide instance segmentations (tight masks around the specimen) to occlude background features. Detectors are not currently provided as a part of Polli Petals, but we plan to release some later this year.

Polli Engine will allow you to pass raw images and handle pipelining in the background.

# Model availability

# Polli Petals

Polli Petals are the world's finest open taxonomic models. Petal models are standalone hierarchical taxonomic models released with vision-only and vision + context variants.

Petals models are trained on exclusively public data (primarily via [iNaturalist Open Data](https://github.com/inaturalist/inaturalist-open-data)). We provide tunes per-region and per-clade.

Training code, deployment utils, and additional variants will be made available as time permits. All models will be available for one-click deployment via our optimized cross-platform inference engine, [Polli Engine](https://polli.ai/software), upon its release in late 2024/early 2025.

# Model details

## Vision-only models

Vision-only models are based on Apple's [MobileOne](https://machinelearning.apple.com/research/mobileone) architecture and are designed to be particularly lightweight. Most models target the S2, S3, or S4 size classes, which can be executed in <2ms on an iPhone 12. Some taxa are also available in our custom XL S5 size class.

Petals MobileOne models are trained with an in-house [MMPretrain](https://github.com/open-mmlab/mmpretrain/tree/main) fork.

## Vision + context models

# Model availability

All models will be available via [Hugging Face](https://huggingface.co/polli-caleb). Uploads will start in April 2024.

| Taxa            | USA-L48 | NA Eastern | NA Central | NA West | NA North (arctic/subarctic) | NA South (Southwest/North Mex) | Central America (inc. Southern Mexico) |
|-----------------|:-------:|:----------:|:----------:|:-------:|:---------------------------:|:------------------------------:|:---------------------------------------:|
| Router          |   ❌    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Router + context|   ❌    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Liliopsida       |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Liliopsida + context | ✅ |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Magnoliopsida    |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Magnoliopsida + context | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Mammalia        |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Mammalia + context | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Aves            |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Aves + context  |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Reptilia        |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Reptilia + context | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Amphibia        |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Amphibia + context | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Hemiptera       |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Hemiptera + context | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Lepidoptera     |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Lepidoptera + context | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Odonata         |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Odonata + context | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Orthoptera      |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Orthoptera + context | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Coleoptera      |   ✅    |     ❌     |     ❌     |   ❌    |             ❌              |               ❌               |                   ❌                    |
| Coleoptera + context | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Diptera         |   ✅    |     ❌     |     ❌     |   ❌    |             ❌             |

## Regional roadmap

We plan to extend the availability of Polli Petals to additional regions across the globe. We are currently constrained by dataset availability (especially outside of NA/Europe) and our available compute. The following regional tunes are currently planned:

- Europe West
- Europe North
- Europe East
- Mediterranean
- Australia/NZ
- Southeast Asia
- East Asia
- Central Asia
- South Asia
- Southwest Asia
- Northwest Asia
- South America
- Africa

*Please contact us if you are interested in supporting the development of our regional models. We are particularly interested in collaborating with local organizations and researchers to improve the quality of our models.*

## Tech roadmap
- Higher-res (>224px) & dynamic classifiers.
- Hierarchical vision + context (mixed-token) releases.
- Taxonomic generalists.
- Some dataset & pretraining tricks from Bouquet.
- New mixed-token vision transformer arch.
