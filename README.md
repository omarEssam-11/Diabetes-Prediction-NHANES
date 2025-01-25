# Diabetes Prediction Project

## Overview
This project aims to predict diabetes using a dataset derived from the National Health and Nutrition Examination Survey (NHANES) spanning cycles from 2005 to 2020. The dataset has been carefully curated by integrating and merging data from multiple cycles, selecting the most relevant features that influence diabetes. This includes both measurable clinical factors such as fasting glucose levels and HbA1c, as well as lifestyle factors.

The project employs various machine learning algorithms, including K-Nearest Neighbors (KNN), Naive Bayes, and Support Vector Machines (SVM), to classify individuals as diabetic or non-diabetic. The dataset was preprocessed and scaled, followed by rigorous hyperparameter tuning and model evaluation.

## Key Features of the Project
- **Data Integration:** Combined NHANES datasets from multiple cycles (2005–2020) into a single, unified dataset.
- **Feature Selection:** Selected the most critical features impacting diabetes based on domain knowledge.
- **Data Preprocessing:** Applied scaling, encoding, and splitting techniques to prepare the data for modeling.
- **Machine Learning Models:** Implemented and evaluated multiple algorithms to identify the best-performing model.
- **Evaluation Metrics:** Used metrics like F1-score, precision, recall, and ROC-AUC to assess model performance.

## Dataset Features
Below is a list of the features used in the dataset along with their descriptions:

1. **Age**: Age of the individual in years.
2. **Gender**: Gender of the individual (‘Male’ or ‘Female’).
3. **Race**: Ethnic background of the individual (encoded categories for ethnicity).
4. **Fasting Glucose**: Fasting blood glucose level (mg/dL).
5. **Glycohemoglobin (%)**: Percentage of glycated hemoglobin (HbA1c) in blood.
6. **HDL-Cholesterol**: High-density lipoprotein (HDL) cholesterol level (mg/dL).
7. **BMX (Body Mass Index)**: Body mass index, calculated from weight and height (kg/m²).
8. **Systolic**: Systolic blood pressure (mmHg).
9. **Diastolic**: Diastolic blood pressure (mmHg).
10. **Family History**: Binary feature indicating a family history of diabetes.
11. **Total Sugars**: Total sugar intake from dietary sources (grams).
12. **Albumin-Creatinine Ratio (Alb/Cr)**: Albumin-to-creatinine ratio in urine, a marker of kidney function.


## Methodology
### Data Preprocessing
1. **Cleaning:** Removed duplicates and handled missing values.
2. **Scaling:** Standardized numerical features using `StandardScaler`.
3. **Encoding:** Applied one-hot encoding for categorical variables like race.
4. **Splitting:** Divided the data into training and testing sets (80:20 ratio).

### Machine Learning Models
- **K-Nearest Neighbors (KNN):** Tuned hyperparameters such as the number of neighbors, distance metric, and weights.
- **Naive Bayes:** Adjusted smoothing parameters to improve performance.
- **Support Vector Machines (SVM):** Optimized kernel types, regularization parameter (C), and gamma values.

### Model Evaluation
- Used cross-validation to ensure robust evaluation.
- Assessed models with metrics such as accuracy, F1-score, precision, recall, and ROC-AUC.
- Plotted confusion matrices and ROC curves for a visual understanding of model performance.

## Results
- Best-performing model: **SVM**
 - F1: **92**

- Precision score is: **90**
  
- Recall score is: **93**
  
- ROC-AUC: **95**


## Dependencies
- Python 3.8+
- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
