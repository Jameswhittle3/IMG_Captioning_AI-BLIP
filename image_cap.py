import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Loads the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

img_path = "Rocket_Engine.png"
# Convert image to RGB format
image = Image.open(img_path).convert('RGB')

text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

# Generates a caption for the image
outputs = model.generate(**inputs, max_length=50)

# Decodes the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)

# Prints the caption
print(caption)