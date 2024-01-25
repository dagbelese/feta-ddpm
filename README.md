<!-- #region -->
# Semantic fetal MR image synthesis using Med-DDPM

This is a forked Github repository containing the code used for my semester project conducted in the University Children's Hospital Zürich and Swiss Federal Institute of Technology.

In this semester project, [Med-DDPM](https://github.com/fepegar/torchio](https://github.com/mobaidoctor/med-ddpm/tree/main)), a denoising diffusion probabilistic model, is employed to generate high-quality 3D MR images of the developing human brain, attempting to address some of the limitations of traditional GAN-based methods. The work focuses on developing and refining the existing Med-DDPM for semantic 3D MRI synthesis using brain tissue label maps and compares its performance with the SPADE GAN method. Results demonstrate Med-DDPM's capabilities to generate realistic, anatomically detailed, coherent fetal MR images with improved statistical accuracy and signal clarity. However, it falls short in reliably and consistently producing these high-quality images compared to SPADE GAN. This exploration contributes to the field of medical imaging by offering a novel approach for generating realistic fetal MRIs from a label map representing anatomical brain tissues.

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

- Fetal MRI synthesis: 128x128x128 - 256x256x256
- Optionally: Define image size in \`diffusion_model/unet.py\`

```
fetal MRI synthesis:$ ./scripts/train.sh
```

## 🧠 Model Weights

Requests to access the model weights and fetal datasets should be directed to: [Andras Jakab](andras.jakab@kispi.uzh.ch)


After obtaininig and downloading the model weights, place the files under the "model" directory.

## 🎨 Generating Samples

To create images, follow these steps:

### Image Dimensions

- Fetal MRI synthesis: 128x128x128 - 256x256x256

### Usage

- Set the learned weight file path with \`--weightfile\`.
- Determine the input mask file using \`--inputfolder\`.

```
fetal MRI synthesis:$ ./scripts/sample.sh
```



