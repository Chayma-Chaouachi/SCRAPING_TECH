import pandas as pd
from datetime import datetime
import re

def clean_money(val: str) -> float:
    """Convertit '$4.425 T' ou '$456.78 B' en float"""
    if not val or val == "N/A":
        return None
    val = val.replace("$", "").replace(",", "").strip()
    try:
        if "T" in val:
            return float(val.replace("T", "").strip()) * 1_000_000_000_000
        elif "B" in val:
            return float(val.replace("B", "").strip()) * 1_000_000_000
        elif "M" in val:
            return float(val.replace("M", "").strip()) * 1_000_000
        else:
            return float(val)
    except:
        return None

def clean_change(val: str) -> float:
    """Convertit '+1.23%' ou '-0.45%' en float"""
    if not val or val == "N/A":
        return None
    val = val.replace("%", "").replace("+", "").strip()
    try:
        return round(float(val), 2)
    except:
        return None

def transform(df: pd.DataFrame) -> pd.DataFrame:
    print("[TRANSFORM] Nettoyage des données...")

    df["rank"]           = pd.to_numeric(df["rank"], errors="coerce")
    df["market_cap_usd"] = df["market_cap"].apply(clean_money)
    df["price_usd"]      = df["price"].apply(clean_money)
    df["change_24h_pct"] = df["change_24h"].apply(clean_change)

    df = df.drop(columns=["market_cap", "price", "change_24h"])
    df = df.dropna(subset=["market_cap_usd"])

    df["is_positive"]  = df["change_24h_pct"] > 0
    df["cap_category"] = df["market_cap_usd"].apply(
        lambda x: "Mega Cap"  if x >= 1e12
        else      "Large Cap" if x >= 1e11
        else      "Mid Cap"
    )
    df["date_scraping"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    df = df[[
        "rank", "name", "ticker", "country",
        "market_cap_usd", "price_usd", "change_24h_pct",
        "is_positive", "cap_category", "date_scraping"
    ]]

    print(f"[TRANSFORM] {len(df)} entreprises propres, {len(df.columns)} colonnes")
    return df