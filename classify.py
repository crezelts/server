from transformers import pipeline

# Step 1: Initialize the Zero-shot classification pipeline with BART model
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

# Step 2: Define the candidate labels (possible intents)
labels = ["summary", "search", "question", "conversation", "weather", "recommand"] # "translation"

# Step 3: Classify the input text
def classify_intent(user_input):
    result = classifier(user_input, candidate_labels=labels)
    return result['labels'][0]  # 가장 높은 확률을 가진 라벨을 반환

