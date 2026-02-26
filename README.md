# 💳 Credit Risk Prediction

An end-to-end Machine Learning project that predicts whether a loan applicant is likely to default using financial and demographic features.

This project demonstrates a complete modeling workflow — from preprocessing and feature engineering to model evaluation and selection.

---

## 📌 Problem Statement

Financial institutions must assess credit risk before approving loans. Incorrectly approving high-risk applicants can result in financial losses.

This project builds a binary classification model to identify high-risk borrowers while maintaining balanced and stable predictive performance.

---

## 🛠 Project Workflow

### 🔹 Data Preprocessing
- Handling missing values  
- Encoding categorical variables  
- Feature scaling  
- Multicollinearity analysis  
- Feature refinement  

### 🔹 Model Development
The following models were implemented and evaluated:

- Logistic Regression  
- Random Forest  
- XGBoost  

Models were compared using classification metrics and ROC analysis.

---

## ⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed using GridSearchCV to evaluate potential performance improvements.

The tuned configuration showed comparable performance to the base model, indicating that the dataset was well-structured and did not require additional complexity.

---

## 🏆 Final Model Selection

Logistic Regression was selected as the final model based on:

- Strong identification of high-risk applicants  
- Balanced classification performance  
- Interpretability and simplicity  
- Stable and consistent results  

Given the importance of minimizing false negatives in credit risk prediction, the selected model aligns well with business objectives.

---

## 📂 Repository Structure

- `Credit_Risk_Analysis.ipynb` — Complete modeling workflow  
- `logistic_model.pkl` — Final trained model  
- `app.py` — Deployment application  
- `requirements.txt` — Project dependencies  

---

## 🚀 Run Locally

```bash
git clone https://github.com/spoorthikunch/credit-risk-predictor.git
cd credit-risk-predictor

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
