from src.scraper import scrape_tech_companies
from src.transform import transform
from src.load import load_to_sqlite
from datetime import datetime

def run_pipeline():
    start = datetime.now()
    print(f"\n{'='*50}")
    print(f"  Pipeline Scraping Tech — {start.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")

    try:
        df_raw   = scrape_tech_companies()
        df_clean = transform(df_raw)
        load_to_sqlite(df_clean)

        duree = (datetime.now() - start).seconds
        print(f"\n[OK] Pipeline terminé en {duree}s")

    except Exception as e:
        print(f"\n[ERREUR] {e}")
        raise

if __name__ == "__main__":
    run_pipeline()