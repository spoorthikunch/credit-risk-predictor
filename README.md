# 💳 Credit Risk Prediction

An end-to-end Machine Learning project that predicts whether a loan applicant is likely to default based on financial and demographic information.

This project covers the complete workflow from data preprocessing and model training to deployment setup.

---

## 📌 Problem Statement

Financial institutions must evaluate the risk of loan default before approving credit.

The objective of this project is to build a classification model that predicts credit risk using applicant features such as:

- Income
- Loan amount
- Employment status
- Credit history
- Age and other demographic attributes

---

## 🛠 Project Workflow

### Data Preprocessing
- Handling missing values
- Encoding categorical variables
- Feature scaling
- Feature engineering

### Models Implemented
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

### Model Evaluation
Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
  

---

## 🏆 Final Model

Three models were evaluated: Logistic Regression, Random Forest, and XGBoost.

Although Random Forest showed slightly higher overall accuracy, Logistic Regression and XGBoost achieved significantly higher recall for high-risk applicants (>0.90).

Since minimizing false negatives (missing defaulters) is critical in credit risk assessment, the final model was selected based on recall performance and ROC-AUC rather than accuracy alone.

---

## 📁 Repository Structure

- `Credit_Risk_Analysis.ipynb` – Complete modeling workflow  
- `app.py` – Deployment application  
- `credit_risk_model.pkl` – Trained model  
- `requirements.txt` – Project dependencies  
- `runtime.txt` – Python version configuration  

---

## ⚙️ Run Locally

```bash
git clone https://github.com/spoorthikunch/credit-risk-predictor.git
cd credit-risk-predictor

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
