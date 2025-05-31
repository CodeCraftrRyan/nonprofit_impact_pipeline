# 🏥 Nonprofit Impact Pipeline

This project is a complete end-to-end data pipeline that simulates how a nonprofit organization can use donor data to drive strategic decisions, segment supporters, and build custom dashboards.

🔗 **Dataset**: [Customer Personality Analysis - Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

---

## 🚀 Project Goals

- Load and clean CRM-style donor data
- Engineer features like donor age, income segments, and total spending
- Export cleaned data to Power BI or Tableau for reporting
- Showcase skills in data transformation, ETL logic, and strategic storytelling

---

## 🧰 Tech Stack

- Python (pandas)
- Tab-separated value (TSV) file
- Git & GitHub for version control
- Power BI / Tableau for final dashboards (optional)

---

## 📁 Project Structure

nonprofit_impact_pipeline/
├── data/
│   ├── raw/                  # Original Kaggle file (tab-separated)
│   └── processed/            # Cleaned data output
├── etl/
│   ├── extract.py            # Loads raw data
│   ├── transform.py          # Cleans and creates new features
│   └── load.py               # Saves cleaned data
├── README.md
├── requirements.txt
└── .gitignore


---

## 🧠 Feature Engineering

These new columns were added to the original dataset:

| Feature        | Description                             |
|----------------|-----------------------------------------|
| `age`          | Calculated from `year_birth`            |
| `income_segment` | Donor segmented into income quartiles |
| `total_spent`  | Combined total across 6 product types   |

---

## ✅ How to Run It

```bash
cd nonprofit_impact_pipeline
python etl/load.py
