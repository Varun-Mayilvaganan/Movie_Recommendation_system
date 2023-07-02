#import the necessary libraries for recommendation system

#USE GOOGLE COLAB =>for making execution easier. 


import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies_data=pd.read_csv("/content/Tamil_movies_dataset.csv")
print(movies_data.head(3))
movies_data.shape

#selecting unique features

selected_features=['Genre','Director','Actor','MovieName']
print(selected_features)

#if any values are null then it will be filled with gap

for feature in selected_features:
    movies_data[feature]=movies_data[feature].fillna('')

#combined features are listed....

combined_features = movies_data['Genre']+'          '+movies_data['Director']+'  '+movies_data['Actor']+'   '+movies_data['MovieName']
print(combined_features)

#combined features are vectorized for prediction

vectorizer=TfidfVectorizer()
feature_vectors=vectorizer.fit_transform(combined_features)
print(feature_vectors)

#Similarity function is used in feature vectors

similarity=cosine_similarity(feature_vectors)
print(similarity)

#enter your fav movie

movie_name=input("Enter your Favourite movie name:")

list_of_all_titles=movies_data['MovieName'].tolist()
print(list_of_all_titles)

#difflib for producing the close match for other values with your favourite movie

find_close_match=difflib.get_close_matches(movie_name,list_of_all_titles)
print(find_close_match)
close_match =find_close_match[0]
print(close_match)

index_of_movie=movies_data[movies_data.MovieName == close_match]['unique-id'].values[0]
print(index_of_movie)

similarity_score=list(enumerate(similarity[index_of_movie]))
print(similarity_score)
len(similarity_score)

sorted_similar_movies=sorted(similarity_score, key=lambda x:x[1], reverse=True)
print(sorted_similar_movies)
#selected similar features
print("Movie suggested for you : \n")
i=1
for movie in sorted_similar_movies:
    index=movie[0]
    title_from_index=movies_data[movies_data.index==index]['MovieName'].values[0]
    if(i<20):
        print(i,'.',title_from_index)
        i+=1
      #end of the code!
