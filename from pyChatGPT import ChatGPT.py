import string
import os
from collections import OrderedDict
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import defaultdict


#--------------------------------------------
clear = lambda: os.system('cls') # on Windows System
os.system('clear') # on Linux System
clear()
#---------------------------------------------
# Load the text from a file
with open('data/DG.txt', encoding='UTF-8') as file:
      text = file.read()

# Remove punctuation and convert to lowercase
exclude = set(string.punctuation)
text = ''.join(ch for ch in text if ch not in exclude).lower().strip()
text = ''.join(s for s in text if s not in ('“', '”', '’'))
text = ''.join([i for i in text if not i.isdigit()])
# Tokenize the text into words
words = word_tokenize(text)

# Remove stopwords
stops = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stops]
words = filtered_words
# Create a frequency distribution of words
fr = FreqDist(filtered_words)
fr_dict = dict(fr.most_common(300))

# Print the most common words
for word, frequency in fr_dict.items():
    print(word, ':', frequency)

# Generate and display the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(fr_dict)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Initialize the defaultdict with dictionaries as default values
mc_dict = defaultdict(lambda: defaultdict(int))
# Populate the mc_dict
for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    mc_dict[word][next_word] += 1

# Calculate transition probabilities within mc_dict
for word, next_word_counts in mc_dict.items():
    total_transitions = sum(next_word_counts.values())

    for next_word, count in next_word_counts.items():
        mc_dict[word][next_word] = count / total_transitions

# Convert the defaultdict to a regular dictionary if needed
mc_dict = dict(mc_dict)


for k in list(mc_dict.keys()):
    if k in ('e', 'b', 'pg', 'ut', 'irs', '•', 'f', 'c', 'facility', 'wwwgutenbergorgdonate'):
          mc_dict.pop(k)    
for key, value in mc_dict.items():
    print(key, ':', value) 

 