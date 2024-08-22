
# Reliability Prediction Project

## Overview

This project aims to predict reliability scores based on various factors. It involves data preprocessing, exploratory data analysis, feature engineering, model development, and deployment.

## Project Structure

- **Data:** Contains the raw and preprocessed data files.
- **Notebooks:** Includes Jupyter notebooks for each stage of the project.
- **Models:** Stores the trained predictive models.
- **Deployment:** Contains scripts or files related to model deployment.

## Steps

1. **Business Understanding:** Define the problem and objectives.
# # **Recommender System for Best Insurance Provider  in Kenya**
# ## **Business Understanding**
# According to Cytonn's report on Kenya's listed insurance sector for H1 2023, insurance penetration in Kenya remains historically low. As of FY 2022, penetration stood at just 2.3%, according to the Kenya National Bureau of Statistics (KNBS) 2023 Economic Survey. This is notably below the global average of 7.0%, as reported by the Swiss Re Institute. The low penetration rate is largely attributed to the perception of insurance as a luxury rather than a necessity, and it is often purchased only when required or mandated by regulation. Additionally, a pervasive mistrust of insurance providers has significantly contributed to the low uptake.
#
# Despite the critical importance of non-liability insurance—such as health, property, and personal accident coverage—for financial protection against unforeseen events, many individuals find it challenging to identify a trustworthy insurance provider due to opaque information on claim settlement records. This project seeks to address this pressing issue by simplifying the process of selecting a suitable insurance provider based on their performance in settling non-liability claims. By enhancing transparency and fostering trust in insurance providers, the project aims to boost insurance uptake and overall customer satisfaction.

2. **Problem Statement:** Clearly articulate the problem to be solved.
#
# ## **Problem Statement**
# Kenya faces a significant challenge with low insurance penetration, standing at just 2.3% as of FY 2022, well below the global average of 7.0%. This disparity is largely due to the perception of insurance as a luxury rather than a necessity, coupled with widespread mistrust towards insurance providers. Many Kenyans only purchase insurance when mandated or compelled by regulation, undermining the financial protection benefits offered by non-liability insurance such as health, property, and personal accident coverage.

3. **Objectives:** Outline the specific goals to be achieved.
### **Objectives**

Our project aims to address the challenges outlined in the business understanding and problem statement by developing a recommender system for the Kenyan insurance market. This system will leverage historical data to assess insurers based on their non-liability claim settlement performance. By offering transparent insights into insurer reliability and fostering trust between consumers and providers, we strive to achieve the following objectives:

1. **Enhanced Transparency:** Provide clear and detailed information on insurers' performance to improve market transparency and empower customers to make informed decisions.

2. **Increased Customer Trust:** Build greater trust between customers and insurance providers by showcasing insurers' reliability in settling non-liability claims.

3. **Boosted Insurance Uptake:** Encourage increased insurance adoption by simplifying the process of finding trustworthy insurers, thereby raising overall market penetration.

4. **Improved Customer Satisfaction:** Guide customers towards insurers with strong claim settlement records to enhance their overall satisfaction with the insurance experience.

4. **Metrics of Success:** Establish metrics to evaluate project success.
# ## **Metrics of Success**
#
# **Prediction Accuracy Metrics**
#
# 1. **RMSE (Root Mean Squared Error)**: For prediction of claim amounts or settlement amounts, RMSE measures the difference between predicted and actual values. Lower RMSE indicates better accuracy. It will serve as our target metric and any RMSE of 1-2% of the mean will be deemed acceptable with 1% being preferred.
#
# 2. **MAE (Mean Absolute Error)**: Similar to RMSE but less sensitive to outliers. It measures the average absolute difference between predicted and actual values. Not necessarily predetermined but anything < 0.5 will be considered good.
#
# 3. **R-squared (R²)**:  Indicates how well the model explains the variability of the target variable. Higher values indicate better performance. Any value above 0.85 will be considered as good.

