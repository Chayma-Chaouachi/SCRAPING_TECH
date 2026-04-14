import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import json
from datetime import datetime

def scrape_tech_companies() -> pd.DataFrame:
    url = "https://companiesmarketcap.com/tech/largest-tech-companies-by-market-cap/"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    print("[SCRAPER] Téléchargement de la page...")
    response = requests.get(url, headers=headers, timeout=15)

    if response.status_code != 200:
        raise Exception(f"Erreur HTTP : {response.status_code}")

    print("[SCRAPER] Analyse du HTML...")
    soup = BeautifulSoup(response.text, "lxml")

    table = soup.find("table")
    if not table:
        raise Exception("Tableau non trouvé sur la page")

    rows = table.find_all("tr")[1:]

    companies = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 5:
            continue

        rank = cols[1].get_text(strip=True)

        # Extraire nom et ticker depuis les classes HTML spécifiques
        name_col = cols[2]
        name_tag   = name_col.find(class_="company-name")
        ticker_tag = name_col.find(class_="company-code")

        if name_tag and ticker_tag:
            name   = name_tag.get_text(strip=True)
            ticker = ticker_tag.get_text(strip=True)
        else:
            # Fallback : texte brut
            name   = name_col.get_text(strip=True)
            ticker = ""

        market_cap = cols[3].get_text(strip=True)
        price      = cols[4].get_text(strip=True)
        change     = cols[5].get_text(strip=True) if len(cols) > 5 else "N/A"
        country    = cols[6].get_text(strip=True) if len(cols) > 6 else "N/A"

        companies.append({
            "rank":       rank,
            "name":       name,
            "ticker":     ticker,
            "market_cap": market_cap,
            "price":      price,
            "change_24h": change,
            "country":    country,
        })

    df = pd.DataFrame(companies)

    os.makedirs("data/raw", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"data/raw/raw_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(companies, f, indent=2, ensure_ascii=False)

    print(f"[SCRAPER] {len(df)} entreprises extraites")
    print(f"[SCRAPER] Exemple : {companies[0]}")
    return df