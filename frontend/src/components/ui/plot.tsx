import * as Plot from "@observablehq/plot";
import PlotFigure from "./PlotFigure";
import { useEffect, useState } from "react";

interface Dado {
  dimensoes: Record<string, string | number>;
  valor: number;
}

interface PlotGenericProps {
  tipo: string;
  dados: Dado[];
}

export default function PlotGeneric({ tipo, dados }: PlotGenericProps) {
  const [brasil, setBrasil] = useState<any>(null);

  // 🔹 Busca do mapa do Brasil (necessário para coropléticos)
  useEffect(() => {
    if (tipo === "mapas_coropleticos") {
      fetch(
        "https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/refs/heads/main/geojson/br_states.json"
      )
        .then((res) => res.json())
        .then((data) => setBrasil(data))
        .catch((error) => console.error("Erro ao carregar mapa:", error));
    }
  }, [tipo]);

  // 🔹 Prepara os dados em formato genérico
  const dadosFormatados = dados.map((d) => ({
    ...d.dimensoes,
    valor: d.valor,
  }));

  // 🔹 Identifica dimensões
  const dimensoes = Object.keys(dados[0]?.dimensoes || {});
  const primeiraDim = dimensoes[0];
  const segundaDim = dimensoes[1];

  // 🔹 Função que renderiza o gráfico de acordo com o tipo
  const renderPlot = () => {
    switch (tipo) {
      case "grafico_barras_horizontal":
        return (
          <PlotFigure
            options={{
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
            }}
          />
        );

      case "grafico_barras_vertical":
        return (
          <PlotFigure
            options={{
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
            }}
          />
        );

      case "grafico_linhas":
        return (
          <PlotFigure
            options={{
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
            }}
          />
        );

      case "mapas_coropleticos":
        if (!brasil) return <p>Carregando mapa...</p>;
        return (
          <PlotFigure
            options={{
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
                  fill: (feature: any) => {
                    const estado = feature.properties.Estado;
                    return dados.find(
                      (d) => Object.values(d.dimensoes)[0] === estado
                    )?.valor;
                  },
                  stroke: "lightgray",
                }),
              ],
            }}
          />
        );

      case "graficos_com_proporcao":
        return (
          <PlotFigure
            options={{
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
            }}
          />
        );

      default:
        return <p>Tipo de gráfico não suportado.</p>;
    }
  };

  return <>{renderPlot()}</>;
}
