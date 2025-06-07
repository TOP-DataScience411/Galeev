from pandas import read_csv
from scipy.sparse import csc_matrix, csr_matrix
from sklearn.neighbors import NearestNeighbors

from pathlib import Path
from sys import path


script_dir = Path(path[0])
movies = read_csv(script_dir / 'movies_ref.csv', index_col='movie_id')
genres = read_csv(script_dir / 'genres_ref.csv')
ratings = read_csv(script_dir / 'ratings_ref.csv')

# genres.drop(columns='Unnamed: 0', inplace=True)

movies_ratings = ratings.pivot_table(values='rating', index='user_id', columns='movie_id')


user_votes = ratings.groupby('user_id')['rating'].agg('count')
movies_votes = ratings.groupby('movie_id')['rating'].agg('count')

user_mask = user_votes.loc[user_votes > 50].index
movies_mask = movies_votes.loc[movies_votes > 10].index


movies_ratings = movies_ratings.loc[user_mask, movies_mask]
movies_ratings = movies_ratings.fillna(0)


movies_ratings_csc = csc_matrix(movies_ratings.values)


model = NearestNeighbors(
    n_neighbors=20,
    metric='cosine',
    algorithm='brute',
    n_jobs=-1,
)
model.fit(movies_ratings_csc.transpose())


recommendations = 7
movie_title = 'How to Train Your Dragon'

search_mask = movies['title'].str.contains(movie_title)
search_results = movies[search_mask]

try:
    movie_id = search_results.iloc[0].name

except IndexError:
    print(f'отсутствует фильм с названием {movie_title!r}')

else:
    movie_id_pos = movies_ratings.columns.get_loc(movie_id)
    movie_vector = movies_ratings_csc[:, movie_id_pos]
    
    closest_movies_dist, closest_movies_ind = model.kneighbors(
        movie_vector.transpose()
    )
    
    distances_indexes = sorted(zip(
        closest_movies_dist.flatten(),
        closest_movies_ind.flatten(),
    ))[1:]
    
    recommendations_ind = []
    for _, movie_id_pos in distances_indexes:
        movie_id_ = movies_ratings.columns[movie_id_pos]
        recommendations_ind.append(movie_id_)
    
    print(movies.loc[recommendations_ind])
    
recomm = movies.loc[recommendations_ind]

# Получаем жанры исходного фильма один раз
source_genres = set(genres[genres['movie_id'] == movie_id]['genre'])

# Создаем словарь {movie_id: set(genres)} для всех рекомендованных фильмов
recomm_movies_genres = genres[genres['movie_id'].isin(recomm.index)]
genre_sets = recomm_movies_genres.groupby('movie_id')['genre'].apply(set).to_dict()

# Фильтруем
recomm_i = [i for i in recomm.index 
           if len(genre_sets.get(i, set()) & source_genres) >= 2]
        
print(movies.loc[recomm_i])        