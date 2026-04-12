# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:19:36 2024

@author: asusa
"""

def analysedf(dfpar,resultat,equipe,saison):
    
    """
    A partir du df compiledata 
    renvoie le TRJ moyen des matches de l'équipe 
    et le ROI global de l'équipe 
    parametre dfpar pour la matrice des données compilées 
    resultat pour le resultat du paris sur lequel on mise
    equipe concernée (=la victoire par défaut) 
    saison si saison spécifique
    """
    import pandas as pd
    import numpy as np
    

    """
    On affecte ci dessus la cote du resultat visé , en fonction de si du choix de paris V N ou 1N par exemple de l'equipe en question'
    """
    
    #on ajoute une colonne vide pour les 5 derniers matchs
    dfpar['last5teamResults']="";
    
    #on definie par defaut la valeur Defaite
    dfpar['teamResult']="D";
    #on definie par defaut une perte
    dfpar['PNL']=-100.0
    dfpar['PNL'].astype(float)

    
    
    for k in range(len(dfpar)):
            
        
        ###ajout de la cote du resultat visé en fonction du choix du paris
            if resultat=="N":
                dfpar.at[k,'CoteResultat']=dfpar.at[k,'B365D']
                dfpar.at[k,'Coteinverse']=dfpar.at[k,'B365HA']
                
            elif resultat =="V":
                if dfpar.at[k,'HomeTeam']==equipe :
                    dfpar.at[k,'CoteResultat']=dfpar.at[k,'B365H']
                    dfpar.at[k,'Coteinverse']=dfpar.at[k,'B365DA']
                    
                else:
                    dfpar.at[k,'CoteResultat']=dfpar.at[k,'B365A']
                    dfpar.at[k,'Coteinverse']=dfpar.at[k,'B365HD']
                        
            elif resultat=="D":
                if dfpar.at[k,'HomeTeam']==equipe :
                    dfpar.at[k,'CoteResultat']=dfpar.at[k,'B365A']
                    dfpar.at[k,'Coteinverse']=dfpar.at[k,'B365HD']
            
                else:
                    dfpar.at[k,'CoteResultat']=dfpar.at[k,'B365H']
                    dfpar.at[k,'Coteinverse']=dfpar.at[k,'B365DA']
            elif resultat=="VN":
                if dfpar.at[k,'HomeTeam']==equipe :
                    dfpar.at[k,'CoteResultat']=dfpar.at[k,'B365HD']
                    dfpar.at[k,'Coteinverse']=dfpar.at[k,'B365A']
            
                else:
                    dfpar.at[k,'CoteResultat']=dfpar.at[k,'B365DA']
                    dfpar.at[k,'Coteinverse']=dfpar.at[k,'B365H']
                
            elif resultat=="DN":
                if dfpar.at[k,'HomeTeam']==equipe :
                    dfpar.at[k,'CoteResultat']=dfpar.at[k,'B365DA']
                    dfpar.at[k,'Coteinverse']=dfpar.at[k,'B365H']
                
                else:
                    dfpar.at[k,'CoteResultat']=dfpar.at[k,'B365HD']
                    dfpar.at[k,'Coteinverse']=dfpar.at[k,'B365A']
        
    
    
    """
    On definie par deafaut la perte dans la colonne PNL
    """

    
    """
    on calcule ci dessous les PNL de chaque matches
    """
        
    for k in range(len(dfpar)):
        # cas lequipe qui recoit est vainqueur 
        if dfpar.at[k,'FTR']=="H" : 
            
            if (resultat =="V" and dfpar.at[k,'HomeTeam']==equipe) or (resultat =="D" and dfpar.at[k,'AwayTeam']==equipe) :
               dfpar.at[k,'PNL']=(float(dfpar.at[k,'CoteResultat'])-1)*100
               dfpar.at[k,'teamResult']+="V"
        
            if (resultat =="VN" and dfpar.at[k,'HomeTeam']==equipe) or (resultat =="DN" and dfpar.at[k,'AwayTeam']==equipe) :
               dfpar.at[k,'PNL']=(float(dfpar.at[k,'CoteResultat'])-1)*100
               dfpar.at[k,'teamResult']+="V"
        
        if dfpar.at[k,'FTR']=="A" :
            if (resultat =="V" and dfpar.at[k,'AwayTeam']==equipe) or (resultat =="D" and dfpar.at[k,'HomeTeam']==equipe) :
               dfpar.at[k,'PNL']=(float(dfpar.at[k,'CoteResultat'])-1)*100
               dfpar.at[k,'teamResult']+="V"
            if (resultat =="VN" and dfpar.at[k,'AwayTeam']==equipe) or (resultat =="DN" and dfpar.at[k,'HomeTeam']==equipe) :
                dfpar.at[k,'PNL']=(float(dfpar.at[k,'CoteResultat'])-1)*100
                dfpar.at[k,'teamResult']+="V"
                
        if dfpar.at[k,'FTR']=="D" :
            dfpar.at[k,'teamResult']+="N"
            if resultat =="N" :
               dfpar.at[k,'PNL']=(float(dfpar.at[k,'CoteResultat'])-1)*100
            if resultat == "DN" or resultat =="VN" : 
               dfpar.at[k,'PNL']=(float(dfpar.at[k,'CoteResultat'])-1)*100 

    """
    On calcule ci dessous les la somme des PNL des 10 , 5 et 3 derniers matches avant celui ci 
    Pour cela on va crée une boucle qui va balayer tous les k de la table des matches de bas en haut cad du 1er match de la saison vers les plus recents
    Puis on va crée on cette de cette boucle dautres boucles qui vont balayer les matches précedents
    """
    
    """
    Cette premiere boucle sert a calculer le ROI des trois derniers matches et 5 dern matches et 10 dern matches
    """
    
    for k in range(len(dfpar)):
        
        somme2J=0
        somme3J=0
        somme5J=0
        somme10J=0
        sommeJJm1=0
        last5matchesResStr="";
        saison=""
        
        ROImoin1JJ=0
        ROImoin2J=0
        ROImoin3J=0
        ROImoin5J=0
        ROImoin10J=0
        CoteJ=dfpar.at[k,'CoteResultat']
        CoteInv=dfpar.at[k,'Coteinverse']
        
        #on cree les colonnes vides :
            
        for col in ['ROI-JJm1','ROI-2J','ROI-3J','ROI-5J','ROI-10J']:
            dfpar[col] = np.nan
        
        #on rajoute le ROI de JetJ-1 pour pouvoi
        if k >= 1 and dfpar.at[k-1,'Saison']==dfpar.at[k,'Saison']:
            
            sommeJJm1+=dfpar.at[k-1,'PNL']
            sommeJJm1+=dfpar.at[k,'PNL']
            dfpar.at[k,'ROI-JJm1']=sommeJJm1+0.0001
            dfpar.at[k,'ROI-JJm1']=dfpar.at[k,'ROI-JJm1']+200
            dfpar.at[k,'ROI-JJm1']=dfpar.at[k,'ROI-JJm1']/200
            ROImoin1JJ=dfpar.at[k,'ROI-JJm1']
        
            
        
        if k >= 2 and dfpar.at[k-2,'Saison']==dfpar.at[k,'Saison']:
            
            
            somme2J+=dfpar.at[k-1,'PNL']
            somme2J+=dfpar.at[k-2,'PNL']
            dfpar.at[k,'ROI-2J']=somme2J+0.0001
            dfpar.at[k,'ROI-2J']=dfpar.at[k,'ROI-2J']+200
            dfpar.at[k,'ROI-2J']=dfpar.at[k,'ROI-2J']/200
            ROImoin2J=dfpar.at[k,'ROI-2J']
        
        
        
        if k >= 3 and dfpar.at[k-3,'Saison']==dfpar.at[k,'Saison'] :
            somme3J+=dfpar.at[k-1,'PNL']
            somme3J+=dfpar.at[k-2,'PNL']
            somme3J+=dfpar.at[k-3,'PNL']
            dfpar.at[k,'ROI-3J']=somme3J+0.0001
            dfpar.at[k,'ROI-3J']=dfpar.at[k,'ROI-3J']+300
            dfpar.at[k,'ROI-3J']=dfpar.at[k,'ROI-3J']/300
            ROImoin3J=dfpar.at[k,'ROI-3J']
        
        if k>=5 and dfpar.at[k-5,'Saison']==dfpar.at[k,'Saison']:
            
            last5matchesResStr+=dfpar.at[k-5,'teamResult']
            last5matchesResStr+=dfpar.at[k-4,'teamResult']
            last5matchesResStr+=dfpar.at[k-3,'teamResult']
            last5matchesResStr+=dfpar.at[k-2,'teamResult']
            last5matchesResStr+=dfpar.at[k-1,'teamResult']
            dfpar.at[k,'last5teamResults']=last5matchesResStr
            
            somme5J+=dfpar.at[k-1,'PNL']
            somme5J+=dfpar.at[k-2,'PNL']
            somme5J+=dfpar.at[k-3,'PNL']
            somme5J+=dfpar.at[k-4,'PNL']
            somme5J+=dfpar.at[k-5,'PNL']
            dfpar.at[k,'ROI-5J']=somme5J+0.0001
            dfpar.at[k,'ROI-5J']=dfpar.at[k,'ROI-5J']+500
            dfpar.at[k,'ROI-5J']=dfpar.at[k,'ROI-5J']/500
            ROImoin5J=dfpar.at[k,'ROI-5J']
            
        if k>=10 and dfpar.at[k-10,'Saison']==dfpar.at[k,'Saison'] : 
            somme10J+=dfpar.at[k-1,'PNL']
            somme10J+=dfpar.at[k-2,'PNL']
            somme10J+=dfpar.at[k-3,'PNL']
            somme10J+=dfpar.at[k-4,'PNL']
            somme10J+=dfpar.at[k-5,'PNL']
            somme10J+=dfpar.at[k-6,'PNL']
            somme10J+=dfpar.at[k-7,'PNL']
            somme10J+=dfpar.at[k-8,'PNL']
            somme10J+=dfpar.at[k-9,'PNL']
            somme10J+=dfpar.at[k-10,'PNL']
            dfpar.at[k,'ROI-10J']=somme10J+0.0001
            dfpar.at[k,'ROI-10J']=dfpar.at[k,'ROI-10J']+1000
            dfpar.at[k,'ROI-10J']=dfpar.at[k,'ROI-10J']/1000
            ROImoin10J=dfpar.at[k,'ROI-10J']
        
        #on rajoute le ROI de JetJ-1 pour pouvoi
        
        
        ROIJ=(dfpar.at[k,'PNL']+100)/100
        saison=dfpar.at[k,'Saison']
    


     ### on calcul les ROI sans le match en question des 10 derniers matchs prec / 5 derniers matches prec / 3 derniers matches prec / 
     
     ### pour cela on va pour chaque ligne , balayer les lignes suivantes et sommer les PNL puis divisoer par un facteur 
        #on arrondie les ROI:
            
    dfpar['ROI-JJm1'] = dfpar['ROI-JJm1'].round(3)
    dfpar['ROI-2J'] = dfpar['ROI-2J'].round(3)
    dfpar['ROI-3J'] = dfpar['ROI-3J'].round(3)
    dfpar['ROI-5J'] = dfpar['ROI-5J'].round(3)
    dfpar['ROI-10J'] = dfpar['ROI-10J'].round(3)

  
    #on somme toutes les pnl par avoir le résultat de la profitabilité de paris sur l'équipe de marseille sur plusieurs saisons
    sommePNL=float(dfpar['PNL'].sum())
    #on calcul la somme total misé , = nbr de matchs * 100
    sommemise=int(len(dfpar)*100)
    #enfin le retour sur investissement global = pnlglobale/mise globale 
    ROI=float((sommemise+sommePNL)/sommemise)

    #on definie last 5 match results comme les 5 derniers resultats du dernier matchs du tableau
    last5matchesTeamResult=dfpar.at[len(dfpar)-1,'last5teamResults']
    
    
    #calcul le TRJ moyen du dataframe
    moyTrj=float(dfpar['Trj%'].sum())/len(dfpar)
    #on fait la moyenne de la cote equipe
    moycotequi=float(dfpar['CoteResultat'].sum())/len(dfpar)
    #date du matche le plus récent
    DateListe=dfpar['Date'].tolist()
    
    #on calclul le nbre de matchs
    nbrmatch=len(dfpar)
    
    
    ### on calcul les ROI sans le match en question des 10 derniers matchs prec / 5 derniers matches prec / 3 derniers matches prec / 
    ### pour cela on va pour chaque ligne , balayer les lignes suivantes et sommer les PNL puis divisoer par un facteur 
    
    
    
    
    
    
    
    #prepare le dataframe résultat
    resultatdf={'DateListe':[DateListe],'Saison':[saison],'Equipe':[equipe],'TRJmoy':[moyTrj],'ROI':[ROI],'Nbrdematchs': [nbrmatch],'MoyCoteResultat':[moycotequi],'ROI-10J':[ROImoin10J],'ROI-5J':[ROImoin5J],'ROI-3J':[ROImoin3J],'ROI-2J':[ROImoin2J],'ROIJJ-1':[ROImoin1JJ],'ROIJ':[ROIJ],'CoteJ':[CoteJ],'CoteInvJ':[CoteInv],'last5teamResults':[last5matchesTeamResult]}
    
    #on sort la liste des saisons du dataframe
    liSai=dfpar['Saison'].tolist()
    
    liSai=list(set(liSai))
    #le tuple du resultat dataframe et liste saison
    tupRes=(pd.DataFrame(resultatdf),liSai)
    
    #renvoie le dataframe avec le nom de lequipe le trj moyen et le roi
    
    # =========================
    # Colonnes du DataFrame retourné par analysedf(...)[0]
    #
    # - DateListe : liste des dates des matchs analysés
    # - Saison : saison (⚠️ correspond à la dernière valeur parcourue)
    # - Equipe : équipe analysée
    # - TRJmoy : taux de retour joueur moyen
    # - ROI : rentabilité globale (Return On Investment)
    # - Nbrdematchs : nombre total de matchs analysés
    # - MoyCoteResultat : cote moyenne du pari choisi
    #
    # --- ROI dynamiques (forme récente) ---
    # - ROI-10J : ROI sur les 10 derniers matchs
    # - ROI-5J : ROI sur les 5 derniers matchs
    # - ROI-3J : ROI sur les 3 derniers matchs
    # - ROI-2J : ROI sur les 2 derniers matchs
    # - ROIJJ-1 : ROI match courant + match précédent
    # - ROIJ : ROI du match courant uniquement
    #
    # --- Infos cotes ---
    # - CoteJ : cote du pari sur le match courant
    # - CoteInvJ : cote calculé du pari inverse (marché opposé)
    #
    # =========================
    
    return(tupRes)
    

