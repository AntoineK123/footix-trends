# ⚽ Footix

## 📌 Description

Projet pédagogique de développement web permettant de consulter :

- les résultats historiques des équipes de football  
- l’évolution de leur performance  
- la rentabilité théorique (ROI) si des paris avaient été effectués  

L’objectif est de démontrer la construction d’une application complète :  
**data → traitement → backend → frontend**

## 🔗 Lien : https://footix.onrender.com/
---

## 🚀 Fonctionnalités

- ⚽ Résultats historiques (Ligue 1, 2012 → 2025)  
- 📈 Calcul de rentabilité des paris par équipe  
- 🔍 Filtres (saison, équipe, compétition)  
- 📊 Analyse des derniers matchs (3, 5, 10…)  

---

## 📊 Chiffres clés

- 11 saisons  
- 4000+ matchs  
- 20+ équipes  
- 3 métriques principales  

---

## 🧠 Méthodologie

### 🧾 Source de données
Les données proviennent de :  
https://www.football-data.co.uk/

### 🗃️ Collecte des données
- Web scraping automatisé avec Python (Selenium)  
- Données récupérées au format CSV  
- Nettoyage et normalisation  

### 🧠 Analyse
- Traitement en Python  
- Calcul des indicateurs :
  - résultats  
  - séries de matchs  
  - ROI (retour sur investissement)  

### 💾 Base de données
- SQLite  
- Stockage des matchs et métriques  

---

## 🏗️ Architecture technique

### Backend
- JavaScript (Node.js)  
- Framework : NestJS  
- Serveur HTTP : Fastify  

Architecture :
- Controllers  
- Services  
- DTO (validation avec Zod)  

Le backend expose des endpoints permettant de récupérer :
- les matchs  
- les statistiques par équipe  
- les indicateurs de rentabilité  

### Frontend
- React  
- UI : Shadcn  
- Table : TanStack Table  
- Data fetching : TanStack Query  

---

## 🔄 Exemple de logique métier

**ROI = gains cumulés - mises cumulées**

Calcul basé sur :
- les cotes historiques  
- les résultats réels  

---

## ⚠️ Disclaimer

Ce projet est pédagogique uniquement.  
Il ne constitue pas un conseil en paris sportifs.

---

## 🛠️ Améliorations prévues

- Ajout d'autres championnats  
- Graphiques (évolution du ROI)  
- Pagination  
- Filtres avancés  
- Optimisation des performances backend  

---

## 🎯 Objectif du projet

Ce projet démontre :

- la manipulation de données réelles  
- la mise en place d’un backend structuré  
- la conception d’une logique métier (ROI)  
- l’intégration complète frontend/backend  