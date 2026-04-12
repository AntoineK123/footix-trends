"use client"
import { MergedMatchesAndStats } from "@/Interfaces&Types";
import { ColumnDef } from "@tanstack/react-table"

export const createColumns = (selectedTeam: string | null): ColumnDef<MergedMatchesAndStats>[] => [
    {
        accessorKey: "Date",
        header: "Date",
        size: 50,
        cell: ({ row }) => {
            const dateStr = row.original.date as string;
            const date = new Date(dateStr); // sécurisé
            console.log(dateStr)
            console.log(date)
            return date.toLocaleDateString('fr-FR', {
                day: '2-digit',
                month: '2-digit'
            }).replace('/', '.');
        },
    },
    {
        id: "matchResult",
        header: "Final Time Score",
        cell: ({ row }) => {
            const rowData = row.original;
            let scoreColor = ""; //empty text color by default

            if (rowData.teamResult && rowData.fullTimeResult !== "D") { //on a selectionne une equipe et son score n'est pas match nul
                rowData.teamResult === "W" ? scoreColor = "text-green-700" : scoreColor = "text-red-600"
            }

            return (
                <div className="grid grid-cols-[1fr_auto_1fr] max-w-[300px] min-w-[220px] gap-2 text-center">
                    <span className={
                        selectedTeam === rowData.homeTeam ? "font-bold" : ""}>
                        {rowData.homeTeam}
                    </span>

                    <span className={"font-bold " + scoreColor}>{`${rowData.homeScore} - ${rowData.awayScore}`}</span>

                    <span className={selectedTeam === rowData.awayTeam ? "font-bold" : ""}>
                        {rowData.awayTeam}
                    </span>
                </div>
            );
        }
    },
    {
        id: "teamTrend5",
        header: "5 Derniers résultats",
        cell: ({ row }) => { return (<span className="">{row.original.last5Results ? row.original.last5Results : ""}</span>)}
    },
    {
        accessorKey: "teamResult",
        header: "Résultat du pari : L'équipe gagne",
        cell: ({ row }) => {
            return (
                <span className={`${row.original.teamResult === "W" ? "text-green-700" : "text-red-600"}`}>
                    {row.original.teamResult === "W" ? "V" : row.original.teamResult === "L" ? "D" : ""}
                </span>
            )
        }
    },
    {
        id: "teamROI5",
        header: "Last 5 matches ROI",
        cell: ({ row }) => {
            if (!row.original.last5ROI && row.original.last5ROI!==0 ) {
                return ""
            } else {
                const deltaPercentage:number=Number(((row.original.last5ROI*100)-100).toFixed(0));
                const symbol:string=row.original.last5ROI<1?"":"+"
                return (<span className={`${symbol===""?"text-red-600":"text-green-600"}`}>{symbol+deltaPercentage+"%"}</span>)
            }
        }
    }
];