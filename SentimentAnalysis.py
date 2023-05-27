#Loading the Dataset
import pandas as pd
data = pd.read_csv('data.csv')


from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

#RegexpTokenizer splits a string into substrings using a regular expression.
token = RegexpTokenizer(r'[a-zA-Z0-9]+')

#CountVectorizer convert a collection of text documents to a vector of term counts.
# ngram_range = (1,1) means   taking only one word at a time.
# tokenizer = token.tokenize is the tokenizer method
# You can do the preprocessing separately, in this cas you are going to use : cv = CountVectorizer()
cv = CountVectorizer(stop_words='english', ngram_range = (1,1), tokenizer = token.tokenize)

#Learn the vocabulary dictionary and return document-term matrix.
text_counts = cv.fit_transform(data['Sentence'])


#Splitting the data into trainig and testing
X_train, X_test, Y_train, Y_test = train_test_split(text_counts, data['Sentiment'], test_size=0.30, random_state=20)

#Training the model using the multinomial Naive Bayes classifier
MNB = MultinomialNB()
###fit Learn a vocabulary dictionary of all tokens in the raw documents.
MNB.fit(X_train, Y_train)
##
##Caluclating the accuracy score of the model
predicted = MNB.predict(X_test)
accuracy_score = metrics.accuracy_score(predicted, Y_test)
print("Accuracuy Score of the model: ",accuracy_score)
##
###transform() ==> Transform documents to document-term matrix.
print(MNB.predict(cv.transform(["this restaurant is awesome!  good vibes"])))
