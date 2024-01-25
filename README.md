<!-- #region -->
# Semantic fetal MR image synthesis using Med-DDPM

Semester project description

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
3. If you have more than 4 segmentation mask label classes, update channel configurations in \`train.py\`, \`datasets.py\`, and \`utils/dtypes.py\`.

## 🎓 Training 

Specify dataset paths using \`--inputfolder\` and \`--targetfolder\`:

### Image Dimensions

- Whole-head MRI synthesis: 128x128x128 - 256x256x256
- Optionally: Define image size in \`diffusion_model/unet.py\`

```
whole-head MRI synthesis:$ ./scripts/train.sh
```

## 🧠 Model Weights

Requests to access the model weights and fetal datasets should be directed to: [Andras Jakab](andras.jakab@kispi.uzh.ch)


After obtaininig and downloading the model weights, place the files under the "model" directory.

## 🎨 Generating Samples

To create images, follow these steps:

### Image Dimensions

- Whole-head MRI synthesis: 128x128x128 - 256x256x256

### Usage

- Set the learned weight file path with \`--weightfile\`.
- Determine the input mask file using \`--inputfolder\`.

```
whole-head MRI synthesis:$ ./scripts/sample.sh
```



