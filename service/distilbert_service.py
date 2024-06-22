from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, pipeline


tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
sentiment_classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)


def get_result(sentences):
  return sentiment_classifier(sentences)
  # return "This is a placeholder for the DistilBERT model."
  