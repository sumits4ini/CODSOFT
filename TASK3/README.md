# 🖼️ Image Captioning AI

> **CodSoft Artificial Intelligence Internship - Task 3**

An AI-powered Image Captioning system that combines **Computer Vision** and **Natural Language Processing (NLP)** to automatically generate meaningful captions for images. This project was developed as part of the **CodSoft AI Internship Program (Task 3: Image Captioning)**.

## 📌 Internship Task Details

**Internship:** CodSoft Artificial Intelligence Internship

**Task Number:** Task 3

**Task Name:** Image Captioning AI

**Objective:**
Build an AI model that can automatically generate descriptive captions for images by combining computer vision and natural language processing techniques. The system uses a pre-trained image recognition model for feature extraction and a transformer-based language model for caption generation.

## 📌 Project Overview

Image Captioning is a challenging task that bridges the gap between computer vision and natural language understanding. The model analyzes the visual content of an image and generates a human-like textual description of what it sees.

This project demonstrates how modern transformer-based architectures can be used to generate accurate and context-aware image captions.

## 🚀 Features

* Generate captions from input images automatically
* Uses a pre-trained transformer-based image captioning model
* Supports various image formats (JPG, PNG, JPEG)
* Easy to run and customize
* Suitable for AI/ML learning and portfolio projects

## 🛠️ Technologies Used

* Python
* PyTorch
* Transformers (Hugging Face)
* Vision Transformer (ViT)
* GPT-2
* Pillow (PIL)

## 📂 Project Structure

```text
TASK3/
│
├── predict.py          # Main script for caption generation
├── sample.jpg          # Sample input image
├── README.md           # Project documentation
```

## ▶️ Usage

Place an image named `sample.jpg` inside the project folder and run:

```bash
python predict.py
```

## 📸 Example

### Input Image

Add your image as:

```text
sample.jpg
```

### Output

```text
Generated Caption:
a dog running through a grassy field
```

## 💻 Sample Code

```python
image = Image.open("sample.jpg")

pixel_values = processor(
    images=image,
    return_tensors="pt"
).pixel_values

output_ids = model.generate(
    pixel_values,
    max_length=20
)

caption = tokenizer.decode(
    output_ids[0],
    skip_special_tokens=True
)

print(caption)
```

## 📈 Applications

* Assistive technology for visually impaired users
* Image search and indexing
* Automated content generation
* Social media caption suggestions
* Digital asset management

## 🎯 Future Improvements

* Real-time webcam image captioning
* Support for batch image processing
* Fine-tuning on custom datasets
* Web application deployment using Flask or Streamlit
* Multilingual caption generation

## 📷 Project Output

| Image         | Generated Caption                     |
| ------------- | ------------------------------------- |
| Dog Image     | A dog running through a grassy field  |
| Bicycle Image | A person riding a bicycle on a street |
| Cat Image     | A white cat sitting on a sofa         |

## 👨‍💻 Author

**Sumit**

AI & Machine Learning Enthusiast
---

⭐ If you found this project helpful, consider giving it a star on GitHub!
