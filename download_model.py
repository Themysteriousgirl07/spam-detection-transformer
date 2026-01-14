import gdown

# Google Drive file ID (STRING)
FILE_ID = "1Snd5MM66qmjDYdkwEMzVdwJBGnTfXuMM"

OUTPUT = "model.safetensors"

# Correct Google Drive download URL for gdown
url = f"https://drive.google.com/uc?id={FILE_ID}"

print("Downloading model from Google Drive...")
gdown.download(url, OUTPUT, quiet=False)
print("Done! Model saved as", OUTPUT)
