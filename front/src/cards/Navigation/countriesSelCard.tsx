import { useNavStore } from "@/store/useNavStore";

import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"


type Country = { code: string; label: string };

const COUNTRIES: Country[] = [
    { code: "fr", label: "France" },
    { code: "en", label: "Angleterre" },
    { code: "es", label: "Espagne" },
    { code: "de", label: "Allemagne" },
    { code: "it", label: "Italie" },
    { code: "be", label: "Belgique" },
    { code: "pt", label: "Portugal" },
    { code: "tr", label: "Turquie" },
];


export function CountrySelCard() {


    const selectedCountry = useNavStore((s) => s.selectedCountry);
    const setSelectedCountry = useNavStore((s) => s.setSelectedCountry);


return (
  <div className="flex flex-wrap md:flex-col gap-2 rounded-xl border px-4 py-3">
    <ToggleGroup 
      type="single" 
      spacing={8} //equivalent du gap entre elements
      value={selectedCountry ?? ""} 
      onValueChange={(code) => {setSelectedCountry(code) }} //radix ajoute automatiquement le data-state-on sur la valeur actuelle selectionnee
      className="flex flex-wrap md:flex-col gap-2 cursor-pointer" //on met le font par defaut 
    >
      {COUNTRIES.map((c) => (
        <ToggleGroupItem
          key={c.code}
          value={c.code}
          className="rounded-xl p-2 data-[state=on]:bg-blue-500 data-[state=on]:text-white cursor-pointer font-normal" //ici si tailwind voit data-state=on dans l'attibut html il va mettre ce qu'il y a apres les ":"
        >
          {c.label}
        </ToggleGroupItem>
      ))}
    </ToggleGroup>
  </div>
)

}
