# Generative AI-Powered Image Captioning

This project implements an image captioning web application using the BLIP model from Hugging Face Transformers. The app generates descriptive captions for any uploaded image.

## Overview

- Uses the `Salesforce/blip-image-captioning-base` pretrained model.
- Provides a simple Gradio interface for users to upload images and receive captions.
- Developed and tested within the Cloud IDE environment provided by the IBM Skills Network.


## How to Run

image_captioning_app.py
1. Ensure you have the required libraries installed:
   ```bash
   pip install gradio transformers Pillow
2. Run the app: python3 image_captioning_app.py
3. Open the Gradio interface URL shown in the terminal to upload images and get captions.

automate_url_captioner.py
1. Ensure you have the required libraries installed:
   ```bash
   pip install gradio transformers Pillow
2. Run the app: python3 automate_url_captioner.py
3. As an output, you will have a new file in the explorer (same directory) with the name: captions.txt
