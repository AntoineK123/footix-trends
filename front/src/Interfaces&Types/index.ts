
//for get Match query 
export type GetMatchesParams = { team?: string; season?: string }

//for get match query raw result
export type MatchesResponse = {
  data: MatchApi[];
};

//for get match query raw result
export type MatchApi = {
  id: number;
  Div: string;
  Season: string;
  Date: string;
  DateInt: number;
  HomeTeam: string;
  AwayTeam: string;
  FTHG: number;
  FTAG: number;
  FTR: "H" | "D" | "A";
  B365H: string;
  B365D: string;
  B365A: string;
};


// match type for front usage

export type matchDetails  = {
  id: number;
  date: string;
  dateInt:number,
  homeTeam: string;
  awayTeam: string;
  homeScore: number;
  awayScore: number;
  fullTimeResult:"H" | "D" | "A";
  teamResult:string|undefined;
   odds: {
    home: number;
    draw: number;
    away: number;
  };
};


//for get stats query 
export type GetStatsParams = { team?: string; season?: string }


// for get stats queries raw results

export type StatApi = {
  id: number;
  DateInt: number;
  Season: string;
  Team: string;
  AvgTRJ: number;
  ROI: number;
  NbrofMatches: number;
  AverageOddResult: number;
  ROI_10D: number;
  ROI_5D: number;
  ROI_3D: number;
  ROI_2D: number;
  ROIJJ_D: number;
  ROID: number;
  OddD: number;
  InvOddD: number;
  Last5Results: string;
};

//for get stats query raw result
export type StatsResponse = {
  data: StatApi[];
};

export type statDetails = {
  id: number;
  dateInt: number;
  team: string;
  last5Results: string|null;
  last5ROI: number|null;

};

//for combination on matches end stats in TanstackTable: 
export type MergedMatchesAndStats = {
  last5Results?: string;
  last5ROI?: number;
  id: number;
  date: string;
  dateInt: number;
  homeTeam: string;
  awayTeam: string;
  homeScore: number;
  awayScore: number;
  fullTimeResult: "H" | "D" | "A";
  teamResult: string | undefined;
  odds: {
    home: number;
    draw: number;
    away: number;
  };
};