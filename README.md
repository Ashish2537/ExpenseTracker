# Expense Tracker (Python + Streamlit)

A sleek and lightweight **Expense Tracker** built with **Python, Streamlit, and SQLite**.  
Easily log your expenses, categorize spending, and visualize insights — all in one simple app.

## Why This Project Matters  
-> Demonstrates **Python + Data Science + Web Dev** in one project  
-> Real-world use case: personal finance management  
-> Strong foundation for **portfolio**

## Tech Stack  
-> **Frontend/UI** → Streamlit (interactive web interface)  
-> **Backend** → Python  
-> **Database** → SQLite  
-> **Data Analysis** → Pandas  
-> **Visualization** → Matplotlib 


## Features  
-> Add, view, and categorize expenses  
-> Auto-generated spending charts & insights  
-> Category-wise analysis  
-> Lightweight & fast — runs locally in your browser 

## Future Enhancements
-> User authentication (multi-user support)
-> Export expenses to CSV/Excel
-> Advanced dashboards with Plotly
-> Deploy to Streamlit Cloud / Azure / Heroku

# Project Structure
ExpenseTracker/
│-- app.py              # Streamlit app
│-- expenses.db         # Local SQLite DB (ignored in GitHub)
│-- requirements.txt    # Dependencies
│-- .gitignore          # Ignore DB & cache
│-- README.md           # Documentation

# Open In Browser: http://192.168.1.4:8501

## Quick Start  

```bash
# Clone the repository
git clone https://github.com/yourusername/ExpenseTracker.git
cd ExpenseTracker

# Setup environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
