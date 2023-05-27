from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Using Vectorizer of sklearn to get vector representation
text1='Eiffel tower is a tourist attraction in france'
text2='The tower of London is a tourist place in London'
documents=[text1,text2]

vectorizer=CountVectorizer()
matrix=vectorizer.fit_transform(documents)

# Obtaining the document-word matrix
doc_term_matrix=matrix.todense()


print(cosine_similarity(doc_term_matrix[0],doc_term_matrix[1]))


