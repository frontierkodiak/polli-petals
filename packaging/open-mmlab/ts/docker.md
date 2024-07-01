# MMDet TorchServe

## Build

## Run

### mmdet-serve-3.3
==current-experimental==

```bash
# TODO: Update MARs.
XS_MODEL=
MD_MODEL=

### BLADE / WSL
docker run \
--restart=unless-stopped \
--shm-size=2g \
--cpus 2 \
--gpus device=1 \
-v /banana/Brain/ts/mmdet-serve-3.x/models:/home/model-server/model-store \
-v /banana/Brain/ts/mmdet-serve-3.x/configs:/configs \
-v /banana/Brain/ts/mmdet-serve-3.x/logs:/logs \
-e LOG_LOCATION=/logs \
-p 8080:8080 -p 8081:8081 -p 8082:8082 \
--name mmdet-serve-3.3 \
frontierkodiak/mmdet-serve-3.3:latest \
torchserve --model-store=/home/model-server/model-store --models "${XS_MODEL} ${MD_MODEL}"
```
*If issues, try mmdet-serve-3.x.*

# MMPre TorchServe

## Build

## Run

### mmpre-serve-1.x

==current==
*Overloads WSL 16GB RAM if all 4 models are loaded.*

```bash
# TODO: Update MARs. Add mammalia, amphibia.
PLANT_MODEL=
AVES_MODEL=
INSECTA_MODEL=
REPTILE_MODEL=
AMPHIBIA_MODEL=
MAMMALIA_MODEL=
MODELS="${AVES_MODEL} ${INSECTA_MODEL} ${REPTILE_MODEL} ${PLANT_MODEL} ${AMPHIBIA_MODEL} ${MAMMALIA_MODEL}"

### BLADE / WSL
docker run \
--restart=unless-stopped \
--shm-size=2g \
--cpus 1 \
--gpus device=1 \
-v /banana/Brain/ts/mmpre-serve-1.x/models:/home/model-server/model-store \
-v /banana/Brain/ts/mmpre-serve-1.x/configs:/configs \
-v /banana/Brain/ts/mmpre-serve-1.x/logs:/logs \
-e LOG_LOCATION=/logs \
-p 8086:8080 -p 8087:8081 -p 8088:8082 \
--name mmpre-serve \
frontierkodiak/mmpre-serve-1.x:latest \
torchserve --model-store=/home/model-server/model-store --models "${MODELS}" --ts-config '/configs/config.properties'
```