5. **Data Understanding:** Explore and understand the dataset.
# ## **Data Understanding**
# Our approach will involve analyzing aggregated data from multiple sources, including historical claim settlement records, insurer performance metrics, and customer feedback. By normalizing and processing this data, we aim to develop a robust recommendation model that aligns with consumer needs and market dynamics.
#
# The dataset obtained from Insurance Regulatory Authority(IRA) website (https://www.ira.go.ke/index.php/publications/statistical-reports/claims-settlement-*statistics*) contains the following columns:
#
# * **Date**: End date of the quarter.
#
# * **Insurer**: Name of the insurance company.
#
# * **Claims_outstanding_at_the_beginning**: Claims outstanding at the beginning of the period.
#
# * **Claims_intimated**: The initial notification or reporting of a claim by a policyholder to their insurance company.
#
# * **Claims_revived**:  insurance claims that were previously closed, denied, or settled but have been reopened for reconsideration or additional processing.
#
# * **Total_Claims_Payable**: Total claims payable (summation of claims outstanding at the beginning, claims intimated, and claims revived).
#
# * **Claims_paid**: these are the claims paid by the insurers during the quarter. The claims paid may include those outstanding at the beginning of the period and those intimated and revived during the quarter.
#
# * **Claims_declined**: Claims declined during the period.
#
# * **Claims_closed_as_no_claims**: notified claims for which the insurer
# makes provisions for liability, but the liability does not crystalize during the quarter.
#
# * **Total_Claims_Action_during_the_Quarter**: summation of the number of
# claims paid, claims declined, claims closed as no claims, and claims
# outstanding at the end of the quarter.
#
# * **Claims_outstanding_at_the_end**: Claims outstanding at the end of the period. Calculated as the subtraction of total claims action during the quarter from the total claims payable during the quarter.
#
# * **Claims_declined_ratio_(%)**:  proportion of the number of claims declined in relation to the total
# number of claims actionable during the quarter
#
# * **Claims_closed_as_no_claims_ratio (%)**: proportion of claims closed as no claims in relation to the total number
# of claims actionable during the quarter.
#
# * **Claim_payment_ratio_(%)**: proportion of the number of claims paid in relation to the total number
# of claims actionable during the quarter.
#
# * **Claim_payment_ratio_(%)_prev**: Previous quarter claim payment ratio.

6. **Data Preprocessing:** Clean, transform, and prepare the data for analysis.

## Data Loading and Cleaning Summary

### 1. Data Loading:

- The dataset was successfully loaded into a pandas DataFrame.
- Initial inspection revealed the presence of both numerical and categorical features.

### 2. Data Cleaning:

- **Data Type Conversion:**
    - Numeric columns (starting from the third column) were converted to float.
    - The 'Date' column was converted to datetime format.
- **Handling Duplicates:**
    - No duplicate rows were found in the dataset.
- **Insurer Name Standardization:**
    - Variations in insurer names were identified and replaced with consistent naming conventions.
    - Entries related to the defunct 'Resolution Insurance Company' were removed.
- **Removal of Industry Totals:**
    - Rows representing industry totals were identified and removed.
    - Rows with dates in the year 1970 were also removed.
- **Outlier Handling:**
    - Numerical columns were analyzed for outliers using box plots.
    - Ratio columns ('Claims_declined_ratio_(%)', 'Claims_closed_as_no_claims_ratio (%)', 'Claim_payment_ratio_(%)') were capped at 100% to address unrealistic values.

### 3. Final Dataset:

- The cleaned dataset is now free of duplicates, inconsistencies in insurer names, industry totals, and unrealistic ratio values.
- The dataset has been saved as 'cleaned_data.csv'.

### Next Steps:

- Exploratory Data Analysis (EDA) can now be performed on the cleaned dataset to gain insights and inform further modeling decisions.


7. **Exploratory Data Analysis:** Gain insights from the data through visualizations and summary statistics.

## Exploratory Data Analysis Summary

### Data Overview

