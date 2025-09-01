import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Database Setup
# ------------------------------
conn = sqlite3.connect("expenses.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT
    )
""")
conn.commit()

# ------------------------------
# Streamlit App
# ------------------------------
st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("Expense Tracker (SQLite + Streamlit)")

# Add Expense Form
st.subheader("Add a New Expense")
with st.form("expense_form"):
    date = st.date_input("Date")
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    description = st.text_area("Description")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        cursor.execute(
            "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
            (str(date), category, amount, description)
        )
        conn.commit()
        st.success("✅ Expense Added Successfully!")

# Show All Expenses
st.subheader("All Expenses")
df = pd.read_sql("SELECT * FROM expenses", conn)
st.dataframe(df, use_container_width=True)

# Summary Section
st.subheader("Summary")

if not df.empty:
    # Total spent
    total = df["amount"].sum()
    st.metric("Total Spent", f"₹{total:,.2f}")

    # Category-wise breakdown
    st.write("### Category Breakdown")
    category_summary = df.groupby("category")["amount"].sum().reset_index()

    fig, ax = plt.subplots()
    ax.pie(category_summary["amount"], labels=category_summary["category"], autopct="%1.1f%%")
    ax.set_title("Expenses by Category")
    st.pyplot(fig)

    # Monthly breakdown
    df["date"] = pd.to_datetime(df["date"])
    monthly_summary = df.groupby(df["date"].dt.to_period("M"))["amount"].sum().reset_index()
    monthly_summary["date"] = monthly_summary["date"].astype(str)

    st.write("### Monthly Breakdown")
    st.bar_chart(monthly_summary.set_index("date"))
else:
    st.info("No expenses yet. Add one above")
