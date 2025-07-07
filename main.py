from transformers import pipeline

summarizer = pipeline("summarization")
file_name = input('Enter file name for summarization: (including .txt) ')

file = open(file_name, 'r')
text = file.read()
file.close()

summary = summarizer(text, max_length= (int(len(text)/2)), min_length=50, do_sample=False)

print(summary[0]['summary_text'])