import { useQuery } from "@tanstack/react-query";
import { getMatches } from "@/api/matches";
import {  GetMatchesParams } from "@/Interfaces&Types";


//une créée une fonction hook qui s'apelle useMatches pour fetcher les matches 

//ce hook va agir dans nos composants comme un state , quand quelque chose bouge il va rerender le component
export const useMatches = (params: GetMatchesParams) =>

  useQuery({
    queryKey: ["matchesDetails", params], //la clé qui permettera de stocker les data dans le cache (une variable en locale) , et params l'objet getParams 
    //si params change la query se lance
    queryFn: () => getMatches(params), //la fonction axios qui sera lancé avec notre params
  });

