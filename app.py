import streamlit as st
import pickle as pk
import pandas as pd
import requests as rq

#st.title("The Movie Recommender")

st.markdown(
    """
    <style>
    .custom-title {
        font-size: 40px;
        color: #8f88b5;
        background-color:#03152d;
        text-align: center;
        padding: 3px; 
        border-radius: 35px;
        font-family: "Times New Roman";
    }
    </style>
    <h1 class="custom-title">Movie Recommendation System</h1>
    <br>
    <br>
    <br>
    """, 
    unsafe_allow_html=True
)

movies_dict=pk.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pk.load(open('similarity.pkl','rb'))
data=pd.read_pickle('df.pck')
def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image('https://i.imgur.com/H8G6IOn.jpeg')

def recommendation_function(movie):
    movie_index=movies[movies.title==movie].index[0] #index of given movie
    distances=similarity[movie_index]  #similarity score of given movie wrt each movies 
    movie_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    recommended_movies_posters=[]

    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters

def fetch_poster(movie_id):
    index=data[data.id==movie_id].index[0]

    return 'http://image.tmdb.org/t/p/w500/'+ data.iloc[index]['poster_path']
 
selected_movie=st.selectbox('Enter Your Fav Movie',movies['title'].values,placeholder="Choose from the list")

if st.button("Recommend"):
    
    names,posters=recommendation_function(selected_movie)
    
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])
        
    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])
        
