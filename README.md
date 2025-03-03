# Text-to-Image GAN Generator

## Overview

This project implements a **Text-to-Image Generation System** using **Generative Adversarial Networks (GANs)**. The model generates images based on textual descriptions and can be integrated into a web-based application.

## Dataset

The project is trained on the **Oxford-102 Flowers** and **Caltech CUB-200 Birds** datasets, widely used for text-to-image synthesis.

### Dataset Links

- [Oxford-102 Flowers](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/)
- [Caltech CUB-200 Birds](http://www.vision.caltech.edu/visipedia/CUB-200.html)

## Technologies Used

- **Python** (GAN Model & Backend)
- **PyTorch** (Deep Learning Framework)
- **Flask & Express.js** (Backend APIs)
- **React.js** (Frontend UI)
- **TensorFlow** (Additional Preprocessing)
- **Node.js** (Server-side execution)

## Installation & Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- TensorFlow & PyTorch
- Flask & Express.js
- React.js & Node.js

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-to-image-gan.git
   cd text-to-image-gan
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the backend API:
   ```bash
   cd backend
   python app.py
   ```
4. Start the Node.js API:
   ```bash
   cd api
   npm install
   node server.js
   ```
5. Start the frontend:
   ```bash
   cd frontend
   npm install
   npm start
   ```

## How to Load Models

### Load the GAN Model in Python

```python
import torch
from models import Generator

# Load Generator model
generator = Generator()
generator.load_state_dict(torch.load("generator.pth"))
generator.eval()
print("Model Loaded Successfully!")
```

### Load API Server (Node.js)

```javascript
const express = require('express');
const app = express();
app.listen(5000, () => console.log("Server running on port 5000"));
```

## Key Code Components

- **GAN Model**: Uses a deep convolutional GAN for high-quality text-to-image synthesis.
- **Flask API**: Backend for generating images using Python.
- **Node.js API**: Bridges the model with the frontend.
- **React.js Frontend**: Allows users to generate and view images.

## Summary

✔ **Step 1:** Install dependencies\
✔ **Step 2:** Load GAN Model & APIs\
✔ **Step 3:** Start backend & frontend\
✔ **Step 4:** Generate images using GAN\
✔ **Step 5:** Display results in the web UI

## External Description

The **Text-to-Image GAN Generator** leverages deep learning to generate realistic images from text descriptions. The system integrates **GAN-based synthesis, API services, and a web interface** for user interaction. This is useful for applications in **artificial creativity, data augmentation, and automated image generation**.

## Contributing

Feel free to contribute by submitting issues or pull requests!

## License

This project is licensed under the **MIT License**.

## Acknowledgments

- **Oxford-102 & CUB-200 datasets** for providing high-quality labeled images.
- **PyTorch & TensorFlow** for deep learning frameworks.
- **Flask, Express.js & React.js** for full-stack integration.

