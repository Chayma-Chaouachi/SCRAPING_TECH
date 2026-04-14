import pandas as pd
from sqlalchemy import create_engine, text
import os

def load_to_sqlite(df: pd.DataFrame, table_name: str = "tech_companies"):
    os.makedirs("data", exist_ok=True)
    engine = create_engine("sqlite:///data/tech_warehouse.db")

    df.to_sql(table_name, engine, if_exists="append", index=False)

    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
        total = result.fetchone()[0]

    print(f"[LOAD] {len(df)} lignes ajoutées — total en base : {total}")
    print(f"[LOAD] Fichier : data/tech_warehouse.db")