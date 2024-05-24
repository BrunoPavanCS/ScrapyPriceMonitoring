import pandas as pd
import sqlite3
from datetime import datetime

pd.options.display.max_columns = None

# Relative pathing to the src folder
json_path = "../data/data.jsonl"

# Reading data.json file
df = pd.read_json(json_path, lines=True)

# Useful columns
df["_source"] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
df["_collection_date"] = datetime.now()

# Type casting - to float
df["old_price_reais"] = df["old_price_reais"].fillna(0).astype(float)
df["old_price_centavos"] = df["old_price_centavos"].fillna(0).astype(float)
df["new_price_reais"] = df["new_price_reais"].fillna(0).astype(float)
df["new_price_centavos"] = df["new_price_centavos"].fillna(0).astype(float)
df["reviews_rating_number"] = df["reviews_rating_number"].fillna(0).astype(float)

# Removing parentheses from reviews_amount column
df["reviews_amount"] = df["reviews_amount"].str.replace(r"[\(\)]", "", regex=True)
df["reviews_amount"] = df["reviews_amount"].fillna(0).astype(int)

# Creating columns old_price and new_price
df["old_price"] = df["old_price_reais"] + df["old_price_centavos"] / 100
df["new_price"] = df["new_price_reais"] + df["new_price_centavos"] / 100

# Droping unecessary columns
df.drop(columns=["old_price_reais", "old_price_centavos", "new_price_reais", "new_price_centavos"], inplace=True)

# Connecting to database
conn = sqlite3.connect("../data/quotes.db")

# Converting to sql and saving data
df.to_sql("mercadolivre_items", conn, if_exists="replace", index=False)

# Closing connection
conn.close()

print(df.head())