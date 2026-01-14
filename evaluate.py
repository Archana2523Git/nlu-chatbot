import json
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from llm_nlu import analyze  # Import your real analyze() function here

# -------------------------
# 1️⃣ Load dataset
# -------------------------
with open("eval_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [item["text"] for item in data]
true_intents = [item["intent"] for item in data]

# -------------------------
# 2️⃣ Analyze each text using Ollama
# -------------------------
predicted_intents = []

for text in texts:
    result = analyze(text)  # Must return {'intent': 'predicted_intent', 'confidence': 0.xx}
    predicted_intents.append(result["intent"])

# -------------------------
# 3️⃣ Compute metrics
# -------------------------
accuracy = accuracy_score(true_intents, predicted_intents)
precision, recall, f1, _ = precision_recall_fscore_support(
    true_intents, predicted_intents, average="weighted", zero_division=0
)
cm = confusion_matrix(true_intents, predicted_intents, labels=list(set(true_intents)))

print("===== EVALUATION RESULTS =====")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")
print("\nConfusion Matrix:\n")
print(cm)

# -------------------------
# 4️⃣ Plot confusion matrix
# -------------------------
plt.figure(figsize=(12, 10))
sns.heatmap(cm, annot=True, fmt="d", xticklabels=list(set(true_intents)),
            yticklabels=list(set(true_intents)), cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
plt.show()
