import * as Plot from "@observablehq/plot";
import PlotFigure from "./ui/PlotFigure";

interface ModalProps {
  showModal: boolean
  setModal: React.Dispatch<React.SetStateAction<boolean>>
  msgContent: string
}

function extractBrazilUFData(text: string) {
  const estadosBR = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
    "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí",
    "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
    "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
  ];

  const data: { uf: string; numero: number }[] = [];

  for (const uf of estadosBR) {
    const index = text.indexOf(uf);
    if (index !== -1) {
      const after = text.slice(index + uf.length);
      const numMatch = after.match(/[\d.]+/);
      if (numMatch) {
        data.push({
          uf,
          numero: Number(numMatch[0].replace(/\./g, "")),
        });
      }
    }
  }

  return data;
}






export default function Modal({ showModal, setModal, msgContent }: ModalProps) {
    if (!showModal) return null
    
  return (
    <>
      {/* Fundo escuro semi-transparente */}
      <div
        className="fixed inset-0 bg-black/50 z-40"
        onClick={() => setModal(false)} // fecha ao clicar no fundo
      />

      {/* Modal centralizado */}
      <div className="fixed top-1/2 left-1/2 w-[600px] h-[600px] -translate-x-1/2 -translate-y-1/2 bg-white z-50 rounded-lg shadow-lg p-4 flex flex-col justify-center items-center">
        <PlotFigure
            options={{
            marks: [
                Plot.barY(extractBrazilUFData(msgContent), {x: "uf", y: "numero", fill: "steelblue"})
            ],
            x: { tickRotate: -45 }, // gira os rótulos -45 graus
            marginBottom: 100 // aumenta a margem inferior
            }}
        />
      </div>
    </>
  )
}
