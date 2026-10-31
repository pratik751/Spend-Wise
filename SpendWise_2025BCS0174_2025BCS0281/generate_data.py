import random
import pandas as pd

random.seed(42)

items = {
    "Food": [("Swiggy order - biryani", 150, 400), ("Zomato - pizza", 200, 550), ("Canteen lunch", 40, 120),
             ("Tea and snacks", 20, 80), ("Swiggy Instamart groceries", 250, 700), ("Zomato - dosa", 90, 220)],
    "Transport": [("Uber to Kottayam town", 120, 350), ("Ola auto ride", 50, 160), ("Petrol for scooty", 200, 500),
                  ("KSRTC bus ticket", 30, 120), ("Train ticket to Kochi", 90, 300)],
    "Shopping": [("Amazon - earphones", 400, 1500), ("Flipkart - t-shirt", 300, 900), ("Amazon - notebook and pens", 100, 400),
                 ("Myntra - shoes", 800, 2200), ("Stationery shop", 30, 150)],
    "Bills": [("Mobile recharge Jio", 239, 299), ("Hostel wifi bill", 300, 500), ("Electricity share", 250, 600)],
    "Entertainment": [("Netflix subscription", 149, 149), ("Movie ticket PVR", 150, 350), ("Spotify premium", 59, 59),
                      ("Bowling with friends", 200, 500)],
    "Health": [("Pharmacy - medicines", 80, 400), ("Hospital consultation", 300, 800), ("Gym fees", 500, 500)],
    "Others": [("Laundry", 60, 200), ("Haircut", 100, 250), ("Gift for friend", 300, 900), ("Printout and xerox", 10, 60)],
}
weights = {"Food": 45, "Transport": 18, "Shopping": 10, "Bills": 6, "Entertainment": 8, "Health": 5, "Others": 8}

rows = []
months = pd.period_range("2026-01", "2026-06", freq="M")
for m in months:
    rows.append((f"{m}-02", "Room rent", "Rent", 6000))
    for _ in range(48):
        day = random.randint(1, m.days_in_month)
        cat = random.choices(list(weights), list(weights.values()))[0]
        desc, lo, hi = random.choice(items[cat])
        amt = random.randint(lo, hi)
        if random.random() < 0.03:
            amt *= 4
        rows.append((f"{m}-{day:02d}", desc, cat, amt))

df = pd.DataFrame(rows, columns=["date", "description", "category", "amount"])
df["category"] = [c if random.random() > 0.4 else "" for c in df["category"]]
df = df.sort_values("date").reset_index(drop=True)
df.to_csv("data/expenses.csv", index=False)
print(len(df), "rows saved")
