## Project Title: What's On The Menu?
=========================

### Executive Summary

... **Problem:** Households often face the challenge of managing food resources efficiently. A significant amount of food is wasted due to over purchasing, improper storage, and the inability to use ingredients before they spoil. Also, individuals often struggle to plan meals that make the best use of what they already have, leading to unnecessary expenditure on groceries.

... **Solution and Impact:** With data science it is possible to develop a recipe recommendation tool that provides relevant recipe options based on ingredients on hand which helps reduce expenses and food waste.

... **Initial Takeaways from Dataset:** Dataset includes mostly text data. Currently focusing on a subset of recipes from the dataset that include serving sizes. From this, there are 105,543 unique recipes with a total of 28,027 unique ingredients. The average number of ingredients per recipe from this subset is ~8. Top 10 frequent occurring words include: salt, pepper, onion, cheese, cream, sugar, butter, water, chicken, oil which are staples commonly found in the kitchen. 

### Demo

... Show your work:
...     Data visualizations
...     Interactive demo (e.g., `streamlit` app)
...     Short video of users trying out the solution


### Methodology

... High-level diagrams of entire process:
...     various data processing steps
...     various modelling directions
...     various prototyping directions


### Organization

#### Repository 

* `data` 
    - contains link to copy of the dataset (stored in a publicly accessible cloud storage)
    - saved copy of aggregated / processed data as long as those are not too large (> 10 MB)

* `model`
    - `joblib` dump of final model(s)

* `notebooks`
    - contains all final notebooks involved in the project

* `docs`
    - contains final report, presentations which summarize the project

* `references`
    - contains papers / tutorials used in the project

* `src`
    - Contains the project source code (refactored from the notebooks)

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `conda.yml`
    - Conda environment specification

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

#### Dataset

... Google Drive links to datasets and pickled models

### Credits & References

... Include any personal learning
