import { useDataStore } from "@/store/useDataStore";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

type Season = { code: string };

const SEASONS: Season[] = [
  { code: "2024/2025" },
  { code: "2023/2024" },
];

const TEAMS: string[] = ["Marseille", "Lyon"];

export function TableFiltersCard() {
  const selectedSeason = useDataStore((s) => s.selectedSeason);
  const setSelectedSeason = useDataStore((s) => s.setSelectedSeason);

  const selectedTeam = useDataStore((s) => s.selectedTeam);
  const setSelectedTeam = useDataStore((s) => s.setSelectedTeam);

  return (
    <div className="flex flex-wrap gap-2 rounded-xl border px-4 py-3">

      <Select value={selectedSeason ?? ""} onValueChange={(code) => setSelectedSeason(code)} >
        <SelectTrigger className="w-[160px]">
          <SelectValue placeholder="Season" />
        </SelectTrigger>
        {/* permet de mettre la direction vers le bas du select*/}
        <SelectContent position="popper" side="bottom" className="w-[160px]">  
          <SelectGroup>
            {SEASONS.map((s) => (
              <SelectItem key={s.code} value={s.code} >
                {s.code}
              </SelectItem>
            ))}
          </SelectGroup>
        </SelectContent>
      </Select>

      <Select value={selectedTeam ?? ""} onValueChange={(team) => setSelectedTeam(team)}>
        <SelectTrigger className="w-[160px]">
          <SelectValue placeholder="Team" />
        </SelectTrigger>
        {/* permet de mettre la direction vers le bas du select*/}
        <SelectContent position="popper" side="bottom" className="w-[160px]">  
          <SelectGroup>
            {TEAMS.map((t) => (
              <SelectItem key={t} value={t}>
                {t}
              </SelectItem>
            ))}
          </SelectGroup>
        </SelectContent>
      </Select>

    </div>
  );
}