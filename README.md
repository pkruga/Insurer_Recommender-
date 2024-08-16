# Insurance Reliability Prediction

This project aims to predict the reliability of insurance companies based on various factors such as financial strength, customer satisfaction, and claims processing efficiency. We leverage machine learning techniques to build predictive models that can assist consumers in making informed decisions when choosing an insurance provider.

## Project Overview

The notebook explores different machine learning models, including:

- Linear Regression
- Random Forest
- Gradient Boosting
- XGBoost
- Stacking Regressor

We evaluate the models using metrics like RMSE, R-squared, MAE, and cross-validation scores to identify the best-performing model.

## Key Findings

- The XGBoost model demonstrates the best predictive performance for reliability scores based on RMSE and cross-validation results.
- Stacking multiple models can further enhance predictive accuracy.
- Further model refinement and feature engineering could potentially improve the results.

## Recommendations

- Collaborate with industry stakeholders like the Association of Kenya Insurers (AKI) and the Insurance Regulatory Authority (IRA) to obtain more comprehensive data.
- Participate in consumer protection trainings conducted by IRA to educate consumers about insurance reliability ratings.

## Next Steps

- Seek additional data on premiums paid to all insurers to calculate loss ratios and market shares, which can further improve model accuracy.
- Request a partnership with IRA for the full deployment of this tool to empower consumers in making informed decisions.

## Usage

1. Clone the repository: `git clone https://github.com/your-username/insurance-reliability-prediction.git`
2. Install the required libraries: `pip install -r requirements.txt`
3. Run the Jupyter notebook: `jupyter notebook insurance_reliability.ipynb`

## Contributing

Contributions are welcome! Please feel free to open issues or pull requests.

## License

This project is licensed under the MIT License.
