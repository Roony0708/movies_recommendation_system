# 🎬 Movie Recommender System

![Movie Recommender](https://via.placeholder.com/1000x300?text=Movie+Recommender+System)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Status](https://img.shields.io/badge/status-active-success.svg)]

## 📌 Overview
The **Movie Recommender System** suggests similar movies based on user preferences. It employs **content-based filtering** to analyze features like **genres, cast, crew, keywords, and overview**. The system also integrates with the **TMDB API** to fetch movie posters, ensuring a visually engaging experience.

## 🌟 Features
✅ **Content-Based Filtering** – Recommends movies based on similarity in genres, cast, crew, keywords, and plot.  
✅ **TMDB API Integration** – Dynamically fetches movie posters for an immersive experience.  
✅ **Interactive UI** – Built with **Streamlit** for a sleek and user-friendly interface.  
✅ **Retry Mechanism** – Handles API request failures gracefully.  
✅ **Lottie Animations** – Enhances UI with visually appealing animations.  

## 🔍 How It Works
### **1️⃣ Data Collection**
- The dataset consists of **5000+ movies from TMDB**.

### **2️⃣ Data Preprocessing**
- Merges **movie details and credits**.
- Extracts relevant features (**genres, cast, crew, keywords, overview**).
- Cleans and transforms data for analysis.

### **3️⃣ Feature Engineering**
- Uses **CountVectorizer** to convert text data into numerical vectors.
- Applies **Porter Stemmer** to normalize words.

### **4️⃣ Similarity Calculation**
- Computes **cosine similarity** between movies to find the most relevant recommendations.

### **5️⃣ Recommendation Process**
- Displays **top 5 similar movies** along with dynamically fetched posters.

## 🛠 Technologies Used
- 🐍 **Python** – Core programming language.
- 🎨 **Streamlit** – For the interactive web app.
- 📊 **Pandas & NumPy** – Data manipulation.
- 🤖 **Scikit-learn** – Vectorization & similarity calculation.
- 📝 **NLTK** – Text preprocessing (stemming).
- 🎬 **TMDB API** – Fetching movie posters.
- 💫 **Lottie** – For smooth animations.

## 🚀 Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 🎥 Usage
1. Select a **movie** from the dropdown menu.
2. Click **"Show Recommendation"**.
3. The system will display **5 recommended movies with their posters**.

## 🖼️ Screenshots
| Movie Recommender Interface | Recommendation Results |
|----------------------------|------------------------|
| ![UI](https://via.placeholder.com/400) | ![Results](https://via.placeholder.com/400) |

## 📂 Dataset Details
The dataset includes **tmdb_5000_movies.csv** and **tmdb_5000_credits.csv**, containing:
- 🎬 **Movie metadata** (budget, revenue, popularity, etc.).
- 🎭 **Genres, keywords, and production companies**.
- 🎞️ **Cast & crew details**.

## 📜 Project Files
```
📦 movie-recommender
 ┣ 📜 app.py  # Main Streamlit application file
 ┣ 📜 Movies_Recommender_system.ipynb  # Jupyter notebook for data preprocessing & training
 ┣ 📜 movie_dict.pkl  # Processed movie dataset
 ┣ 📜 similarity.pkl  # Precomputed similarity matrix
```

## 🔮 Future Improvements
✅ **User Authentication** – Allow users to save preferences.  
✅ **Hybrid Recommendations** – Combine content-based & collaborative filtering.  
✅ **Enhanced UI** – More interactive features for a better experience.  

## 👤 Author
**Abhishek Yadav**  
📩 Contact: [ydabhi1999@gmail.com](mailto:ydabhi1999@gmail.com)

---
🎬 *Enjoy personalized movie recommendations!* 🍿

