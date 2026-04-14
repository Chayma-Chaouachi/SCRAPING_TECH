# 📊 Tech Companies Scraping Pipeline

Ce projet est un pipeline ETL (Extract, Transform, Load) développé en Python permettant de collecter, nettoyer et stocker des données sur les plus grandes entreprises technologiques mondiales.

Il simule un cas réel de Data Engineering, en mettant en place un flux automatisé allant du scraping web jusqu'au stockage dans une base de données.

## 🎯 Objectif du projet

L'objectif est de construire un pipeline complet capable de :

- Extraire automatiquement des données depuis un site web
- Nettoyer et structurer les données avec Pandas
- Stocker les données dans une base SQLite
- Historiser les données brutes
- Organiser un projet selon les bonnes pratiques Data Engineering

## 🌐 Source des données

Les données sont extraites depuis :

👉 [https://companiesmarketcap.com/tech/largest-tech-companies-by-market-cap/](https://companiesmarketcap.com/tech/largest-tech-companies-by-market-cap/)

## 🏗️ Architecture du projet
scraping_tech_companies/
│
├── src/
│   ├── scraper.py      # Scraping web (Requests + BeautifulSoup)
│   ├── transform.py    # Nettoyage et transformation des données
│   └── load.py         # Chargement dans SQLite
│
├── data/
│   ├── raw/            # Données brutes JSON (historisées)
│   └── tech_warehouse.db
│
├── main.py             # Pipeline principal (orchestrateur)
├── check.py            # Vérification de la base de données
├── README.md
└── .gitignore

## 🔄 Pipeline ETL

### 1️⃣ Extract — Scraping

Le scraper récupère automatiquement :

- Rank (classement)
- Nom de l'entreprise
- Ticker boursier
- Market Cap
- Prix de l'action
- Variation sur 24h
- Pays

Les données brutes sont sauvegardées en JSON avec un timestamp.

### 2️⃣ Transform — Data Cleaning

Les données sont nettoyées et structurées :

- Suppression des valeurs manquantes
- Standardisation des colonnes
- Ajout de la date d'extraction
- Conversion en DataFrame (Pandas)

### 3️⃣ Load — Data Warehouse

Les données sont stockées dans une base SQLite : `data/tech_warehouse.db`

Chaque exécution du pipeline ajoute un nouveau snapshot de données.

## ▶️ Exécution du projet

### 1. Installer les dépendances

```bash
pip install requests beautifulsoup4 pandas sqlalchemy lxml
```

### 2. Lancer le pipeline

```bash
python main.py
```

### 3. Résultat attendu
✅ 100 entreprises extraites
✅ 100 entreprises nettoyées
✅ 100 lignes ajoutées en base
✅ Pipeline terminé

## 🧪 Vérifier la base de données

```bash
python check.py
```

## 💾 Technologies utilisées

| Outil | Usage |
|---|---|
| Python | Langage principal |
| Requests | Requêtes HTTP |
| BeautifulSoup | Parsing HTML |
| Pandas | Transformation des données |
| SQLite | Base de données |
| SQLAlchemy | ORM / connexion DB |
| Git | Versioning |