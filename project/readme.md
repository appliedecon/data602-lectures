# DATA602 Final Project
This is your opportunity to utilize the concepts in the course in undertaking your own machine learning analysis. This will be worth 30% of your final grade.

# Deliverables:
### (1) A GitHub repository with your project, containing:
- README that contains an overview of your work. 
- Copy or link to your data. 
- Jupyter Notebook - containing:  
  - an abstract/introduction;   
  - exploratory data analysis);  
  - data cleaning and feature engineering;  
  - modeling;  
  - results and discussion;  
  - conclusion/next steps;  
  - references. 
  - The notebook must be submitted with all cells executed in order and a PDF that memorializes the results will need to be submitted in addition to what is submitted on GitHub.  
### (2) Slide presentation that summarizes your motivation for choosing the dataset, the specific problem you are trying to solve, exploratory data analysis, and model results. You should include motivation towards the techniques chosen and areas for further exploration. Time permitting in the last week, everyone will have ~5 minutes to present their projects.
### (3) Youtube recording (< 5 minutes) overviewing the slides. You’ll submit the link.

# Grading Guidelines:
- ( 5%) Project motivation clearly explained. 
- ( 5%) Dataset is suitable and is within the below requirements. 
- (15%) Exploratory analysis clearly presented with professional/publication quality graphics. 
- (15%) Feature engineering steps clearly explained. 
- (10%) Proper splitting/partitioning of data to ensure results are robust. 
- (20%) Fitting of several models and exploration of different hyperparameters. 
- (10%) Discussion of machine learning models chosen for exploration. For those chosen, detail on why the final hyperparameters were chosen.  
- (10%) Visualizations on model results and clear explanation on the final model.  
- ( 5%) Slides overview the project, results, and conclusions. Include necessary exhibits/text.  
- ( 5%)The video clip (of reasonable audio quality) that walks through the entirety of your analysis.  
- Additional consideration will be given to participation during the in-class presentations for volunteering to present your project and for participating in discussions.  

# Data requirements:
- Should not be one of the common machine learning datasets used in examples and textbooks (no titanic, MNIST, iris, Boston house prices, textbook datasets, including any of the machine learning data repositories, e.g., UCI). Look for open data sets where their first purpose isn't machine learning.  
- Use a dataset of at least moderate size (> 5,000 rows and 10 features). Ideally, the dataset should have a mix of numerical and categorical features, but that is not mandatory. Datasets from Kaggle, Data.World, or other machine learning-specific repositories are not allowed for the project.  
- The dataset should not be proprietary or internal to your company. Look for open data sets.  
- This should be a **CLASSIFICATION** problem, either binary or multi-class.  
- Data sets used in class demonstrations are not allowed, this includes the IMDb dataset and MNIST. Data sets included with libraries (e.g., scikit-learn, pandas, keras, ...) are also not allowed.

#### I would highly recommend doing a cursory EDA on candidate datasets to make sure they fit the requirements.

# Deadlines:
- [Use this Google Form to submit the dataset you are using by 11/15/2021](https://docs.google.com/forms/d/e/1FAIpQLScAG7BMCHkF34TVkEs5Mdx0VMO3makWxoYRCin1NluxkI0NCQ/viewform?usp=sf_link).  
- In the form, I added a link for where you imported the data and proved that it was useful for modeling.  
- Links to GitHub repository, slides (pdf), and YouTube video must be submitted via Blackboard by December 13th, 2021 at 11:59PM.  
- This [Google Sheet](https://docs.google.com/spreadsheets/d/1xaUkc5SB9Jozq_gxNoAEFUi8m9WVUzqQt_enws5pdFA/edit?usp=sharing) lists all of the datasets that have been "approved". Once a student gets their dataset approved, no one else may choose that dataset.

# Example project descriptions:  
- Sentiment analysis of review data to predict user reviews, whether an individual purchased a product, ...  
- Image classification, e.g., predicted whether a picture is a dog, cat, fish, ...  
- Predict employee attrition.  
- Predict whether the stock market increases or not.  
- Predict type of recipe given ingredient lists.  
- Predict whether transactions are fraud or not.  
- Predict whether someone falls based on gyroscopic measurements.  
- Predict the authenticity of autographs based on images.  
- Generate new data based on a system of machine learning products.  
- Predict whether someone buys products based on recommendation engines.  

# Things to include:
- Thorough EDA with visualizations.  
- Document how you are planning to handle missing values, outliers, ....
- Selection of evaluation metric(s) for modeling with justification.  
- Understanding of minimum performance levels classifiers should have to be useable.  
- Proper partitioning of training and test datasets and explanation of why you are setting up the experiment that way.    
- Broad grid search on multiple models.  
- Refined grid search on models that showed most promise.  
- In addition to printing top-level (e.g., accuracy, recall, ...) provide ROC curves and/or precision-recall curves to better differentiate between models.  
- If runtime is a considering factor, save those and plot the different runtimes.  
- Additional feature engineering/reduction if warranted and repeat of modeling processes.  
- Summarization of results.  
- Recommendations on next steps, including potential ways to improve performance and additional data that would be valuable.  

**IF YOUR MODELS HAVE AN ACCURACY OF 100%, PLEASE MAKE SURE YOU DIDN'T LEAK DATA ABOUT YOUR TARGET!**

# Expectations:
- Organized repository, with folders for data, diagrams (if any), and a readme file.  
- README should be in a markdown format and summarize your project (think an abstract).  
- Notebook should be error free, include sections, and narratives to explain your thought process and summarize your observations.  
- Notebook should have every code cell executed sequentially (i.e., restart your kernel and run all).  
- PowerPoint should be clean, well organized, and summarize your project. There should be no grammatical mistakes, misspellings, ECT, ...  You should be comfortable presenting this to the president of your company.  
- Video clip should walk through your PowerPoint. Verbally should go through the slide deck without reading verbatim.  
