import sqlite3
import pandas as pd

RULES = {
    "Food": ["swiggy", "zomato", "canteen", "tea", "snacks", "lunch"],
    "Transport": ["uber", "ola", "petrol", "bus", "train"],
    "Shopping": ["amazon", "flipkart", "myntra", "stationery"],
    "Bills": ["electricity", "wifi", "recharge"],
    "Entertainment": ["netflix", "movie", "spotify", "bowling"],
    "Health": ["pharmacy", "hospital", "gym"],
    "Rent": ["rent"],
}


def load_csv(path):
    df = pd.read_csv(path, parse_dates=["date"])
    df["category"] = df["category"].fillna("").astype(str).str.strip()
    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df


def categorize(desc):
    text = desc.lower()
    for cat, words in RULES.items():
        if any(w in text for w in words):
            return cat
    return "Others"


def fill_categories(df):
    df = df.copy()
    blank = df["category"] == ""
    df.loc[blank, "category"] = df.loc[blank, "description"].apply(categorize)
    return df, int(blank.sum())


def save_to_db(df, path):
    con = sqlite3.connect(path)
    out = df.copy()
    out["date"] = out["date"].dt.strftime("%Y-%m-%d")
    out.to_sql("transactions", con, if_exists="replace", index=False)
    con.close()


def run_query(path, sql):
    con = sqlite3.connect(path)
    res = pd.read_sql_query(sql, con)
    con.close()
    return res


def check_budget(df, budgets):
    spent = df.groupby(["month", "category"])["amount"].sum().reset_index()
    spent["budget"] = spent["category"].map(budgets)
    spent = spent.dropna(subset=["budget"])
    over = spent[spent["amount"] > spent["budget"]].copy()
    over["over_by"] = over["amount"] - over["budget"]
    return over.sort_values(["month", "category"]).reset_index(drop=True)


def iqr_flags(df):
    q1, q3 = df["amount"].quantile([0.25, 0.75])
    limit = q3 + 1.5 * (q3 - q1)
    return df[(df["amount"] > limit) & (df["category"] != "Rent")], limit
