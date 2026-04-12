import { GetMatchesParams, matchDetails, MatchesResponse } from "@/Interfaces&Types";
import axios from "axios";

const api = axios.create({ baseURL: "http://localhost:3000" });

export const getMatches = async (
  params: GetMatchesParams,
): Promise<matchDetails[]> => {
  
  // Supprime les clés avec valeurs null / undefined / ""
  const filteredParams = Object.fromEntries(
    Object.entries(params).filter(([_, value]) => value !== undefined && value !== "")
  );
  
  //on met les filtered params
  const res = await api.get<MatchesResponse>("/matches", { params:filteredParams });

  console.log(await res)
  const convertedRes :matchDetails[] =
  res.data.data.map((m) => {
    const homeScore = m.FTHG;
    const awayScore = m.FTAG;

    //on calcule ici automatiquement le resultat de notre equippe si il y a un team dans nos params
    let teamResult: "W" | "L" | "D" | undefined = undefined;
    if (params.team) {
      if (params.team === m.HomeTeam) {
        teamResult =
          m.FTR === "H" ? "W" : "L";
      } else if (params.team === m.AwayTeam) {
        teamResult =
          m.FTR === "A" ? "W" : "L";
      }
    }

    return{
      id: m.id,
      date: m.Date,
      dateInt:m.DateInt,
      homeTeam: m.HomeTeam,
      awayTeam: m.AwayTeam,
      homeScore,
      awayScore,
      teamResult,
      fullTimeResult:m.FTR,
      odds: {
        home: Number(m.B365H),
        draw: Number(m.B365D),
        away: Number(m.B365A),
      },
    };

  });
  //enf of map 

  console.log(convertedRes);

  return convertedRes



};