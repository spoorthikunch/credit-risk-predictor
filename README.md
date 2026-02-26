# 💳 Credit Risk Prediction

An end-to-end Machine Learning project that predicts the likelihood of loan default using financial and demographic applicant data.

The goal is to support risk-aware credit approval decisions by identifying high-risk applicants while minimizing false negatives.

---

## 📌 Problem Statement

Financial institutions must assess default risk before approving loans.

This project builds a binary classification model to predict whether an applicant is likely to default based on features such as:

- Income  
- Loan amount  
- Employment status  
- Credit history  
- Age and other demographic attributes  

The primary objective is to optimize recall for high-risk applicants, ensuring potential defaulters are not missed.

---

## 🛠 Project Workflow

### Data Preprocessing
- Missing value handling  
- Categorical variable encoding  
- Feature scaling  
- Structured feature engineering  

### Models Implemented
- Logistic Regression  
- Random Forest Classifier  
- XGBoost Classifier  

### Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-Score  
- ROC-AUC  

---

## 📊 Model Performance Summary

| Model              | Accuracy | ROC-AUC |
|-------------------|----------|---------|
| Logistic Regression | ~0.82 | ~0.89 |
| Random Forest       | ~0.83 | ~0.89 |
| XGBoost             | ~0.82 | ~0.89 |

While Random Forest achieved slightly higher accuracy, Logistic Regression and XGBoost demonstrated stronger recall for defaulters.

---

## 🏆 Final Model Selection

Model selection was based on business-critical metrics rather than accuracy alone.

Since minimizing false negatives (missing high-risk applicants) is crucial in credit risk assessment, the final model was chosen based on:

- Strong recall for defaulters  
- High ROC-AUC (~0.89)  
- Balanced precision-recall tradeoff  

This ensures risk-sensitive and reliable credit evaluation.

---

## 📁 Repository Structure

- `Credit_Risk_Analysis.ipynb` – End-to-end modeling workflow  
- `app.py` – Deployment application (Streamlit)  
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
