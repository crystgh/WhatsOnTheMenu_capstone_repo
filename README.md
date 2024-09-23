## Recipe Recommendation System: What's On The Menu? 🍽️👩‍🍳


### Executive Summary

**Problem:** Households often face the challenge of managing food resources efficiently. A significant amount of food is wasted due to over purchasing, improper storage, and the inability to use ingredients before they spoil. Also, individuals often struggle to plan meals that make the best use of what they already have, leading to unnecessary expenditure on groceries.

**Solution and Impact:** With data science it is possible to develop a recipe recommendation tool that provides relevant recipe options based on ingredients on hand which helps reduce expenses and food waste.

**Initial Takeaways from Dataset:** The dataset includes mostly text data. In this project I focused on a subset of recipes that include serving sizes. This sample includes 105,543 unique recipes with a total of 5,529 unique ingredients. The average number of ingredients per recipe from this subset is ~8. The top 10 frequent occurring words include: salt, pepper, onion, cheese, cream, sugar, butter, water, chicken, and oil, which are staples commonly found in the kitchen. 

### Demo

Please see below a preview of my streamlit app:
![Preview of my Streamlit App](streamlit_app_preview.png)


### Methodology

**Data processing steps**: The list of changes and actions performed in the original dataset to process the data include: cleaning up missing values and checking for duplicates, extracting the serving size and converting to the same unit of measure (e.g. dozens to single units), calculating a variable containing the number of ingredients in each recipe, and labeling each recipe by meal type (e.g. breakfast, lunch, dinner, drinks, dessert, and salads) using .loc method and supervised learning.

**Modelling directions**: The selected model is a content based recommendation model. The vectorizer of choice is Bag of Words (BoW) using CountVectorizer(). The ingredients list in the dataset was tokenized and the resulting sparse matrix was one hot encoded for further use. Additionally, the meal type variable that was engineered previously was encoded and sparsed. The two sparse matrices were then combined to calculate a cosine similarity based on the user inputs: **meal type** and **list of ingredients on hand**. The output of this model include a dataframe containing the top 5 recipes that most closely match the user inputs. The dataframe outputs the recipe name, ingredients list, serving size, instructions, measures and similarity of the top 5 recipes.

**Prototyping directions**: The prototyping direction of choice for showcasing this app is Streamlit, which allows users to interact with it in real time and providing inputs through dropdowns and text boxes. This is really useful for this project since the user input directly affects the recommendations output. 


### Organization

#### Repository 

* `data` 
    - Raw Data: This file contains the link to 'recipe_dataset.csv' which is needed to replicate the data loading, initial cleaning and EDA of the dataset. Please follow the shared link below to download the 'recipe_dataset.csv' file: https://drive.google.com/file/d/1DlGpPBCo_N-PkD8fi-nR-8jt51Q2zlMV/view?usp=drive_link

    - Final Preprocessed Data: This file contains the link to 'recipe_dataset_3.csv'. This is the final preprocessed data which is needed to replicate the modeling steps. Please follow the shared link below to download the 'recipe_dataset_3.csv' file: https://drive.google.com/file/d/1UiSlRW5jgBxF9VDmRLukwIoj9gLrSCLT/view?usp=drive_link 

* `model`
    - [models](https://github.com/crystgh/capstone_repo/tree/main/models): contains `joblib` dump of final model files
    - Baseline model: Content Based Recommendation System with the sparse matrix of unique ingredients, using recipe name as input.
    - Final model: Content Based Recommendation System with a combined sparsed matrix and taking two user inputs to calculate cosine similarities: meal type and list of ingredients on hand.


* `notebooks`
    - [notebooks](https://github.com/crystgh/capstone_repo/tree/main/notebooks): contains all final notebooks involved in the project

* `docs`
    - [docs](https://github.com/crystgh/capstone_repo/tree/main/docs): contains final report, presentations which summarize the project

* `references`
    - [references](https://github.com/crystgh/capstone_repo/tree/main/references): contains papers / tutorials used in the project

* `src`
    - [src](https://github.com/crystgh/capstone_repo/tree/main/src): contains application to demo my data science solution as a Streamlit app.

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `conda environment`
    - `capstone_env.yml` file included in the capstone files.

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Copyright (c) <2024> <crystalgilherrera>

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#### Dataset

Raw data: https://drive.google.com/file/d/1DlGpPBCo_N-PkD8fi-nR-8jt51Q2zlMV/view?usp=drive_link
Final preprocessed data: https://drive.google.com/file/d/1UiSlRW5jgBxF9VDmRLukwIoj9gLrSCLT/view?usp=drive_link 
Final model files: https://drive.google.com/drive/folders/1NhLVdBMhsIQcWTyQBBoGxJNKNzdW5u-P?usp=sharing 

### Taste Tests and What is Next on the Menu?

Dealing with a dataset that was only text without any numerical variables was an interesting and new experience for me. This was both challenging and rewarding. Using this dataset pushed me to be extra creative in terms of how to preprocess the data for EDA and modeling.

In the future, I would like to try additional modeling techniques for text processing such as embeddings and Word2Vec, and compare the recommendations against the current model. I would also like to add an output list of ingredients missing between the user's input and the recipe's ingredients that can serve as a grocery list if the user is missing some of these ingredients in their kitchen. Lastly, I would like to explore appending pictures to recipes which can help as a visual guide for users on what the final recipe output would look like.

### Credits & References

I would like to extend my gratitude to the following individuals and resources, whose support and guidance were vital in the successful completion of this project:

**BrainStation Educators**: Thank you for all of your support and encouragement throughout this journey! You were a key part in the successful completion of this project by laying out guiding steps that helped me overcome many of the challenges that this capstone posed.
**Family**: Thank you to my family for your unconditional support, and keeping me motivated and healthy throughout the duration of this project!
**RecipeNLG**: The substantial dataset posted on [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/recipenlg) served as the foundation of this project.
**Online Communities**: Platforms like Stack Overflow, GitHub and Youtube served as helpful communities where I was able to draw ideas from to try on my own project, which allowed me to tackle some of the complexities presented.

I am really grateful to all for your contribution and involvement in this project. 

*Take care and stay cooking!*
*Crystal* 👩‍🍳💻
