#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Flatten, Reshape, Conv2DTranspose, Conv2D, LeakyReLU, BatchNormalization

# Load Dataset (Example: Oxford-102 Flowers or CUB-200 Birds)
def load_data():
    # Replace with actual dataset loading logic
    (X_train, _), (_, _) = keras.datasets.mnist.load_data()
    X_train = np.expand_dims(X_train, -1).astype('float32') / 255.0
    return X_train

# Define Generator Model
def build_generator():
    model = keras.Sequential([
        Dense(128 * 8 * 8, activation='relu', input_shape=(100,)),
        Reshape((8, 8, 128)),
        Conv2DTranspose(128, kernel_size=4, strides=2, padding='same', activation='relu'),
        BatchNormalization(),
        Conv2DTranspose(64, kernel_size=4, strides=2, padding='same', activation='relu'),
        BatchNormalization(),
        Conv2DTranspose(3, kernel_size=4, strides=2, padding='same', activation='tanh')
    ])
    return model

# Define Discriminator Model
def build_discriminator():
    model = keras.Sequential([
        Conv2D(64, kernel_size=4, strides=2, padding='same', input_shape=(64, 64, 3)),
        LeakyReLU(alpha=0.2),
        Conv2D(128, kernel_size=4, strides=2, padding='same'),
        LeakyReLU(alpha=0.2),
        Flatten(),
        Dense(1, activation='sigmoid')
    ])
    return model

# Compile GAN
def build_gan(generator, discriminator):
    discriminator.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0002), loss='binary_crossentropy', metrics=['accuracy'])
    discriminator.trainable = False
    gan_input = keras.Input(shape=(100,))
    fake_image = generator(gan_input)
    gan_output = discriminator(fake_image)
    gan = keras.Model(gan_input, gan_output)
    gan.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0002), loss='binary_crossentropy')
    return gan

# Training Function
def train_gan(generator, discriminator, gan, dataset, epochs=10000, batch_size=32):
    for epoch in range(epochs):
        noise = np.random.normal(0, 1, (batch_size, 100))
        fake_images = generator.predict(noise)
        real_images = dataset[np.random.randint(0, dataset.shape[0], batch_size)]
        labels_real = np.ones((batch_size, 1))
        labels_fake = np.zeros((batch_size, 1))
        
        d_loss_real = discriminator.train_on_batch(real_images, labels_real)
        d_loss_fake = discriminator.train_on_batch(fake_images, labels_fake)
        
        noise = np.random.normal(0, 1, (batch_size, 100))
        g_loss = gan.train_on_batch(noise, np.ones((batch_size, 1)))
        
        if epoch % 1000 == 0:
            print(f"Epoch {epoch}: D Loss Real={d_loss_real[0]}, D Loss Fake={d_loss_fake[0]}, G Loss={g_loss}")

# Load data and build models
dataset = load_data()
generator = build_generator()
discriminator = build_discriminator()
gan = build_gan(generator, discriminator)

# Train the GAN
train_gan(generator, discriminator, gan, dataset)

