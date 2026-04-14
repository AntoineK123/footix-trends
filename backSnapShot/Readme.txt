Vous trouverez un "snapshot" du dossier "back" le backend du site. Il est simplement démonstratif, afin de montrer ce qu'il y a sous le capot.

Le backend est développé en JavaScript avec le framework NestJS, utilisant Fastify comme serveur HTTP.

Il n'y a pas de système d'authentifiacation pour accèder aux données.

Le dossier src est constituté ainsi pour traiter les requetes HTTP GET entrantes: routes > controllers > Dto (grâce à Zod) > services. 

3 routes principales existent dans le serveur HTTP : 

/matches => 
* renvoie les données concernant les matches passés sans aucune analyse contenu dans la table MatchData : Division, Date , Equipe Domicile, Equipe Exterieur,Score Equipe Domicile,Score Equipe Exterieur,Résultat final en anglais, les cotes Victoire Domicile/Matche Nul/Victoire Exterieur
* possibilité d'ajouter des query params ?season=... et &team=...

/stats => renvoie les résultats des analyses par équipe par saison par date (par match donc) contenu dans la table StatsData. Cette table contient notamment les données des Retour sur Investissement (ROI) en cas de paris les X matches précedents/le jour même, la cote de la victoire ce jour match -ci, la cote du pari inverse "Mon équipe ne gagne pas", et une chaine de caractere qui stocke les 5 résultats précedents ce match
* possibilité d'ajouter des query params ?season=... et &team=...

/filters => renvoie des données qui permettent d'alimenter les filtres Selects, en se basant sur la view DistincDivTeamSeason. Cette view est le résultat d'une requete qui cherche les Div et Season distinctes et crées un tableau JSON des équipes qui appartiennent à cette unicité Div-Season.