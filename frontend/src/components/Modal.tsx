import * as Plot from "@observablehq/plot";
import PlotFigure from "./ui/PlotFigure";
import { useState, useEffect } from "react";

interface ModalProps {
  showModal: boolean
  setModal: React.Dispatch<React.SetStateAction<boolean>>
  msgContent: string
}



const estadosBR = [
  { "estado": "São Paulo", "casos": 18201 },
  { "estado": "Rio de Janeiro", "casos": 12361 },
  { "estado": "Pernambuco", "casos": 5251 },
  { "estado": "Pará", "casos": 4804 },
  { "estado": "Rio Grande do Sul", "casos": 4729 },
  { "estado": "Bahia", "casos": 4324 },
  { "estado": "Minas Gerais", "casos": 3799 },
  { "estado": "Amazonas", "casos": 3659 },
  { "estado": "Ceará", "casos": 3491 },
  { "estado": "Maranhão", "casos": 2492 },
  { "estado": "Paraná", "casos": 2201 },
  { "estado": "Santa Catarina", "casos": 1937 },
  { "estado": "Rio Grande do Norte", "casos": 1366 },
  { "estado": "Espírito Santo", "casos": 1350 },
  { "estado": "Mato Grosso do Sul", "casos": 1387 },
  { "estado": "Mato Grosso", "casos": 1151 },
  { "estado": "Paraíba", "casos": 1248 },
  { "estado": "Goiás", "casos": 1000 },
  { "estado": "Alagoas", "casos": 939 },
  { "estado": "Sergipe", "casos": 934 },
  { "estado": "Piauí", "casos": 745 },
  { "estado": "Rondônia", "casos": 570 },
  { "estado": "Acre", "casos": 528 },
  { "estado": "Roraima", "casos": 435 },
  { "estado": "Amapá", "casos": 406 },
  { "estado": "Distrito Federal", "casos": 337 },
  { "estado": "Tocantins", "casos": 217 }
]

const tuberculoseMes2021 = [
  { "mes": "Janeiro", "casos": 5333 },
  { "mes": "Fevereiro", "casos": 6205 },
  { "mes": "Março", "casos": 7194 },
  { "mes": "Abril", "casos": 6731 },
  { "mes": "Maio", "casos": 6748 },
  { "mes": "Junho", "casos": 7102 },
  { "mes": "Julho", "casos": 7576 },
  { "mes": "Agosto", "casos": 8241 },
  { "mes": "Setembro", "casos": 8162 },
  { "mes": "Outubro", "casos": 7946 },
  { "mes": "Novembro", "casos": 8159 },
  { "mes": "Dezembro", "casos": 8052 }
]

const tuberculoseMes2021Numerico = tuberculoseMes2021.map((d, i) => ({
  ...d,
  mesNumero: i + 1
}));

const tuberculoseMes2022 = [
  {"mes": "Janeiro", "mesNumero": 1, "casos": 7445},
  {"mes": "Fevereiro", "mesNumero": 2, "casos": 8131},
  {"mes": "Março", "mesNumero": 3, "casos": 9647},
  {"mes": "Abril", "mesNumero": 4, "casos": 8016},
  {"mes": "Maio", "mesNumero": 5, "casos": 9114},
  {"mes": "Junho", "mesNumero": 6, "casos": 8081},
  {"mes": "Julho", "mesNumero": 7, "casos": 8627},
  {"mes": "Agosto", "mesNumero": 8, "casos": 9639},
  {"mes": "Setembro", "mesNumero": 9, "casos": 8726},
  {"mes": "Outubro", "mesNumero": 10, "casos": 8565},
  {"mes": "Novembro", "mesNumero": 11, "casos": 8196},
  {"mes": "Dezembro", "mesNumero": 12, "casos": 8264}
]

const empilhado = [
  {ano: 2022, raca: "Parda", casos: 52682},
  {ano: 2022, raca: "Branca", casos: 26729},
  {ano: 2022, raca: "Preta", casos: 13869},
  {ano: 2022, raca: "Ignorado", casos: 7287},
  {ano: 2022, raca: "Indígena", casos: 943},
  {ano: 2022, raca: "Amarela", casos: 941}
]

