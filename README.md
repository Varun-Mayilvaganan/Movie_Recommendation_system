# Movie_Recommendation_system
A movie recommendation system is a type of software that suggests movies to users based on their preferences, browsing history, and other factors. 
# Step1:- Using Libraries...
1.NumPy (import numpy as np): NumPy is a powerful library for numerical computing in Python. It provides support for large, multi-dimensional arrays and a wide range of mathematical functions. With NumPy, you can efficiently perform numerical operations on arrays, manipulate data, and implement mathematical algorithms.

2.Pandas (import pandas as pd): Pandas is a versatile library for data manipulation and analysis. It offers data structures like DataFrames, which are tabular data objects that allow for easy handling of structured data. Pandas provides a comprehensive set of functions for reading, writing, filtering, transforming, and aggregating data, making it a popular choice for data preprocessing and analysis tasks.

3.difflib (import difflib): The difflib module provides functionalities for comparing and finding differences between sequences, such as strings or lists. It offers methods like SequenceMatcher that compute similarities between sequences and can be used for tasks like string matching, finding common elements, or identifying changes between two versions of a document.

4.TfidfVectorizer (from sklearn.feature_extraction.text import TfidfVectorizer): TfidfVectorizer is a class from scikit-learn (sklearn) library. It is used to transform a collection of raw documents into a numerical matrix representing the TF-IDF (Term Frequency-Inverse Document Frequency) features. TF-IDF is a statistical measure often used in text mining and information retrieval to reflect the importance of a term in a document within a larger collection. TfidfVectorizer helps in preparing text data for machine learning algorithms that require numeric input.

5.cosine_similarity (from sklearn.metrics.pairwise import cosine_similarity): cosine_similarity is a function from the sklearn.metrics.pairwise module. It calculates the cosine similarity between pairs of samples or between sample vectors. Cosine similarity measures the similarity between two vectors by computing the cosine of the angle between them. It is commonly used in various applications, such as recommendation systems, document clustering, and information retrieval, to assess the similarity between textual or numerical data.

By importing these libraries and modules, you have access to a range of powerful tools for working with numerical computations, data manipulation, text analysis, and similarity measures.
# Step2:- 
Include the Datasets which you want to use to recommendation system.
# Step3:-
Print the combined features which is used to analyze the data and that's features makes the recommendation system more efficiently work on particular data.
# Step4:-
we are trying to use a vectorizer to convert a collection of textual descriptions into a numerical representation using the fit_transform method().
# Step5:-
Find the cosine Similarity between the featured vectors.
# Step6:-
Find the close match with all movies list and your value then it will return the exact match with similarity scores.
# Step7:-
Now we can see the 20 movies which recommended by the given input movie name.
<img src="https://github.com/Varun-Mayilvaganan/Movie_Recommendation_system/blob/main/Screenshot%20(140).png">
<img src="https://github.com/Varun-Mayilvaganan/Movie_Recommendation_system/blob/main/Screenshot%20(141).png">
