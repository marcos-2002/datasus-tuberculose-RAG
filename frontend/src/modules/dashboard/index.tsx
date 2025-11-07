"use client"

import { useEffect, useState } from "react"

import { Button } from "@/components/ui/button"

import Header from "./components/header"
import { useNavigate } from "react-router-dom"
import PlotGeneric from "@/components/ui/plot"
import { IoIosInformationCircleOutline } from "react-icons/io";
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
} from "@/components/ui/dialog"

interface Visualizacao {
    tipo: string;
    score: number;
    dados: Dado[];
    pergunta: string;
    titulo: string;
}

interface Dado {
    dimensoes: Record<string, string | number>; // chave-valor genérico para qualquer dimensão
    valor: number;
}

interface JsonVisualizacoes {
    visualizacoes: Visualizacao[];
}

const dashboardDownload = () => {

}

const codeGraph = (typeGraph: string) => {
    switch (typeGraph) {
        case "grafico_barras_horizontal":
            return `
Plot.plot({
    width: 530,
    height: 530,
    marks: [
    Plot.barX(dadosFormatados, {
        x: "valor",
        y: primeiraDim,
        fill: "steelblue",
    }),
    ],
    x: { grid: true },
    marginLeft: 120,
})`

        case "grafico_barras_vertical":
            return `
Plot.plot({
    width: 530,
    height: 530,
    marks: [
    Plot.barY(dadosFormatados, {
        x: primeiraDim,
        y: "valor",
        fill: "steelblue",
    }),
    ],
    x: { tickRotate: -45 },
    marginBottom: 100,
})`

        case "grafico_linhas":
            return `
Plot.plot({
    width: 530,
    height: 530,
    marks: [
    Plot.line(dadosFormatados, {
        x: primeiraDim,
        y: "valor",
        stroke: "steelblue",
    }),
    Plot.dot(dadosFormatados, {
        x: primeiraDim,
        y: "valor",
        fill: "darkblue",
    }),
    ],
    y: { grid: true },
    x: { label: primeiraDim },
    margin: 70,
})`

        case "mapas_coropleticos":
            return `
Plot.plot({
    width: 530,
    height: 530,
    axis: null,
    color: {
        type: "quantize",
        scheme: "blues",
        label: "Valor",
        legend: true,
    },
    marks: [
        Plot.geo(brasil, {
            fill: feature => {
            const estado = feature.properties.Estado;
            return dados.find(
                (d) => Object.values(d.dimensoes)[0] === estado
            )?.valor;
            },
            stroke: "lightgray",
        }),
    ],
})`

        case "graficos_com_proporcao":
            return `
Plot.plot({
    width: 530,
    height: 530,
    x: { label: primeiraDim },
    y: { label: "Valor" },
    color: { legend: true },
    marks: [
    Plot.barY(dadosFormatados, {
        x: primeiraDim,
        y: "valor",
        fill: segundaDim || primeiraDim,
    }),
    ],
})`

        default:
            return `Tipo de gráfico incorreto.`
    }
}

export default function DashboardPage() {
    const [isOpen, setIsOpen] = useState(false)
    const [plotList, setPlotList] = useState<Visualizacao[]>([]);

    const [isDataModalOpen, setIsDataModalOpen] = useState<boolean>(false)
    const [openPlotIndex, setOpenPlotIndex] = useState<number | null>(null)


    const navigate = useNavigate()

    useEffect(() => {
        const plots = localStorage.getItem("plots")
        if (plots !== null) {
            setPlotList(JSON.parse(plots))
        }
    }, [])
    console.log(plotList)

    return (
        <div className="flex h-screen bg-gray-50/50 overflow-hidden">
            <Header />

            <div className="flex-1 flex flex-col mt-14 overflow-hidden">
                {/* Header da conversa */}
                <div className="bg-white border-b border-gray-100 p-5 py-2 shrink-0 flex items-center justify-between">
                    <div>
                        <h2 className="text-lg font-medium text-gray-800">Dashboard de Pesquisa Epidemiológica</h2>
                        <p className="text-sm text-gray-500">Especializado em Tuberculose</p>
                    </div>
                    <div className="flex flex-row gap-4">
                        <Button size="sm" className="bg-gray-300 hover:bg-gray-400 text-blac" onClick={() => navigate('/')}>
                            Chat
                        </Button>
                        {/* Botão para abrir modal com lista de dados disponíveis */}
                        <Button size="sm" className="bg-blue-600 hover:bg-blue-700" onClick={() => dashboardDownload()}>
                            Baixar gráficos
                        </Button>
                    </div>
                </div>
                <div className="overflow-y-auto">
                    <div className="flex mx-5 my-3 gap-10 flex-wrap">
                        {plotList.map((plot, index) => (
                            <div key={index} className="flex gap-4">
                                <div className="bg-white p-2 rounded-xl shadow-[0_4px_10px_rgba(0,0,0,0.07)] w-[530px]">
                                    <p className="font-semibold text-center mt-2 mb-6 text-xl">{plot.titulo}</p>
                                    <PlotGeneric dados={plot.dados} tipo={plot.tipo} />
                                </div>

                                <div
                                    className="cursor-pointer"
                                    onClick={() => setOpenPlotIndex(index)}
                                >
                                    <IoIosInformationCircleOutline size={32} />
                                </div>

                                <Dialog
                                    open={openPlotIndex === index}
                                    onOpenChange={(open) => setOpenPlotIndex(open ? index : null)}
                                >
                                    <DialogContent className="max-w-4xl max-h-[90vh] overflow-y-auto">
                                        <DialogHeader>
                                            <DialogTitle>Informações do gráfico</DialogTitle>
                                            <DialogDescription>
                                                Estas são as informações que foram necessárias para a criação desse gráfico:
                                            </DialogDescription>
                                        </DialogHeader>

                                        <p>A pergunta que gerou esse gráfico foi:</p>
                                        <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                                            {plot.pergunta}
                                        </pre>

                                        <p>Os dados para gerar esse gráfico foram:</p>
                                        <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                                            {`dados = ` + JSON.stringify(plot.dados, null, 2)}
                                        </pre>

                                        <p>O código para gerar esse gráfico foi:</p>
                                        <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                                            {`// importar a biblioteca Plot\n`}
                                            {`import {Plot} from "@observablehq/plot"`}
                                        </pre>
                                        <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                                            {plot.tipo === "mapas_coropleticos" ? `
brasil = (
  await fetch("https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/main/geojson/br_states.json")
    .then(res => res.json())
)
.catch((error) => console.error("Erro ao carregar mapa:", error));` : `
 // 🔹 Prepara os dados em formato genérico
  const dadosFormatados = dados.map((d) => ({
    ...d.dimensoes,
    valor: d.valor,
  }));

  // 🔹 Identifica dimensões
  const dimensoes = Object.keys(dados[0]?.dimensoes || {});
  const primeiraDim = dimensoes[0];
  const segundaDim = dimensoes[1];`}
                                        </pre>
                                        <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                                            {codeGraph(plot.tipo)}
                                        </pre>
                                    </DialogContent>
                                </Dialog>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )
}