- The dataset contains information on insurance claims, including claims paid, claims declined, and claims closed as no claims, along with other relevant variables.
- The dataset spans a specific time period and includes data from multiple insurers.

### Key Findings

- **Top Insurers by Claims Paid:** Identified the insurers with the highest total claims paid and the highest claims payment ratio.
- **Trends Over Time:** Visualized changes in claims payment ratio, claims declined ratio, and claims closed as no claims ratio over time for different insurers.
- **Bivariate Analysis:**
    - Scatter plots revealed the relationship between claims payment ratio and claims declined ratio, as well as claims payment ratio and claims closed as no claims ratio.
    - Correlation analysis quantified the strength of relationships between numerical variables.
    - Pair plots and heatmaps provided visual representations of pairwise correlations.

### Insights and Recommendations

- **Claims Handling Performance:** The analysis provides insights into the claims handling performance of different insurers, which can be valuable for customers, insurers, and regulators.
- **Further Analysis:**
    - Investigate the underlying reasons for observed trends.
    - Compare metrics with industry benchmarks.
    - Develop predictive models to forecast future claims outcomes.

### Data Preprocessing and Feature Engineering (if applicable)

- **Handling Missing Values:** Describe any techniques used to address missing data (e.g., imputation).
- **Feature Scaling or Transformation:** Explain any transformations applied to numerical features (e.g., standardization, normalization).
- **Categorical Variable Encoding:** Outline how categorical variables were handled (e.g., one-hot encoding, label encoding).

### Next Steps

- **Model Selection:** Based on the EDA findings, select appropriate machine learning models for predicting claims outcomes.
- **Model Training and Evaluation:** Train and evaluate the selected models using appropriate metrics.
- **Model Deployment and Monitoring:** Deploy the best-performing model and establish a monitoring system to track its performance over time.


9. **Feature Engineering:** Create or modify features to improve model performance.

## Feature Engineering Summary

### Objectives

- Enhance the predictive power of the dataset by creating new features and transforming existing ones.
- Address potential issues like multicollinearity and missing values.

### Key Steps

- **Label Encoding:** Converted categorical variables ('Insurer', 'Reliability_Label') into numerical representations for compatibility with machine learning models.
- **Quarter and Year Extraction:** Extracted quarter and year information from the 'Date' column to capture potential temporal trends.
- **Reliability Score Creation:** Engineered a composite 'Reliability_Score' metric based on weighted combinations of claims payment, declined, and no-claims ratios. This score provides a comprehensive measure of insurer performance.
- **Reliability Score Visualization:** Explored the distribution of the 'Reliability_Score' using histograms and identified top-performing insurers using bar plots.
- **Multicollinearity Assessment:** Conducted Variance Inflation Factor (VIF) analysis to detect and address potential multicollinearity among numerical features.
- **Feature Selection:** Dropped features with high VIF values or limited relevance to the target variable.
- **Data Splitting:** Partitioned the dataset into training and testing sets to facilitate model evaluation.
- **Normalization and Scaling:** Standardized numerical features using StandardScaler to ensure consistent scaling across variables.
- **Missing Value Imputation:** Employed SimpleImputer to handle missing values by replacing them with the mean of the respective features.

### Outcomes

- The dataset is now enriched with engineered features that capture relevant information for predicting insurer reliability.
- Potential issues like multicollinearity and missing values have been addressed, improving the dataset's suitability for modeling.
- The normalized and imputed features are ready for use in training machine learning models.

### Next Steps

- Proceed with model selection, training, and evaluation using the preprocessed dataset.
- Consider further feature engineering techniques based on model performance and domain knowledge.


10. **Modelling:** Develop predictive models using various algorithms.

## Modelling

In this step, we aimed to develop a predictive model for reliability scores based on the preprocessed data. We experimented with various regression algorithms, including:

