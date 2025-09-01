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


# Quick Start  

## Clone the repository
git clone https://github.com/Ashish2537/ExpenseTracker.git
cd ExpenseTracker

## Setup environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

## Install dependencies
pip install -r requirements.txt

## Run the app locally
streamlit run app.py

## Open in browser
http://192.168.1.4:8501


## Project Structure
-> app.py → Streamlit app entry point
<br>
-> expenses.db → Local SQLite DB (ignored in Git)
<br>
-> requirements.txt → Python dependencies
<br>
-> .gitignore → Ignore DB & cache files
<br>
-> README.md → Documentation

## Future Enhancements
-> User authentication (multi-user support)
<br>
-> Export expenses to CSV/Excel
<br>
-> Advanced dashboards with Plotly
<br>
-> Deploy to Streamlit Cloud / Azure / Heroku
