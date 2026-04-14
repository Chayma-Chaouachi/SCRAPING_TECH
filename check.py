import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/tech_warehouse.db")
df = pd.read_sql("SELECT * FROM tech_companies ORDER BY rank", engine)

print(f"\nTop 10 entreprises tech par capitalisation :\n")
print(df[["rank", "name", "country", "market_cap_usd", "change_24h_pct", "cap_category"]].head(10).to_string())
print(f"\nTotal en base : {len(df)} lignes")