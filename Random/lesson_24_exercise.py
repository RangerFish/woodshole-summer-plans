#---SE370 Lesson 24 Lecture/Exercise---#
#-By: Ian Kloo
#-March 2025

import os
os.getcwd()

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# pip install -U spacy
# python -m spacy download en_core_web_sm
#spacy is a package that wraps together a bunch of other technology for natural language processing
#there are many other ways to do these taks, but spacy gives a nice single interface
import spacy

# pip install spacytextblob
# python -m textblob.download_corpora
#we need to install the spacytextblob package to do sentiment analysis
#this package is a wrapper around the textblob package, which is a wrapper around the nltk package
#this is a good example of how packages can be built on top of each other
from spacytextblob.spacytextblob import SpacyTextBlob

#things to do:
#1. Reading in text data 
#2. Cleaning/normalizing text data
#3. Making nice plots -- wordclouds, barplots
#4. Named entity recognition
#5. Sentiment analysis

#---basic processing with Spacy
#read in a dataset with comments on new york times articles
df = pd.read_csv('nyt_comments_sample.csv')
#lets just work with 1000 comments for now
df = df[:1000]
df.head(3)

df['commentBody'].tolist()[10][5]

#-tokenization/cleaning

#specify an nlp pipeline and model
nlp = spacy.load('en_core_web_sm')
#process all of the reviews using the nlp pipeline
docs = list(nlp.pipe(df['commentBody']))

#-lemmatization
#lets look at the lemmatized text.  the document is broken into individual words.  the lemma_ attribute gives the root form of the word
docs[10]
docs[10][5]
docs[10][5].lemma_

#print all of the lemma forms of the words in the 10th comment
for word in docs[10]:
    print(word.lemma_)

#-stopwords and punctuation
#each word also gets an attribute stating if it is a "stopword"
#these are common words that are often removed in text processing
docs[10][5]
docs[10][5].is_stop


docs[10][0]
docs[10][0].is_stop

#a common task is removing all stopwords


#we might also want to remove all punctuation 


#-!Exercise: Make a single list of all words (for all reviews) that are not stopwords or punctuation.  Only store the
#lemmatized version of the text.  Also, set the text to lowercase.
#Hint: use a nested loop - one to loop over the comments and another to loop over the words within each comment.
all_text = []

for doc in docs:
    for word in doc:
        if not word.is_stop and not word.is_punct:
            all_text.append(word.lemma_.lower())

all_text

#---visualization
#we now have a "bag of words" representation of our text data
#we can now make simple plots based on word frequency to get a sense for what is in the data

#-barplot of word frequency
#let's just do the top 20 words
word_df = pd.DataFrame(all_text, columns = ['word'])
word_df.head()
word_counts = word_df['word'].value_counts().sort_values(ascending = False).reset_index(name ='counts')
word_counts.head()

# first 20 words
plot_df = word_counts[:20]

fig, ax = plt.subplots()
ax.bar(plot_df['word'], plot_df['count'])
ax.set_xticklabels(labels = plot_df['word'], rotation = 45, ha = 'right')

words_to_remove = ['<', ' ']
word_df = word_df[~word_df['word'].isin(words_to_remove)]

word_counts = word_df['word'].value_counts().sort_values(ascending= False).reset_index(name ='counts')

#-wordclouds are another way to show text frequency
#the wordcloud function just takes a single string, so we need to recombine everything:
text_to_cloud = ' '.join(word_df['word'])
wordcloud = WordCloud().generate(text_to_cloud)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

import re
text_to_cloud2 = re.sub('<.*>', '', text_to_cloud)

wordcloud = WordCloud().generate(text_to_cloud2)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

#wordcloud is picking up on an HTML tag that is contained in some of our words!
#we should remove this as well


#---named entity recognition (NER) is a more advanced NLP task. fortunately, spacy automatical does it!


#we can also get labels for each entity


#-!Exercise: extract all of the entities mentioned in the comments and make a barplot of the most common entities
#Hint: you can use the same nested loop structure as before


#we will return to NER when we talk about networks!


#---sentiment analysis
#sentiment analysis tries to determine the positivity or negativity of a text
#Warning!  sentiment analysis is way overhyped.  It is entirely incapable of detecting sarcasm or irony and so it 
#does a bad job with most forms of conversational language.  Use at your own risk!

#we first need to add a new features to our NLP pipeline
#this will create new attributes for each document and word that give the sentiment of the text

#process all of the reviews using the nlp pipeline


#polarity goes from -1 (negative) to 1 (positive)

#subjectivity goes from 0 (objective) to 1 (subjective)

#we can also see which words contribute to the assessment of polarity and subjectivity

#let's look at the most negative texts
#are these sarcastic?


#how about the most positive texts
#these hardly seem "positive"


#sentiment analysis is not generally useful for individual texts, but can be used in aggregate to compare things
#let's make a boxplot comparing the polarity of comments on OpEds and Science articles
