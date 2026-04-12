import { ColumnDef } from "@tanstack/react-table";
import { createColumns } from "./columns"
import { DataTable } from "./data-table"
import { useDataStore } from "@/store/useDataStore";
import { matchDetails, MergedMatchesAndStats, statDetails } from "@/Interfaces&Types";
import { useMatches } from "@/hooks/useMatches";
import { useMemo } from "react";
import { useStats } from "@/hooks/useStats";



export default function MatchesTable() {


  //avant de render du composant on cree le schema columns adapté  à l'équipe actuellement selectionnée
  //ansi on utilise bien le state actuel lors du rendre de la table 
  // et donc la table connait l'équipe selectionnée
  const selectedTeam: string = useDataStore((s) => s.selectedTeam);
  const selectedSeason: string = useDataStore((s) => s.selectedSeason);

  //on crée un objet params qui ne sera redifinie uniquement si il est différent a cahqe rerender , 
  const Memoparams = useMemo(() => ({
    team: selectedTeam, //state team issu de la tablefiterCard
    season: selectedSeason, // state season issu de la tablefilter Card
  }), [selectedTeam, selectedSeason]);

  // récupération des matchs depuis le hook-api
  const { data: matches, isLoading:isLoadingMatches } = useMatches(Memoparams);
  const { data: stats, isLoading: isLoadingStats } = useStats(Memoparams);
  
  let mergedDatas;

  if (Boolean(matches && stats)){
    mergedDatas=matches?.map(match =>{

    //on obtient les stats du jour du match en question de l'equipe en question 
    const joinedStat=stats?.find(s=>s.dateInt===match.dateInt) as statDetails //entre les deux fetchs ont join chaque match a ses stats de la requete stats team season par la dateInt

    //on fusionne les deux objets pour un return qu'un:

    return{
      ...match,
      last5Results:joinedStat.last5Results,
      last5ROI:joinedStat.last5ROI
    }
  }) as MergedMatchesAndStats[];
  console.log("tables mergées")
  
  } else {
    mergedDatas=matches as MergedMatchesAndStats[];
  } 

  console.log(mergedDatas)
  const columns: ColumnDef<MergedMatchesAndStats>[] = createColumns(selectedTeam);


  return (
    <div>
      {/* affichage conditionnel */}
      {(isLoadingMatches||isLoadingStats) ? (
        <p>Loading matches...</p>
      ) : (
        <DataTable columns={columns} data={mergedDatas || []} />
      )}
    </div>
  )
}