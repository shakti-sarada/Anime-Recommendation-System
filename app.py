import streamlit as st
import pickle
import requests
import time

# Default blank image URL
BLANK_IMAGE_URL = "https://via.placeholder.com/150x200.png?text=No+Image"

# Function to fetch an image URL using MyAnimeList API with caching and retries
@st.cache_data
def fetch_image_from_myanimelist_api(anime_name, client_id, retries=3):
    search_url = "https://api.myanimelist.net/v2/anime"
    headers = {"X-MAL-CLIENT-ID": client_id}
    params = {"q": anime_name, "limit": 1}

    for attempt in range(retries):
        try:
            response = requests.get(search_url, headers=headers, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            # Debug print to see the actual response
            print(f"Response data for {anime_name}: {data}")
            
            if 'data' in data and len(data['data']) > 0:
                if 'main_picture' in data['data'][0]['node']:
                    image_url = data['data'][0]['node']['main_picture']['medium']
                    return image_url
                else:
                    print(f"No 'main_picture' key in response for {anime_name}.")
                    return BLANK_IMAGE_URL
            else:
                print(f"No 'data' key in response or empty data list for {anime_name}.")
                return BLANK_IMAGE_URL
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2)  # Wait before retrying
            else:
                return BLANK_IMAGE_URL

# Lazy load the data with caching
@st.cache_resource
def load_data():
    animes = pickle.load(open('artifacts/anime_list.pkl', 'rb'))
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
    return animes, similarity

# Anime recommendation function
def recommend(anime):
    client_id = '686b1c464ef5faed358bb183beee39eb'
    animes, similarity = load_data()
    
    index = animes[animes['title'] == anime].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_anime_name = []
    recommended_anime_image = []
    
    for i in distances[1:21]:
        names = animes.iloc[i[0]].title
        recommended_anime_name.append(names)

        # Fetch the image for each recommended anime using MyAnimeList API
        image_url = fetch_image_from_myanimelist_api(names, client_id)
        recommended_anime_image.append(image_url)
        time.sleep(1)  # To prevent rate limiting

    return recommended_anime_image, recommended_anime_name

# Custom CSS for styling
st.markdown("""
    <style>
    /* Set the background image */
    .stApp {
        background-image: url('https://wallpapercave.com/wp/wp13661180.png'); /* Add your anime background image URL */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    
    /* Center the header and add custom styling */
    .stHeader h1 {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 3em;
        text-shadow: 2px 2px #000000;
    }

    /* Style the select box */
    .stSelectbox label {
        color: #FFFFFF;
        font-size: 1.2em;
    }
    .stSelectbox select {
        background-color: #333333;
        color: #FFFFFF;
        border-radius: 5px;
    }

    /* Style the button */
    .stButton button {
        background-color: #f55a42;
        color: white;
        font-size: 1.2em;
        padding: 0.5em 1em;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: white;
    }

    /* Style the image captions */
    .stImage div {
        color: #000000; /* Set caption text color to black */
        font-size: 1.1em;
        text-shadow: 1px 1px #FFFFFF; /* Optional shadow for better visibility */
    }

    </style>
""", unsafe_allow_html=True)

# Heading
st.header("Anime Recommendation System")

# Load anime names for the selectbox
animes, _ = load_data()
anime_list = animes['title'].values

# Creating a selectbox with a non-empty label
anime_name = st.selectbox(
    "Select an Anime",
    anime_list
)

# Creating a recommendation button
if st.button('Show Recommendations'):
    with st.spinner('Fetching recommendations...'):
        recommended_anime_image, recommended_anime_name = recommend(anime_name)

        image_width = 150
        image_height = 200

        for i in range(0, 20, 2):  # Loop in steps of 2 to create rows with 2 anime each
            cols = st.columns(2)  # 2 columns per row

            for j in range(2):
                with cols[j]:
                    st.image(
                        recommended_anime_image[i + j], 
                        width=image_width, 
                        caption=recommended_anime_name[i + j]
                    )