export default function Modal({ showModal, setModal, msgContent }: ModalProps) {
  if (!showModal) return null

  const [brasil, setBrasil] = useState({})
  useEffect(() => {
    fetch("https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/refs/heads/main/geojson/br_states.json", {
      method: "GET"
    })
    .then((res) => res.json())
    .then((data) => setBrasil(data))
    .catch((error)=> console.log(error))
  }, [])

  return (
    <>
      {/* Fundo escuro semi-transparente */}
      <div
        className="fixed inset-0 bg-black/50 z-40"
        onClick={() => setModal(false)} // fecha ao clicar no fundo
      />

      {/* Modal centralizado */}
      <div className="fixed top-1/2 left-1/2 w-[1271px] max-h-screen -translate-x-1/2 -translate-y-1/2 bg-white z-50 rounded-lg shadow-lg p-4 flex flex-row flex-wrap items-center gap-6 overflow-y-auto">
      <div className="w-[600px]">
        <PlotFigure
            options={{
              width: 600,
              height: 600,
              marks: [
                Plot.barX(estadosBR, {x: "casos", y: "estado", fill: "steelblue"})
              ],
              x: {grid: true, axis: "both"},
              marginLeft: 120
            }}
        />
        </div>
        <div className="w-[600px]">
          <PlotFigure
              options={{
                width: 600,
                height: 600,
                marks: [
                    Plot.barY(estadosBR, {x: "estado", y: "casos", fill: "steelblue"})
                ],
                x: { tickRotate: -45 }, // gira os rótulos -45 graus
                marginBottom: 100 // aumenta a margem inferior
              }}
          />
        </div>
        <div className="w-[600px]">
          <PlotFigure
              options={{
                width: 600,
                height: 600,
                marks: [
                    Plot.line(tuberculoseMes2021Numerico, {x: "mesNumero", y: "casos", stroke: "steelblue"}),
                    Plot.dot(tuberculoseMes2021Numerico, { x: "mesNumero", y: "casos", fill: "darkblue" })
                ],
                y: {grid: true},
                x: { 
                    tickFormat: (i:number) => tuberculoseMes2021[i - 1]?.mes
                  },
                margin: 70
              }}
          />
        </div>
        <div className="w-[600px]">
          <PlotFigure
              options={{
                width: 600,
                height: 600,
                marks: [
                    Plot.line(tuberculoseMes2021Numerico, {x: "mesNumero", y: "casos", stroke: "steelblue"}),
                    Plot.dot(tuberculoseMes2021Numerico, { x: "mesNumero", y: "casos", fill: "darkblue" }),
                    Plot.line(tuberculoseMes2022, {x: "mesNumero", y: "casos", stroke: "red"}),
                    Plot.dot(tuberculoseMes2022, { x: "mesNumero", y: "casos", fill: "darkred" }),
                ],
                y: {grid: true},
                x: { 
                    tickFormat: (i:number) => tuberculoseMes2021[i - 1]?.mes
                  },
                margin: 70
              }}
          />
        </div>
        <div className="w-[600px] ">
          <PlotFigure
              options={{
                width: 600,
                height: 600,
                axis: null,
                color: {
                  type: "quantize",
                  scheme: "blues",
                  label: "População masculina",
                  legend: true
                },
                marks: [
                  Plot.geo(brasil, {fill: (elemento) => estadosBR.find((e) => e.estado === elemento.properties.Estado)?.casos, stroke: "lightgray"})
                ]
              }}
          />
        </div>
        <div className="w-[600px] ">
          <PlotFigure
              options={{
                x: {label: "Ano"},
                y: {label: "Casos"},
                color: {legend: true},
                marks: [
                  Plot.barY(empilhado, {
                    x: "ano",
                    y: "casos",
                    fill: "raca"
                  })
                ]
              }}
          />
        </div>
      </div>
    </>
  )
}
