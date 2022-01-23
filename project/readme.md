# DATA602 Final Project
This is your opportunity to utilize the concepts in the course in undertaking your own machine learning analysis. This will be worth 30% of your final grade. This should be oriented around a **classification problem - either binary or a multiclass problem**.

# Deliverables:
### (0) Project Proposal
- Notebook with the business question being answered.  
- Exploratory analysis (EDA) on the data to ensure the problem can be answered.  
- This will be worth 25% of your project grade.  
- This should contain:  
  - a README explaining the data set you've chosen, why you've chosen it, and the classification activity you plan on pursuing.  
  - a Jupyer Notebook that thoroughly performs EDA on your data set. Unnecessary features should be documented and removed, data with bad data types should be fixed, and any necessary if-else type transformations should be explored/implemented. **DO NOT** perform any missing value replacement or standardization on this data, however, note which features would require that type of additional processing.  
  - The end results of the EDA should be a very clean data set that would be ready for modeling activities.
### (1) A GitHub repository with your project, containing:
- README that contains an overview of your work. 
- Copy or link to your data. 
- Jupyter Notebook - containing:  
  - an abstract/introduction;   
  - exploratory data analysis (this will be done via your project proposal);  
  - data cleaning and feature engineering;  
  - modeling;  
  - results and discussion;  
  - conclusion/next steps;  
  - references. 
  - The notebook must be submitted with all cells executed in order and a PDF that memorializes the results will need to be submitted in addition to what is submitted on GitHub.  
### (2) Slide presentation that summarizes your motivation for choosing the dataset, the specific problem you are trying to solve, exploratory data analysis, and model results. You should include motivation towards the techniques chosen and areas for further exploration. Time permitting in the last week, everyone will have ~5 minutes to present their projects.
### (3) Youtube recording (< 5 minutes) overviewing the slides. You’ll submit the link.

# Checklist of things to include:
- Project motivation clearly explained. 
- Dataset is suitable and is within the below requirements. 
- Exploratory analysis clearly presented with professional/publication quality graphics. 
- Document how you are planning to handle missing values, outliers, ....
- Feature engineering steps clearly explained. 
- Selection of evaluation metric(s) for modeling with justification.  
- Proper splitting/partitioning of data to ensure results are robust. 
- Fitting of several models and exploration of different hyperparameters using a search technique.  
- ROC curves and/or precision-recall curves to visually show how the models performed.  
- Refined hyperparameter search on best performing model.   
- Discussion of machine learning models chosen for exploration. For those chosen, detail on why the final hyperparameters were chosen.  
- Visualizations on model results and clear explanation on the final model.  
- Recommendations on next steps, including potential ways to improve performance and additional data that could be useful.  
- Slides overview the project, results, and conclusions. Include necessary exhibits/text.  
- The video clip (of reasonable audio quality) that walks through the entirety of your analysis.  

# Data requirements:
- Should not be one of the common machine learning datasets used in-class, in textbooks, online tutorials, or included within packages (i.e., MNIST, Titantic, Iris, ....).   
- Datasets should not be proprietary or internal to your company.  
- Use a dataset of at least moderate size (> 5,000 rows and 10 features). Ideally, the dataset should have a mix of numerical and categorical features, but that is not mandatory.   

# Deadlines:  
- Project proposal: TBD. 
- Overall project due date: TBD.  

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

# Expectations:
- Organized repository, with folders for data, diagrams (if any), and a readme file.  
- README should be in a markdown format and summarize your project (think an abstract).  
- Notebook should be error free, include sections, and narratives to explain your thought process and summarize your observations.  
- Notebook should have every code cell executed sequentially (i.e., restart your kernel and run all).  
- PowerPoint should be clean, well organized, and summarize your project. There should be no grammatical mistakes, misspellings, ECT, ...  You should be comfortable presenting this to the president of your company.  
- Video clip should walk through your PowerPoint. Verbally should go through the slide deck without reading verbatim.  

# Questions I've received in the past:
#### What if my column is mostly missing values?
- Read the data documentation to determine if there is a reason for the missing values and handle accordingly
If no documentation exists, you'll need to use your own judgement, which could include:  
- Fill as "Unknown/Missing" using the fill_value in the simple imputer, then use One Hot Encoding (if categorical).  
- Fill as zero if the data represents some type of count, or use the median/mean/mode fill strategies (if numeric).  
- Not include the column for modeling (not every column needs to be included, if it isn't useful it isn't useful).  

#### What if my categorical variable has a lot of unique values?
- Identify the top N and replace the rest with "Other" and then use One Hot Encoding.  
- Use One Hot Encoding then pass through a variance threshold imputer to remove very rare values.  
- Don't worry and use methods that regularize the useless categories to zero/near-zero.  

#### What if my target variable has a lot of categories with small N?
- Consolidate the categories using an if-statement.  
- Drop the small categories and acknowledge rationale within the modeling process.  