- **Linear Regression:** A simple linear model to establish a baseline.
- **Random Forest:** An ensemble method using multiple decision trees for improved accuracy and robustness.
- **Gradient Boosting:** Another ensemble technique that sequentially builds trees to minimize prediction errors.
- **XGBoost:** A highly optimized gradient boosting algorithm known for its efficiency and performance.
- **ElasticNet:** A linear model with regularization to prevent overfitting and improve generalization.
- **Stacking Regressor:** An ensemble method that combines predictions from multiple base models to potentially achieve even better performance.

We evaluated the models using metrics such as Root Mean Squared Error (RMSE), R-squared, and Mean Absolute Error (MAE). Additionally, we performed k-fold cross-validation to obtain a more reliable estimate of model performance on unseen data.

The results indicated that the **ElasticNet** model achieved the lowest RMSE and demonstrated strong performance in cross-validation, suggesting it as a suitable candidate for predicting reliability scores. However, further model refinement and feature engineering could be explored to potentially enhance the results.


11. **Recommendation:** Provide actionable recommendations based on the analysis.

## Recommendations

Based on our analysis and modeling, we recommend the following actions to improve reliability scores:

**Business Understanding:**
# # **Recommender System for Best Insurance Provider  in Kenya**
# ## **Business Understanding**
# According to Cytonn's report on Kenya's listed insurance sector for H1 2023, insurance penetration in Kenya remains historically low. As of FY 2022, penetration stood at just 2.3%, according to the Kenya National Bureau of Statistics (KNBS) 2023 Economic Survey. This is notably below the global average of 7.0%, as reported by the Swiss Re Institute. The low penetration rate is largely attributed to the perception of insurance as a luxury rather than a necessity, and it is often purchased only when required or mandated by regulation. Additionally, a pervasive mistrust of insurance providers has significantly contributed to the low uptake.
#
# Despite the critical importance of non-liability insurance—such as health, property, and personal accident coverage—for financial protection against unforeseen events, many individuals find it challenging to identify a trustworthy insurance provider due to opaque information on claim settlement records. This project seeks to address this pressing issue by simplifying the process of selecting a suitable insurance provider based on their performance in settling non-liability claims. By enhancing transparency and fostering trust in insurance providers, the project aims to boost insurance uptake and overall customer satisfaction.

**Problem Statement:**
#
# ## **Problem Statement**
# Kenya faces a significant challenge with low insurance penetration, standing at just 2.3% as of FY 2022, well below the global average of 7.0%. This disparity is largely due to the perception of insurance as a luxury rather than a necessity, coupled with widespread mistrust towards insurance providers. Many Kenyans only purchase insurance when mandated or compelled by regulation, undermining the financial protection benefits offered by non-liability insurance such as health, property, and personal accident coverage.

**Objectives:**
### **Objectives**

Our project aims to address the challenges outlined in the business understanding and problem statement by developing a recommender system for the Kenyan insurance market. This system will leverage historical data to assess insurers based on their non-liability claim settlement performance. By offering transparent insights into insurer reliability and fostering trust between consumers and providers, we strive to achieve the following objectives:

1. **Enhanced Transparency:** Provide clear and detailed information on insurers' performance to improve market transparency and empower customers to make informed decisions.

2. **Increased Customer Trust:** Build greater trust between customers and insurance providers by showcasing insurers' reliability in settling non-liability claims.

3. **Boosted Insurance Uptake:** Encourage increased insurance adoption by simplifying the process of finding trustworthy insurers, thereby raising overall market penetration.

4. **Improved Customer Satisfaction:** Guide customers towards insurers with strong claim settlement records to enhance their overall satisfaction with the insurance experience.

**Model Performance:**

## Model Comparison

| Model | RMSE | R-squared | MAE | Mean CV RMSE |
|---|---|---|---|---|
| Linear Regression | 1.70 | 0.99 | 0.28 | 0.37 |
| Random Forest | 1.40 | 1.00 | 0.51 | 0.97 |
| Gradient Boosting | 1.37 | 1.00 | 0.50 | 0.81 |
| XGBoost | 1.35 | 1.00 | 0.48 | 1.01 |
| ElasticNet | 1.23 | 1.00 | 0.28 | 0.57 |
| Stacking Regressor | 1.70 | 0.99 | 0.28 | 0.36 |

