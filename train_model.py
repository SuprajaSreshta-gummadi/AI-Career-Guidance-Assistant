import json
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)


training_sentences = []
training_labels = []


# Prepare training data
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        training_sentences.append(pattern)
        training_labels.append(intent["tag"])


# Convert text into numerical features
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X = vectorizer.fit_transform(training_sentences)


# Train the machine learning model
model = LogisticRegression(max_iter=1000)

model.fit(X, training_labels)


# Save the trained model
with open("intent_model.pkl", "wb") as file:
    pickle.dump(model, file)


# Save the vectorizer
with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)


print("Model training completed successfully!")
print("intent_model.pkl created")
print("vectorizer.pkl created")