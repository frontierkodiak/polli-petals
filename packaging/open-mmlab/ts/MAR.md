# MMDetection



# MMPretrain

### Current
#### Setup export environment:
```bash
# blade
docker run --shm-size=8g -it -v /banana:/banana -v /local-data:/local-data -v /home/caleb/repo/Polli-Brain/mmpre/1.x:/workspace/mmpretrain -v /pond/petals:/petals -v /peach:/peach -v /pond/modelZoo:/modelZoo frontierkodiak/mmpre:1.0.3
```

#### Make the MARs, upload to PolliServe
TODO: Decide-- uploading to PolliServe? Backblaze? or huggingface?

Output mars to '/petals/preview/hClass/<MAR_NAME>.
    MAR_NAME ex. `petal.hClass.USA.aves.preview.xs.v0.0`

```bash
RAW_BASE="/petals/raw" # TODO: Update path to 'petals'
OUT_BASE="/petals/preview/hClass"
EXTRA_FILES="mmpretrain/apis/multiTask_image_classification.py,mmpretrain/apis/baseMulti.py,mmpretrain/apis/modelMulti.py,mmpretrain/datasets/transforms/transform_utils.py"


# Common metadata
FAMILY="petal.hClass.preview"
MODEL_ARCH_FAMILY="mobileone"
MODEL_ARCH_VAR="s2" # NOTE: Angio is s3
MODEL_FRAMEWORK_FAMILY="mmdeploy"
MODEL_FRAMEWORK_VARIANT="mmpretrain"
MODEL_FRAMEWORK_VARIANT_VERSION="1.0.3"
ENGINE_DOCKER_IMAGE="frontierkodiak/mmpre:1.0.3" # latest?
ENDPOINT_DOCKER_IMAGE="frontierkodiak/mmpre-serve-1.x:latest"
MODEL_TYPE="hierarhical_classifier"
REGION="USA"

# FUTURE: Pull i/o metadata from config.py files. Can hardcode for now.
INPUT_DIM_MIN=[1, 3, 224, 224] # [batch, channel, height, width]
INPUT_DIM_OPT=[1, 3, 224, 224] # optimal
INPUT_DIM_MAX=[1, 3, 224, 224]
INPUT_META_AVAILABLE="false" # No meta tokens available on polli preview
OUTPUT_SCHEMA="polli_v0" # NOTE: json should include schema
OUTPUT_FORMAT="json" # VERIFY

# Per-export metadata

### CLADE is one of: angiospermae/arthropoda/aves/mammalia/reptilia/amphibia
CLADE="arthropoda"
EXPERIMENT="E21.1.4.arthro"
CKPT="best_L10_accuracy_top1_epoch_240"
MODEL_NAME="petal.hClass.USA.arthro.preview.xs.v0.0"
ROOT_RANK_LEVEL="60"
ROOT_TAXON_ID="47120"
OUTPUT_RANK_LEVELS="[10, 20, 30, 40, 50]"

CLADE="reptilia"
EXPERIMENT="E21.1.5.reptilia"
CKPT="best_L10_accuracy_top1_epoch_240"
MODEL_NAME="petal.hClass.USA.reptilia.preview.xs.v0.0"
ROOT_RANK_LEVEL="50"
ROOT_TAXON_ID="26036"
OUTPUT_RANK_LEVELS="[10, 20, 30, 40]"

CLADE="aves"
EXPERIMENT="E21.1.4.aves"
CKPT="best_L10_accuracy_top1_epoch_277"
MODEL_NAME="petal.hClass.USA.aves.preview.xs.v0.0"
ROOT_RANK_LEVEL="50"
ROOT_TAXON_ID="3"
OUTPUT_RANK_LEVELS="[10, 20, 30, 40]"

CLADE="angio"
EXPERIMENT="E24.4.3.angio"
CKPT="best_L10_accuracy_top1_epoch_54"
MODEL_NAME="petal.hClass.USA.angio.preview.sm.v0.0"
ROOT_RANK_LEVEL="57"
ROOT_TAXON_ID="47125"
MODEL_ARCH_VAR="s3"
OUTPUT_RANK_LEVELS="[10, 20, 30, 40, 50]"

CLADE="mammalia"
EXPERIMENT="E24.1.6.mammalia"
CKPT="best_L10_accuracy_top1_epoch_212"
MODEL_NAME="petal.hClass.USA.mammalia.preview.xs.v0.0"
ROOT_RANK_LEVEL="50"
ROOT_TAXON_ID="40151"
OUTPUT_RANK_LEVELS="[10, 20, 30, 40]"

CLADE="amphibia"
EXPERIMENT="E24.1.6.amphibia"
CKPT="best_L10_accuracy_top1_epoch_218"
MODEL_NAME="petal.hClass.USA.amphibia.preview.xs.v0.0"
ROOT_RANK_LEVEL="50"
ROOT_TAXON_ID="20978"
OUTPUT_RANK_LEVELS="[10, 20, 30, 40]"

# TODO: Finalize manifest.yaml schema (schema version=="petals-v0")
# TODO: Script to generate manifest.yaml from these vars (Do not read from config, tabling this for the future)
# NOTE: I think this metadata is sufficient. Remember this is v0 for the preview release.
# TODO: New handlers:
# - [ ] Read taxonID_mapping.json, convert outputs
# - [ ] Include results schema tag in results json.
    - We will read this from the manifest.yaml. For now, all results will be in polli-v0 schema (which has not yet been finalized).
# TODO: Everything below!

python tools/torchserve/mmpretrainMulti2torchserve.py "${WORK_DIR_BASE}${EXPERIMENT}/${EXPERIMENT}.py" "${WORK_DIR_BASE}${EXPERIMENT}/${CKPT}.pth" --output-folder "${MODEL_ZOO_BASE}${CLADE}/${EXPERIMENT}" --model-name "${MAR_NAME}" --extra-files "${EXTRA_FILES}" -f


# Check model destination
echo "${MODEL_ZOO_BASE}${CLADE}/${EXPERIMENT}"
# Outside the container
gzip -k "/pond${MODEL_ZOO_BASE}${CLADE}/${EXPERIMENT}/${MAR_NAME}.mar" && rsync -avz "/pond${MODEL_ZOO_BASE}${CLADE}/${EXPERIMENT}/${MAR_NAME}.mar.gz" "caleb@polliserve:~/assets/models/ts/${MAR_NAME}.mar.gz"

# If the config and raw ckpt haven't been put in brain zoo yet..
cp "/banana-pool/banana/mm-work-dirs/${EXPERIMENT}/${CKPT}.pth" "/pond${MODEL_ZOO_BASE}${CLADE}/${EXPERIMENT}/" && cp "/banana-pool/banana/mm-work-dirs/${EXPERIMENT}/${EXPERIMENT}.py" "/pond/${MODEL_ZOO_BASE}${CLADE}/${EXPERIMENT}/"
# If you want to load directly into mmpre-serve-1 model store:
cp "/pond${MODEL_ZOO_BASE}${CLADE}/${EXPERIMENT}/${MAR_NAME}.mar" /banana/Brain/ts/mmpre-serve-1.x/models/
```