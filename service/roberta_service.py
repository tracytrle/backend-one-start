from transformers import pipeline
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

def get_result(sentences):
  return classifier(sentences)
  