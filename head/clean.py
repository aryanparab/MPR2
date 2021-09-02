import re
from nltk.corpus import stopwords

def clean(text):
  words = stopwords.words('english')
  text = text.lower()
  text = re.sub('https?://[^\s<>"]+|www\.[^\s<>"]+',' ',text)
  text = re.sub('[^0-9a-z]',' ',text)
  text = " ".join([i for i in text.split() if  i not in stopwords.words('english')])
  return text