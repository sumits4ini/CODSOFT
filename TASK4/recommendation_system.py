import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = pd.read_csv(r"C:\Users\sumit\OneDrive\Documents\GitHub\CODSOFT\TASK4\movies.csv")


cv = CountVectorizer()
vectors = cv.fit_transform(movies["genre"])

similarity = cosine_similarity(vectors)

def recommend(movie_name):
    movie_name = movie_name.lower()

    movie_index = None

    for i in range(len(movies)):
        if movies.iloc[i]["title"].lower() == movie_name:
            movie_index = i
            break

    if movie_index is None:
        print("Movie not found!")
        return

    distances = list(enumerate(similarity[movie_index]))

    sorted_movies = sorted(
        distances,
        reverse=True,
        key=lambda x: x[1]
    )

    print(f"\nRecommended movies for '{movie_name.title()}':\n")

    count = 0
    for movie in sorted_movies:
        if count == 5:
            break

        index = movie[0]

        if index != movie_index:
            print(movies.iloc[index]["title"])
            count += 1


movie = input("Enter Movie Name: ")
recommend(movie)