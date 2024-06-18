# models.py
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, pipeline as distilbert_pipeline
from transformers import pipeline as roberta_pipeline

# Model A
tokenizer_a = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model_a = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
sentiment_classifier = distilbert_pipeline('sentiment-analysis', model=model_a, tokenizer=tokenizer_a)

# Model B
classifier = roberta_pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
