from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(user_text):
  summary = summarizer(user_text, max_length= (int(len(user_text)/2)), min_length=50, do_sample=False)
  return summary
