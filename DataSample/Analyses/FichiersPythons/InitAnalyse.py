# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:44:05 2024

@author: asusa
"""
import sys
import os

# chemin absolu du dossier du script courant
current_dir = os.path.dirname(os.path.abspath(__file__))

# on l'ajoute au PYTHONPATH si pas déjà présent
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
#on force le path du crrent directory a celui ci

import AnalyseDfParis
import CompileDataParis
import pandas as pd

"La fonction rentabilité permet d'analyser la performance d'un résultat sur une ou plusieurs saisons et pendant une période plus ou moins spécifique"

def Rentabilite(resultat : str,choix: str, lienDos: str,saison="",debut=0,fin=20500101):
    
    """
    Pour le premier parametre mettre le resultat sur lequel on veut parier => "V","N","D",ou bien des doubles chances "VN" "DN" "VD"
    Cette fonction va renvoyer un tableau avec la rentabilite d'une equipe specifique de ligue 1 ou de toutes ///
    mettre en parametre :"toutesliste" pour afficher la liste des equipes analysables, ou le nom d'une "equipe" ou bien "toutes"
    //// rajouter un parametre saison si besoin exemple "2122" /// on peut rajouter deux dates si on veut analyser une plage de temps spécifique exemple 20240115 et 202240415 
    """

    #on lance compile data qui va nous sortir la liste des tous les clubs présents dans ons données
    if choix=="toutesliste":
        return(CompileDataParis.compiledata(lienDos, choix, saison,debut,fin))
    
    #sinon , si déifférent de "touteslistes" on lance compile data avec comme parametre une equipe specifique
    elif choix!="toutes":
        dfComp=CompileDataParis.compiledata(lienDos, choix, saison,debut,fin)
        
        if type(dfComp)==str:
            return("DFComp Vide")
            
        return(AnalyseDfParis.analysedf(dfComp,resultat,choix, saison))
    
    #si l'utilisateur a taper 'toutes' alors on lance compile data pour chacune des equipe et on compile le resultat dans un gros dataframe
    elif choix=="toutes":
        
        listeclubs=CompileDataParis.compiledata(lienDos, "toutesliste", saison)
        
        #puis on lance une boucle qui va lancer compiledata et analysedfparis pour chaque equipe
        
        for k in range(len(listeclubs)):
            
            
            club=listeclubs[k]
            
            if club==club:
                #dfCompRes va compiler les resultats de la compile et de l'analyse de chacune des equipes
                dfCompClub=CompileDataParis.compiledata(lienDos, club, saison,debut,fin)
                
                if dfCompClub=="DFComp Vide":
                    return("DFComp Vide")
                
                dfResClub=AnalyseDfParis.analysedf(dfCompClub,resultat,club, saison)[0]
                
                if k==0:
                    dfRes=dfResClub
                else:
                    dfRes=pd.concat([dfRes,dfResClub],ignore_index=True, sort=False)
            else:
                pass
            
            dfRes=dfRes.sort_values('ROI')
                
    print("ROI moy : ",float(dfRes["ROI"].sum()/len(dfRes)))
    return(dfRes)
    
    ########################################################################""
    
    "La fonction Evolrentabilite va permettre de tracer au fur et à mesure de la saison la rentabilité d'une équipe"
    #on va utiliser la fonction rentabilite que l'on va compiler sur plusieurs dates différentes 
    #on ne prendra pas en compte de critère de date on regardera l'évolution de la rentabilité uniquement sur une seule saison
    

def EvolRentabilite(resultat : str,choix: str, lienDos: str,saison="",debut=20180101,fin=20251009):
        
        
    #on désactive les prints qui n'apportent rien 


    import pandas as pd
    
        
    # On démarre l'analyse
    
    #on affecte le résultat de Rentabilite à la variable 
    #on construit une boucle qui va prendre toutes les dates entre debut et fin 
    
    jour=fin
    dfResEvol="evol vide"
    limatches=[]

    
    #on fait une boucle qui commence par la dernière date et qui va aller jusqu'à la date initiale
    
    for jour in range(fin,debut,-1):
        
        #si on a la liste des matches obtenues à l'étape plus bas , alors on va éviter d'analyse les dates où il n'y a pas de matches 
        if limatches!=[]:
            if jour not in limatches:
                continue
        
        dfRes=Rentabilite(resultat, choix, lienDos,saison,debut,jour)
        
        
        if type(dfRes)==tuple:
            
            dfRes=dfRes[0]
     

            
            if type(dfResEvol)==str:
                #on est dans le cas on on obtient le premier tableau de resultats
           
                #on va extraire la liste des dates des matchs 
     
                limatches=dfRes.at[0,'DateListe']
                dfRes.at[0,'DateListe']=max(dfRes.at[0,'DateListe']) 
                #on initialise dfResEvol en supprimant la colonne
                dfResEvol=dfRes
                
                
            else:
                
                #a chaque fois on garde dans Date liste la date du match le plus récent sorti par DfRes
                dfRes.at[0,'DateListe']=max(dfRes.at[0,'DateListe'])              
                frames=[dfResEvol, dfRes]
                dfResEvol= pd.concat(frames, sort=False,ignore_index=True)
             
            #a chaque fin d'itération on on garde uniquement la date du match le plus récent sorti par DfRes
    
    
    #on corrige si les deux premières lignes sont identiques 

    if dfResEvol.at[0,'DateListe']==dfResEvol.at[1,'DateListe']:

        dfResEvol=dfResEvol.drop(0)
    
    
    
    return(dfResEvol)

    
def MultiEvolRenta(resultat : str,multiequi : list ,choix1equi: str, lienDos: str,saison="",debut=20180101,fin=20251009):
    
    #si dans choix on a "toutesliste" on renvoie la liste de toutes les equipes de la saison
    
    import CompileDataParis
    import pandas as pd
    import DataframeToCsvToExplorer as tocsv
    
    
    #on definit la liste de toutes les equipes potentiellement analyssable sur les saisons selectionnées 
    Ttsequi=CompileDataParis.compiledata(lienDos, "toutesliste", saison)
    print(Ttsequi)
    
    #si dans choix on a "toutesliste" on renvoie la liste de toutes les equipes de la saison

    if choix1equi=="toutesliste":
        return(Ttsequi)
    
    
    elif len(multiequi)>0:
        listefinale=[]
        
        for k in multiequi :
            if k in Ttsequi:
                listefinale.append(k)
        print(listefinale)
        
        #une fois la liste des clubs validé on compile les analyses EvolRenta pours ces clubs 
        

        for j in range(len(listefinale)):
            print(j)
            dfEvolRenta=EvolRentabilite(resultat,listefinale[j],lienDos,saison,debut,fin)
            print("en cours")
            if j ==0:
                dfmultirenta=dfEvolRenta

            else:
                frames=[dfmultirenta, dfEvolRenta]
                dfmultirenta= pd.concat(frames, sort=False,ignore_index=True)

        tocsv.export_df_to_csv(dfmultirenta,r"C:\Users\kulekci antoine\Documents\DATA","export16h101104")
        return(dfmultirenta)
    
  
    else:
        if len(choix1equi)>1:

            if Ttsequi.count(choix1equi)>0:
                #lequipe en question est bien présente dans dons données on fait l'analyse
                
                dfmultirenta=EvolRentabilite(resultat,choix1equi,lienDos,saison,debut,fin)
                tocsv.export_df_to_csv(dfmultirenta,r"C:\Users\kulekci antoine\Documents\DATA","export14h031104")
                return(dfmultirenta)
    
        else:
            return("rien dans equipe")
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    