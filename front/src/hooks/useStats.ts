import { useQuery } from "@tanstack/react-query";
import { getStats } from "@/api/stats";
import {  GetStatsParams } from "@/Interfaces&Types";


//une créée une fonction hook qui s'apelle useMatches pour fetcher les matches 

//ce hook va agir dans nos composants comme un state , quand quelque chose bouge il va rerender le component
export const useStats = (params: GetStatsParams) =>

  useQuery({
    queryKey: ["statsDetails", params], //la clé qui permettera de stocker les data dans le cache (une variable en locale) , et params l'objet getParams 
    //si params change la query se lance
    queryFn: () => getStats(params), //la fonction axios qui sera lancé avec notre params
    enabled:Boolean(params.team && params.season) //on active le qquery que si les deux params existent
  });

