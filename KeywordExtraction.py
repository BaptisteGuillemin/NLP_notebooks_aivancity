from nltk import tokenize
from operator import itemgetter
import math
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 



doc = """Big data integration is the problem of combining voluminous data stored in many database systems. It provides a unified view of data through a common representation called the global schema. 
	Defining the global schema is one of the main tasks in the design of a data integration system. It is one of the oldest research topics in the relational databases field. However, few solutions are proposed in the context of NoSQL systems.
	In this paper, we propose a new approach to automatically define the global schema of a data integration system composed of several NoSQL databases.  The proposed approach is divided into three phases which are schema extraction where we define the local schemas using a unified representation, schema matching in which we propose a hybrid approach to specify attributes correspondences between  the local schemas, and schema integration where we propose a methodology to define the global schema using the results of the schema matching.
	We evaluate the effectiveness of our approach using a set of existing benchmarks and a use case. """

#Text Cleaning
#You should not remove '.' 


### Remove UpperCases & stop words & white spaces stop words
stop_words = set(stopwords.words('english'))

### 
doc = doc.lower()
for word in word_tokenize(doc):
  if word in stop_words:
    doc = doc.replace(' '+word+' ', ' ')



##Number of sentences
total_sentences = tokenize.sent_tokenize(doc)
total_sent_len = len(total_sentences)


##Number of words
total_words = word_tokenize(doc)
total_words_len = len(total_words)




## the frequency of each word in the text
tf_score = {}
for each_word in total_words:
    if each_word in tf_score:
        tf_score[each_word] += 1
    else:
        tf_score[each_word] = 1

# Dividing by total_word_length for each dictionary element
tf_score.update((x, y/int(total_words_len)) for x, y in tf_score.items())
#print(tf_score)



##the number of sentences containing a word:

def NumOfSentwithWord(word, sentences):
  i=0
  for sentence in sentences:
    if word in sentence:
      i = i+1
  return i



idf_score = {}
for each_word in total_words:

    if each_word in idf_score:
        idf_score[each_word] = NumOfSentwithWord(each_word, total_sentences)
    else:
        idf_score[each_word] = 1

# Performing a log and divide
idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())
#print(idf_score)



tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
#print(tf_idf_score)



sorted_tf_idf_score = sorted(tf_idf_score.items(), key = itemgetter(1), reverse = True)
keywords = dict(sorted_tf_idf_score[:5])
print(keywords.keys())


