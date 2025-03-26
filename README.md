# 🧪 A/B Testing with Flask – CTA Text Optimization

This project is an end-to-end simulation of an A/B testing workflow using **Flask**, **Python**, and **Jupyter Notebook**. It demonstrates how to test variations of a landing page CTA (call-to-action) and make data-driven decisions based on user behavior.

---

## 🎯 Objective

To evaluate which of two CTA button texts leads to higher user conversions:

- **Version A:** "Sign Up Now"
- **Version B:** "Get Your Free Account"

Users were randomly assigned to one of the two variations. Their clicks were tracked and stored for analysis.

---

## 🛠️ Tech Stack

- **Web App:** Flask
- **Traffic Simulation:** Python (`simulate_users.py`)
- **Data Storage:** CSV (`data/user_logs.csv`)
- **Analysis:** Jupyter Notebook with Pandas, Matplotlib, Seaborn, SciPy

---

## 📊 Results Summary

| Group | Users           | Clicks | Conversion Rate |
| ----- | --------------- | ------ | --------------- |
| A     | _fill from CSV_ | _fill_ | ~30%            |
| B     | _fill from CSV_ | _fill_ | ~70%            |

- **T-statistic:** `-42.0127`
- **P-value:** `0.0`

✅ **Conclusion:** The difference is statistically significant. **Group B** performs significantly better and should be used in production.

---

## 📂 Project Structure

```
AB_TEST_PROJECT/
├── analysis/
│   ├── ab_test_analysis.ipynb       # Data analysis notebook
│   ├── ab_test_summary.csv          # Group summary table
│   └── conversion_rate_chart.png    # Visual chart of results
├── data/
│   └── user_logs.csv                # Log of all user actions
├── static/                          # (Empty, but ready for styling)
├── templates/
│   ├── index_a.html                 # Version A landing page
│   └── index_b.html                 # Version B landing page
├── venv/                            # Python virtual environment
├── app.py                           # Main Flask web app
├── simulate_users.py                # Traffic simulation script
└── requirements.txt                 # Python dependencies
```

---

## 🚀 How to Run the Project

### 1. Clone the repo and navigate to the project folder

```bash
git clone <your-repo-url>
cd ab_test_project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

App will be available at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 5. In a new terminal, simulate traffic

```bash
python simulate_users.py
```

### 6. Analyze results

```bash
jupyter notebook analysis/ab_test_analysis.ipynb
```

---