**Best Model (based on RMSE):** ELASTIC NET

### Interpretation

- **RMSE:** Measures the average prediction error in the same units as the target variable. Lower RMSE indicates better accuracy.
- **R-squared:** Represents the proportion of variance in the target variable explained by the model. Higher R-squared indicates better fit.
- **MAE:** Measures the average absolute difference between predicted and actual values. Lower MAE indicates better accuracy.
- **Mean CV RMSE:** Average RMSE from cross-validation, providing a more robust estimate of model performance on unseen data.

### Conclusion

Based on the results, the **ELASTIC NET** model demonstrates the best predictive performance for reliability scores, considering both RMSE and cross-validation results. However, further model refinement and feature engineering could potentially improve the results.


**Modeling Summary:**

## Modelling

In this step, we aimed to develop a predictive model for reliability scores based on the preprocessed data. We experimented with various regression algorithms, including:

- **Linear Regression:** A simple linear model to establish a baseline.
- **Random Forest:** An ensemble method using multiple decision trees for improved accuracy and robustness.
- **Gradient Boosting:** Another ensemble technique that sequentially builds trees to minimize prediction errors.
- **XGBoost:** A highly optimized gradient boosting algorithm known for its efficiency and performance.
- **ElasticNet:** A linear model with regularization to prevent overfitting and improve generalization.
- **Stacking Regressor:** An ensemble method that combines predictions from multiple base models to potentially achieve even better performance.

We evaluated the models using metrics such as Root Mean Squared Error (RMSE), R-squared, and Mean Absolute Error (MAE). Additionally, we performed k-fold cross-validation to obtain a more reliable estimate of model performance on unseen data.

The results indicated that the **ElasticNet** model achieved the lowest RMSE and demonstrated strong performance in cross-validation, suggesting it as a suitable candidate for predicting reliability scores. However, further model refinement and feature engineering could be explored to potentially enhance the results.


**Specific Recommendations:**

1. **Focus on Key Factors:** The ELASTIC NET model highlights the most influential factors affecting reliability. Prioritize actions to address these factors.

2. **Data-Driven Decision Making:** Leverage the predictive model to identify assets or processes with potentially low reliability scores and proactively implement preventive maintenance or improvements.

3. **Continuous Monitoring and Improvement:** Regularly collect and analyze reliability data, retrain the model periodically, and adapt strategies based on evolving trends and insights.

4. **Invest in Predictive Maintenance:** Implement predictive maintenance technologies and practices to optimize maintenance schedules, reduce downtime, and extend asset lifecycles.

5. **Foster a Culture of Reliability:** Promote a company-wide focus on reliability through training, communication, and incentivization programs.

By adopting these recommendations, the organization can enhance asset reliability, reduce operational costs, and improve overall performance.


12. **Deployment Summary:** Describe the deployment strategy and process.

## Deployment Summary

In this final step, we focused on deploying the chosen ELASTIC NET for practical use. The model was saved using joblib, enabling easy loading and utilization for predictions.

This deployment strategy allows for:

- **Efficient Predictions:** The saved model can be readily loaded to generate predictions on new data, either in real-time or batch mode.
- **Scalability:** The deployment can be scaled based on the volume of prediction requests, ensuring timely responses.
- **Integration:** The deployed model can be integrated into existing systems or applications, providing seamless access to reliability score predictions.

By successfully deploying the XGBoost model, we have empowered stakeholders to leverage the model's predictive capabilities for informed decision-making and proactive reliability management.


## Usage

1. **Install Dependencies:** Install the required libraries listed in the notebooks.
2. **Run Notebooks:** Execute the Jupyter notebooks in the specified order.
3. **Deploy Model:** Follow the deployment instructions to use the trained model for predictions.

## Contributing

Contributions to this project are welcome. Please follow the guidelines outlined in the CONTRIBUTING.md file.

## License

This project is licensed under the [License Name] license. See the LICENSE file for details.
