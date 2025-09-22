import * as Plot from "@observablehq/plot";
import PlotFigure from "./ui/PlotFigure";
import { useState, useEffect } from "react";

interface ModalProps {
  isOpen: boolean
  setIsOpen: React.Dispatch<React.SetStateAction<boolean>>
  json_plot?: JsonVisualizacoes
}

interface Visualizacao {
  tipo: string;
  score: number;
  dados: Dado[];
}

interface Dado {
  dimensoes: Record<string, string | number>; // chave-valor genérico para qualquer dimensão
  valor: number;
}

interface JsonVisualizacoes {
  visualizacoes: Visualizacao[];
}

export default function Modal({ isOpen, setIsOpen, json_plot }: ModalProps) {
  if (!isOpen) return null
  if (!json_plot) {
    console.log("não tem nada no json")
    return null
  }

  const [brasil, setBrasil] = useState({})
  useEffect(() => {
    fetch("https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/refs/heads/main/geojson/br_states.json", {
      method: "GET"
    })
      .then((res) => res.json())
      .then((data) => setBrasil(data))
      .catch((error) => console.log(error))
  }, [])

   const renderPlot = (vis: any) => {
    switch (vis.tipo) {
      case "grafico_barras":
        const dimensao = Object.keys(vis.dados[0].dimensoes)[0]; // pega a chave da dimensão
        const dadosFormatados = vis.dados.map((d: Dado) => ({ ...d.dimensoes, valor: d.valor }));

        return (
          <>
            {/* Barras horizontais */}
            <div className="w-[600px]">
              <PlotFigure
                options={{
                  width: 600,
                  height: 600,
                  marks: [
                    Plot.barX(dadosFormatados, { x: "valor", y: dimensao, fill: "steelblue" })
                  ],
                  x: { grid: true, axis: "both" },
                  marginLeft: 120
                }}
              />
            </div>

            {/* Barras verticais */}
            <div className="w-[600px]">
              <PlotFigure
                options={{
                  width: 600,
                  height: 600,
                  marks: [
                    Plot.barY(dadosFormatados, { x: dimensao, y: "valor", fill: "steelblue" })
                  ],
                  x: { tickRotate: -45 }, // gira os rótulos
                  marginBottom: 100
                }}
              />
            </div>
          </>
        );
      case "grafico_linhas":
        return (
        <PlotFigure
          options={{
            width: 600,
            height: 600,
            marks: [
              Plot.line(vis.dados.map((d: Dado) => ({ ...d.dimensoes, valor: d.valor })), { 
                x: Object.keys(vis.dados[0].dimensoes)[0], 
                y: "valor", 
                stroke: "steelblue" 
              }),
              Plot.dot(vis.dados.map((d: Dado) => ({ ...d.dimensoes, valor: d.valor })), { 
                x: Object.keys(vis.dados[0].dimensoes)[0], 
                y: "valor", 
                fill: "darkblue" 
              })
            ],
            y: { grid: true },
            x: { label: Object.keys(vis.dados[0].dimensoes)[0] },
            margin: 70
          }}
        />
      );
      case "mapas_coropleticos":
         return (
          <PlotFigure
            options={{
              width: 600,
              height: 600,
              axis: null,
              color: {
                type: "quantize",
                scheme: "blues",
                label: "Valor",
                legend: true
              },
              marks: [
                Plot.geo(brasil, { 
                  fill: (elemento: any) => {
                    const estado = elemento.properties.Estado;
                    return vis.dados.find((d: Dado) => Object.values(d.dimensoes)[0] === estado)?.valor;
                  },
                  stroke: "lightgray"
                })
              ]
            }}
          />
        );
      case "graficos_com_proporcao":
        return (
        <PlotFigure
          options={{
            width: 600,
            height: 600,
            x: { label: Object.keys(vis.dados[0].dimensoes)[0] },
            y: { label: "Valor" },
            color: { legend: true },
            marks: [
              Plot.barY(vis.dados.map((d: Dado) => ({ ...d.dimensoes, valor: d.valor })), {
                x: Object.keys(vis.dados[0].dimensoes)[0],
                y: "valor",
                fill: Object.keys(vis.dados[0].dimensoes)[1] || Object.keys(vis.dados[0].dimensoes)[0]
              })
            ]
          }}
        />
      );
      default:
        return null
  }}
 
  console.log(json_plot)

  return (
    <>
      {/* Fundo escuro semi-transparente */}
      <div
        className="fixed inset-0 bg-black/50 z-40"
        onClick={() => setIsOpen(false)} // fecha ao clicar no fundo
      />

      <div className="fixed top-1/2 left-1/2 w-[1271px] max-h-screen -translate-x-1/2 -translate-y-1/2 bg-white z-50 rounded-lg shadow-lg p-4 flex flex-row flex-wrap  gap-6 overflow-y-auto">
      {json_plot?.visualizacoes
        .filter((vis) => vis.score >= 0.8) // 👈 aqui você controla o limite do score
        .map((vis, index) => (
          <div key={index} className="w-[600px]">
            {renderPlot(vis)}
          </div>
        ))}
    </div>
    </>
  )
}
