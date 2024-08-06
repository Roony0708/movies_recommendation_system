import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Function to fetch movie poster from TMDB API with retries
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=48d965535fc7d40ceb0ecd697596779c"
        response = session.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        poster_path = data.get('poster_path', None)
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_path
    except requests.exceptions.RequestException as e:
        st.warning(f"Error fetching poster for movie ID {movie_id}: {e}")
    return "https://via.placeholder.com/500x750?text=No+Image+Available"  # Fallback image

# Function to recommend movies based on similarity
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    count = 0
    for i in distances[1:]:
        if count >= 5:
            break
        movie_id = movies.iloc[i[0]].movie_id
        poster_path = fetch_poster(movie_id)
        if poster_path:
            recommended_movie_posters.append(poster_path)
            recommended_movie_names.append(movies.iloc[i[0]].title)
            count += 1
    return recommended_movie_names, recommended_movie_posters

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Set up retries for the session
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)
session.mount("http://", adapter)

# Set custom background and title
page_bg_img = '''
<style>
body {
background-color: #f5f5f5;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #6c63ff;'>Movie Recommender System</h1>", unsafe_allow_html=True)

# Movie selection dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Display recommendations when button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    if recommended_movie_names:
        st.markdown("<h3 style='text-align: center; color: #6c63ff;'>Recommended Movies</h3>", unsafe_allow_html=True)
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            if idx < len(recommended_movie_names):
                col.image(recommended_movie_posters[idx], use_column_width=True)
                col.markdown(f"<h5 style='text-align: center; color: #6c63ff;'>{recommended_movie_names[idx]}</h5>", unsafe_allow_html=True)

# Adding a nice animation (optional)
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Check if the request was successful
        return r.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading animation: {e}")
        return None

lottie_animation = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_x62chJ.json')
if lottie_animation:
    st_lottie(lottie_animation, height=200, key="coding")

# Footer
st.markdown("---")
st.markdown("<h4 style='text-align: center; color: #6c63ff;'>Made by - Abhishek Yadav</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #6c63ff;'>Contact: <a href='mailto:ydabhi1999@gmail.com'>ydabhi1999@gmail.com</a></h4>", unsafe_allow_html=True)
