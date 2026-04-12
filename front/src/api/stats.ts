import { GetStatsParams, statDetails, StatsResponse } from "@/Interfaces&Types";
import axios from "axios";

const api = axios.create({ baseURL: "http://localhost:3000" });

export const getStats = async (
  params: GetStatsParams,
): Promise<statDetails[]> => {

  // l'objet est censé recevoir un un params avec season et team sinon la requete ne marchera pas dans le serveur

  //on met les filtered params
  const res = await api.get<StatsResponse>("/stats", { params });

  console.log(await res)
  const convertedRes: statDetails[] =
    res.data.data.map((s) => {

      return {
        id: s.id,
        dateInt: s.DateInt,
        team: s.Team,
        last5Results: s.Last5Results,
        last5ROI: s.Last5Results?s.ROI_5D:null,
      }})
  //enf of map 

  console.log(convertedRes);

  return convertedRes



};