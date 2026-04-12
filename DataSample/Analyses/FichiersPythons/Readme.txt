Grâce à ces 4 fichiers on peut obtenir l'historique des résultats et de la rentabilité du pari "Victoire de l'équipe" sur plusieurs matchs et plusieurs saisons.

Voici le résumé simplifié de l'utilsiation de ces fichiers :

Foot-data-scrapping.py :

Fichier python qui utilise la librairie Selenium pour détecter et telecharger les fichiers csv de chaque page pays (du site football-data.co.uk).
Ce fichier est utilisé tout seul il sert uniquement à webscrapper toutes les données sur le web pourp préaparer les futurs analyses.

InitAnalyse est le fichier central qui appel d'autres modules :

1) CompileDataParis va compiler dans un dataFramepropre et standardisé les données qui ont été webscrappées précedemment. Il prépare les données pour la vraie analyse. 

2) AnalyseDfParis a pour but de boucler sur tous les matches du df précedent pour analyser en profondeur le dataframe de CompileDataParis, il va notamment calculer la rentabilité de chaque équipe sur les X derniers matchs, sortir la liste des derniers résultats de l'équipe ... 

3) Le résultat de cette analyse pour toutes les équipes d'une équipe d'une saison est ensuite exporté et enregistré en CSV

Vers BDD :

Tous ces résultats d'analyses ont permis d'alimenter la BDD qui est apellée par le serveur HTTP.

