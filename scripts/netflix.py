import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration des graphiques
plt.style.use('seaborn')
sns.set_palette("husl")

## 1. Chargement et premier aperçu des données
netflix = pd.read_csv('./netflix_titles.csv')

print("=== Premier aperçu des données ===")
print(netflix.head())
print("\n=== Informations sur le dataframe ===")
print(netflix.info())

## 2. Analyse des valeurs manquantes
print("\n=== Pourcentage de valeurs manquantes par colonne ===")
missing_data = netflix.isnull().mean() * 100
print(missing_data.sort_values(ascending=False))

## 3. Visualisations principales

# Configuration de la figure
plt.figure(figsize=(15, 12))

# Graphique 1: Répartition Films vs Séries TV
plt.subplot(2, 2, 1)
sns.countplot(x='type', data=netflix)
plt.title('Répartition Films vs Séries TV sur Netflix')

# Graphique 2: Top 10 des pays producteurs
plt.subplot(2, 2, 2)
top_countries = netflix['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 des pays producteurs de contenu')
plt.xlabel('Nombre de titres')

# Graphique 3: Contenus ajoutés par année de sortie
plt.subplot(2, 2, 3)
netflix.groupby('release_year')['show_id'].count().plot()
plt.title('Contenus ajoutés par année de sortie')
plt.xlabel('Année de sortie')
plt.ylabel('Nombre de titres')

# Graphique 4: Durée moyenne des films
plt.subplot(2, 2, 4)
movies = netflix[netflix['type'] == 'Movie'].copy()
movies['duration_min'] = movies['duration'].str.extract('(\d+)').astype(float)
movies.groupby('release_year')['duration_min'].mean().plot()
plt.title('Durée moyenne des films par année')
plt.ylabel('Minutes')

plt.tight_layout()
plt.show()

## 4. Analyse approfondie des films

# Statistiques descriptives sur la durée des films
print("\n=== Statistiques sur la durée des films ===")
print(movies['duration_min'].describe())

# Nouvelle figure pour l'analyse des films
plt.figure(figsize=(15, 6))

# Graphique 5: Distribution de la durée des films
plt.subplot(1, 2, 1)
sns.histplot(movies['duration_min'], bins=30, kde=True)
plt.title('Distribution de la durée des films')
plt.xlabel('Durée (minutes)')

# Graphique 6: Top 10 pays producteurs de films
plt.subplot(1, 2, 2)
top_movie_countries = movies['country'].value_counts().head(10)
sns.barplot(x=top_movie_countries.values, y=top_movie_countries.index)
plt.title('Top 10 pays producteurs de films')
plt.xlabel('Nombre de films')

plt.tight_layout()
plt.show()

## 5. Observations complémentaires

# Analyse par rating
print("\n=== Répartition par classification ===")
print(netflix['rating'].value_counts())

# Analyse des catégories
from collections import Counter
categories = netflix['listed_in'].str.split(', ').explode()
print("\n=== Top 10 des catégories ===")
print(Counter(categories).most_common(10))

# Visualisation des catégories
plt.figure(figsize=(12, 8))
top_categories = pd.Series(Counter(categories)).sort_values(ascending=False).head(10)
sns.barplot(x=top_categories.values, y=top_categories.index)
plt.title('Top 10 des catégories de contenu')
plt.xlabel('Nombre de titres')
plt.show()