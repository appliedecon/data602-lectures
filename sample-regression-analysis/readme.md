# Sample Regression Analysis
This repository contains an example of a regression analysis on the [California Housing Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing). This should be used as a guide as to expectations on format, best practices, and what should be included in your analyses.

# Dataset Description
The data being explored comes from [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing). It is a dataset containing attributes that relate to median home prices in California. Additional detail can be found [here](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset).

# Business Question/Problem Statement
Being able to understand drivers and predict home values can be used in policy and investment decisions. From a policy perspective, understanding what drives home prices can be used to normalize variances in home prices across areas and potentially create greater general affordability. From an investment perspective, being able to predict values could be used to identify under-valued properties that could be attractive investments.

# Exploratory Analysis Findings
We found that location is a significant driver of home prices in California. Higher home values are concentrated on the coastal areas and in denser population centers.

# Regression Results
We captured 60% of the variation in home values with a simple regression model. We found median income and distance to the coast were the two strongest drivers of median home values. We admit this dataset technically violates an assumption of linear models because geographic blocks are not purely independent from one another.

# Predictions Using this Dataset
We were able to predict median home values with a r-squared of 60% on a test dataset. We attempted regularization via Ridge, but found no benefit to adding regulariztion to our models.

# Potential Next Steps and Follow-ups
We could explore collecting additional data or engineering data using the geo-attributes of the dataset.
