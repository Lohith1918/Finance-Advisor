This project is based on the paper "Optimizing Personal Finance Management through AI-Driven Decision Support Systems". It integrates ML models, NLP (GPT-2), and a Streamlit interface to help users receive personalized financial recommendations.

## 📁 Project Structure
```
ai_finance_advisor/
├── data/                        # Dataset
│   └── personal_finance_dataset.csv
├── models/                     # Trained models (.pkl)
├── notebooks/                  # Jupyter analysis notebooks
├── outputs/                    # Generated plots
│   ├── savings_vs_income.png
│   └── expenditure_distribution.png
├── src/                        # Core logic
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model_train.py
│   ├── model_eval.py
│   ├── recommender.py
│   └── nlp_utils.py            # GPT-2 NLP tools
├── app.py                      # Streamlit app
├── requirements.txt
├── README.md
└── .gitignore
```

## ✅ Features
- Load and preprocess financial data
- Train ML models (Linear, XGBoost, AdaBoost...)
- Evaluate metrics (R², RMSE, MAE...)
- Generate recommendations
- GPT-2-based NLP summarizer and sentiment analyzer

## 🚀 Usage
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📚 Authors
Team Kanyarasi – KIIT University
