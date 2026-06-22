import warnings
warnings.filterwarnings("ignore")

from transformers import (
    VisionEncoderDecoderModel,
    ViTImageProcessor,
    AutoTokenizer,
    logging
)
from PIL import Image
import torch

logging.set_verbosity_error()

model_name = "nlpconnect/vit-gpt2-image-captioning"

print("Loading model...")

model = VisionEncoderDecoderModel.from_pretrained(model_name)
processor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

tokenizer.pad_token = tokenizer.eos_token

image = Image.open("sample.jpg")

if image.mode != "RGB":
    image = image.convert("RGB")

pixel_values = processor(
    images=image,
    return_tensors="pt"
).pixel_values

output_ids = model.generate(
    pixel_values,
    max_length=16,
    num_beams=4,
    early_stopping=True,
    pad_token_id=tokenizer.pad_token_id
)

caption = tokenizer.decode(
    output_ids[0],
    skip_special_tokens=True
)

print("\nGenerated Caption:")
print(caption)