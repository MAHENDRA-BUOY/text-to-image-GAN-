# Text-to-Image Synthesis Using GANs

## Overview
This project focuses on **text-to-image synthesis** using **Generative Adversarial Networks (GANs)**. The implementation is inspired by **StackGAN, Wasserstein GAN-CLS, and Progressive Growing GANs (PGGAN)** to generate images based on textual descriptions.

## Dataset
- **Oxford-102 Flowers**: 8,192 images of 102 flower categories.
- **Caltech CUB-200 Birds**: 11,788 images of 200 bird species.
- **Data Augmentation**: Applied transformations like cropping and flipping to increase dataset diversity.

### Dataset Links
1. **Oxford-102 Flowers Dataset**: [Download](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/)
2. **Caltech CUB-200 Birds Dataset**: [Download](http://www.vision.caltech.edu/visipedia/CUB-200.html)

## Model Implementation
- **GAN Architecture**: Implemented **Generator** and **Discriminator** models using **Convolutional Neural Networks (CNNs)**.
- **Wasserstein GAN-CLS**: Improved stability by modifying loss functions.
- **StackGAN**: Multi-stage generation for higher image resolution.
- **Progressive GAN (PGGAN)**: Layer-wise image generation for smoother transitions.

## Technologies Used
- **Python**
- **TensorFlow/Keras**
- **Matplotlib & Seaborn** (for visualization)
- **NumPy**

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- TensorFlow/Keras
- NumPy
- Matplotlib & Seaborn

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-to-image-gan.git
   cd text-to-image-gan
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   ```bash
   python train_model.py
   ```
4. Generate images from text:
   ```bash
   python generate.py --text "A red rose with green leaves"
   ```

## Results
- The GAN successfully generates images based on textual descriptions.
- **StackGAN & PGGAN** produce higher resolution and visually coherent images.

## Contributing
Feel free to contribute by submitting issues or pull requests!

## License
This project is licensed under the **MIT License**.

## Acknowledgments
- **Oxford-102 & CUB-200 datasets** for providing high-quality labeled images.
- **TensorFlow & Keras** for deep learning frameworks.
- **StackGAN, Wasserstein GAN-CLS & PGGAN researchers** for improving GAN architectures.

