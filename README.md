<!-- #region -->
# Semantic fetal MR image synthesis using Med-DDPM

Semester project description

## Synthetic Samples for Given Input Mask:

<!-- #endregion -->

## 🛠️ Setup 

Ensure you have the following libraries installed for training and generating images:

- **Torchio**: [Torchio GitHub](https://github.com/fepegar/torchio)
- **Nibabel**: [Nibabel GitHub](https://github.com/nipy/nibabel)

```
pip install -r requirements.txt
```

## 🚀 Run on Your Own Dataset

Med-DDPM is versatile. If you're working with image formats other than NIfTI (.nii.gz), modify the \`read_image\` function in \`dataset.py\`.

1. Specify the segmentation mask directory with \`--inputfolder\`.
2. Set the image directory using \`--targetfolder\`.
3. If you have more than 3 segmentation mask label classes, update channel configurations in \`train.py\`, \`datasets.py\`, and \`utils/dtypes.py\`.

## 🎓 Training 

Specify dataset paths using \`--inputfolder\` and \`--targetfolder\`:

### Image Dimensions

- Whole-head MRI synthesis: 128x128x128
- Brain-extracted 4 modalities (T1, T1ce, T2, Flair) synthesis (BraTS2021): 192x192x144

```
whole-head MRI synthesis:$ ./scripts/train.sh
(BraTS) 4 modalities MRI synthesis:$ ./scripts/train_brats.sh
```

## 🧠 Model Weights

Get our optimized model weights for both whole-head MRI synthesis and 4-modalities MRI synthesis from the link below:

[Download Model Weights](https://drive.google.com/drive/folders/1t6jk5MrKt34JYClgfijlbNYePIcTEQvJ?usp=sharing)

After downloading, place the files under the "model" directory.

## 🎨 Generating Samples

To create images, follow these steps:

### Image Dimensions

- Whole-head MRI synthesis: 128x128x128
- Brain-extracted 4 modalities (T1, T1ce, T2, Flair) synthesis (BraTS2021): 192x192x144

### Usage

- Set the learned weight file path with \`--weightfile\`.
- Determine the input mask file using \`--inputfolder\`.

```
whole-head MRI synthesis:$ ./scripts/sample.sh
(BraTS) 4 modalities MRI synthesis:$ ./scripts/sample_brats.sh
```



```python

```
