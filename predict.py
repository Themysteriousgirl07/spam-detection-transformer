import sys
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Read text from command-line argument
if len(sys.argv) < 2:
    print("No input text provided")
    sys.exit(1)

text = sys.argv[1]

# Load  model
tokenizer = AutoTokenizer.from_pretrained("spam_model")
model = AutoModelForSequenceClassification.from_pretrained("spam_model")
model.eval()

torch.set_num_threads(1)

# Tokenize 
inputs = tokenizer(
    text,
    padding=True,
    truncation=True,
    max_length=128,
    return_tensors="pt"
)

# Predict
with torch.no_grad():
    outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1).item()

# Output 
print("SPAM" if pred == 1 else "HAM")
