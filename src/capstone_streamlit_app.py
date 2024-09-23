### CODING AN APP IN STREAMLIT FOR MY CAPSTONE PROJECT: "WHAT'S ON THE MENU?"

### import libraries
import pandas as pd
import numpy as np
import streamlit as st
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
from scipy.sparse import hstack
import re
import ast

#st.write('Streamlit is an open-source app framework for Machine Learning and Data Science teams. For the docs, please click [here](https://docs.streamlit.io/en/stable/api.html). \
#    This is is just a very small window into its capabilities.')

#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file

#######################################################################################################################################
### Create a title
st.title("Welcome to What's On The Menu!")

### Display an image

st.image(r"C:\Users\cryst\Desktop\BrainStation - Data Science\Capstone\Capstone Files\streamlit app\pic_3.png")
# Press R in the app to refresh after changing the code and saving here

### Create a caption
st.caption("Delicious Recipes Await!")

#######################################################################################################################################
### DATA LOADING

### A. define function to load data
@st.cache_data
def load_data(path, num_rows):

    df = pd.read_csv(path, nrows = num_rows)

    return df

### B. Load data rows into a df variable
recipe_df_filtered = load_data("recipe_df_filtered_3.csv", 60808)

#######################################################################################################################################
### MODEL LOADING

loaded_vectorizer = joblib.load('ingredients_vectorizer.pkl')
loaded_encoder = joblib.load('meal_type_encoder.pkl')
combined_matrix = joblib.load('combined_matrix.pkl')

#######################################################################################################################################
### Tag options for user to interact with

### Meal Types
tag_options = ['breakfast', 'lunch', 'dinner', 'dessert', 'salad', 'drink']
meal_type_selected = st.selectbox('Please select a tag for a meal type that you are interested in.', tag_options)

### Ingredients

user_input = st.text_input('Please enter any ingredients you have on hand separated by a comma.',
                             help = 'Use lowercase and plural form when approrpriate')
user_input = user_input.strip()

### Search Button

search = st.button('Search for matching recipes')

if search:
    user_input = user_input.strip()
    user_ingredients_vector = loaded_vectorizer.transform([user_input])
    meal_type_vector = loaded_encoder.transform([[meal_type_selected]])

    user_vector = hstack([user_ingredients_vector, meal_type_vector])

    filtered_recipes = recipe_df_filtered[recipe_df_filtered['Meal_Type'] == meal_type_selected]

    filtered_matrix = combined_matrix[filtered_recipes.index]

    similarities = cosine_similarity(user_vector, filtered_matrix)

    sim_df = pd.DataFrame({
        'recipe': filtered_recipes['title'],
        'ingredients list': filtered_recipes['ingredient_list'],
        'serving size': filtered_recipes['serving_size'],
        'instructions': filtered_recipes['preparation_instructions'],
        'measures': filtered_recipes['ingredient_measures'],
        'similarity': np.array(similarities).squeeze()
    })

    top_similar_recipes = sim_df.sort_values(by='similarity', ascending=False).head(5)
    st.write(top_similar_recipes)
else:
    st.write("No recipes found for the selected meal type.")