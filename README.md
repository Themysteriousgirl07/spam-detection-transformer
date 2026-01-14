# spam-detection-transformer
Spam Detection using Transformer Models (C + Python)
Brief intructions about the project , downloading and setup:
This project implements a spam detection system using a Transformer-based NLP model (DistilBERT).
The system integrates **C and Python** to classify text messages as **Spam** or **Ham**.
The focus of this project is on building the **core ML pipeline and system integration**, not UI or deployment.
## Features
- Transformer-based spam classification
- Context-aware text understanding
- C → Python integration
- Reproducible setup using a model download script

## Setup Instructions
### 1. Download the model weights
The trained model weights are not included in this repository due to file size limitations.
Run the following commands in command prompt:
python -m pip install gdown
python download_model.py
This will download the file model.safetensors into the project directory.
## Manual download (backup option)
If the script does not work, download the model manually from Google Drive:

https://drive.google.com/file/d/1Snd5MM66qmjDYdkwEMzVdwJBGnTfXuMM/view

Place the downloaded file in the project root directory as:
model.safetensors
## 2.Running the Project
Compile and execute:
gcc main.c -o spam
./spam or spam 

## To run this project, the following prerequisites are required:
Python3.9 or higher 
PyTorch
Hugging Face Transformers
gdown
C Complier (GCC)
