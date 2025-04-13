# Nadia's Recommendation System (spec)
# Created a simple recommendation system that suggests movies (in given database)
# to users based on their movie genre preferences.

import pandas as pd
# content-based filtering with Scikit-Learn and using TFI-DF and cosine sim
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List

# movie dataset (recommends film based on given genre associated)
data = {
    'movie_id': list(range(1, 49)),
    'title': [
        'The Shining', 'Hereditary', 'The Notebook', 'Superbad', 
        'Interstellar', 'Coco', 'Inception', 'Knives Out',
        'Mad Max: Fury Road', 'The Godfather', 'Parasite', 'Toy Story',
        'Titanic', 'The Grand Budapest Hotel', 'The Dark Knight', 'Finding Nemo',
        'Spirited Away', 'The Matrix', 'Pulp Fiction', 'The Social Network',
        'La La Land', 'Deadpool', 'The Conjuring', 'The Silence of the Lambs',
        'Get Out', 'Amélie', 'Monsters, Inc.', 'Whiplash', 'The Lion King',
        'Shrek', 'Gravity', 'Eternal Sunshine of the Spotless Mind',
        'Pans Labyrinth', 'Arrival', 'The Big Sick', 'Jojo Rabbit',
        'Inside Out', 'A Quiet Place', 'The Farewell', 'Zootopia',
        'Memento', 'Logan', 'Black Panther', 'Moonlight',
        'The Shape of Water', 'The Babadook', 'Ford v Ferrari', 'Up'
    ],
    'genres': [
        'horror thriller', 'horror drama', 'romance drama', 'comedy',
        'sci-fi drama', 'animation', 'sci-fi thriller', 'comedy mystery',
        'action sci-fi', 'crime drama', 'thriller social', 'animation family',
        'romance disaster', 'comedy adventure', 'action crime', 'animation kids',
        'animation fantasy', 'sci-fi action', 'crime comedy', 'biography',
        'romance musical', 'action comedy', 'horror supernatural', 'thriller horror',
        'horror satire', 'romance fantasy', 'animation comedy', 'drama music',
        'animation musical', 'comedy fantasy', 'sci-fi space', 'romance sci-fi',
        'fantasy war', 'sci-fi mystery', 'romantic comedy', 'comedy war',
        'animation drama', 'horror sci-fi', 'drama family', 'animation buddy',
        'mystery thriller', 'superhero drama', 'superhero action', 'drama lgbtq',
        'romance fantasy', 'horror psychological', 'action biography', 'animation adventure'
    ]
}

df = pd.DataFrame(data)

# user genre preference
def user_pref() -> str:
    print("Enter your preferred genres (e.g. comedy, drama, etc.)\n")
    u_input = input("Genres: ")
    return u_input.lower()

# TF-IDF matrix for genre mapping / prioritisation
vec = TfidfVectorizer()
tfidf = vec.fit_transform(df['genres'])

# recommends top movies based on genre mapping
def rec_movies(u_genres: str, top_n: int = 3) -> pd.DataFrame:
    user_vec = vec.transform([u_genres])
    similar = cosine_similarity(user_vec, tfidf).flatten()
    top_ind = similar.argsort()[-top_n:][::-1]
    recs = df.iloc[top_ind].copy()
    recs['similarity'] = similar[top_ind]
    return recs[['title', 'genres', 'similarity']]

# runs main once for correct implementation
if __name__ == "__main__":
    u_genres = user_pref()
    recs = rec_movies(u_genres)
    print("\nRecommended Movies for You:\n")
    print(recs.to_string(index=False))
