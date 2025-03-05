import fitz  # PyMuPDF
import requests
import nltk
import os
from nltk.tokenize import sent_tokenize, word_tokenize

#nltk.download('punkt')  # Ensure the tokenizer models are downloaded

example_string ="Muad'Dib learned rapidly because his first training was in how to learn."
'And the first lesson of all was the basic trust that he could learn.'
"It's shocking to find how many people do not believe they can learn, and how many more believe learning to be difficult."

print(sent_tokenize(example_string))
print(word_tokenize(example_string))

