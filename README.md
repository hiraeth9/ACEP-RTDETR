# ACEP-RTDETR

This repository is the **official and canonical implementation of ACEP-RTDETR** associated with the manuscript:

**ACEP-RTDETR: Degradation-aware Representation Enhancement for Underwater Small-object Detection**

ACEP-RTDETR is a degradation-aware pre-query representation enhancement framework for underwater small-object detection. It is developed based on the RT-DETR implementation in the Ultralytics framework.

The proposed framework contains three main components:

- **GHCEB (Grouped Half Convolution Enhanced Block)** for local structural enhancement.
- **ACEU (Attention Convolution Enhancement Unit)** for semantic and locality-sensitive representation enhancement.
- **PEFAS (Pyramid ELAN Feature Aggregation Structure)** for hierarchical contextual aggregation before query selection.

The implementation in this repository corresponds to the experiments reported in the manuscript and should be regarded as the **canonical ACEP-RTDETR release**, rather than an unmodified upstream Ultralytics repository.

## Main Datasets

The experiments reported in the manuscript include:

- URPC2020
- UDD
- UODD
- DUO

## Main Results

| Dataset | mAP50 (%) | mAP50:95 (%) |
|---|---:|---:|
| URPC2020 | 84.5 | 48.8 |
| UDD | 65.2 | 28.6 |
| DUO | 84.1 | 62.2 |

## Environment

The main experiments were conducted using:

- PyTorch
- CUDA 11.8
- NVIDIA GeForce RTX 4090
- Input size: 640 × 640
- Batch size: 4
- Random seed: 60

## Code Availability

The source code and implementation files corresponding to ACEP-RTDETR are provided in this repository for research and reproducibility purposes.

## Acknowledgements

This implementation is developed based on the Ultralytics RT-DETR framework. We sincerely thank the original authors and open-source community for their contributions.
