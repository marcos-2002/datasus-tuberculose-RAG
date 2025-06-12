import { Button } from "@/components/ui/button"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Separator } from "@/components/ui/separator"
import {
    TrendingUp,
    MapPin,
    BarChart3,
    Calendar,
    Globe,
    Users,
} from "lucide-react"

const LeftSideBar = () => {
    return (
        <div className="w-64 bg-white border-r border-gray-100 mt-14">
            <ScrollArea className="h-full">
                <div className="p-4">
                    {/* Recent Research */}
                    <div className="mb-5">
                        <h3 className="text-xs font-medium text-gray-700 mb-2 uppercase tracking-wider">Pesquisas Recentes</h3>
                        <div className="space-y-1">
                            <Button
                                variant="ghost"
                                size="sm"
                                className="w-full justify-start text-gray-500 hover:text-gray-200 font-normal text-sm h-8"
                            >
                                <TrendingUp className="w-4 h-4 mr-3 text-gray-400" />
                                Análise de Casos 2023
                            </Button>
                            <Button
                                variant="ghost"
                                size="sm"
                                className="w-full justify-start text-gray-500 hover:text-gray-200 font-normal text-sm h-8"
                            >
                                <MapPin className="w-4 h-4 mr-3 text-blue-500" />
                                Distribuição Geográfica
                            </Button>
                            <Button
                                variant="ghost"
                                size="sm"
                                className="w-full justify-start text-gray-500 hover:text-gray-200 font-normal text-sm h-8"
                            >
                                <BarChart3 className="w-4 h-4 mr-3 text-gray-400" />
                                Fatores de Risco
                            </Button>
                        </div>
                    </div>

                    <Separator className="my-3" />

                    {/* Research Filters */}
                    <div>
                        <h3 className="text-xs font-medium text-gray-700 mb-2 uppercase tracking-wider">Filtros de Pesquisa</h3>
                        <div className="space-y-1">
                            <Button
                                variant="ghost"
                                size="sm"
                                className="w-full justify-start text-gray-500 hover:text-gray-200 font-normal text-sm h-8"
                            >
                                <Calendar className="w-4 h-4 mr-3 text-gray-400" />
                                Período de Análise
                            </Button>
                            <Button
                                variant="ghost"
                                size="sm"
                                className="w-full justify-start text-gray-500 hover:text-gray-200 font-normal text-sm h-8"
                            >
                                <Globe className="w-4 h-4 mr-3 text-gray-400" />
                                Região Geográfica
                            </Button>
                            <Button
                                variant="ghost"
                                size="sm"
                                className="w-full justify-start text-gray-500 hover:text-gray-200 font-normal text-sm h-8"
                            >
                                <Users className="w-4 h-4 mr-3 text-gray-400" />
                                Faixa Etária
                            </Button>
                            {/* <Button
                                variant="ghost"
                                size="sm"
                                className="w-full justify-start text-gray-500 hover:text-gray-200 font-normal text-sm h-8"
                            >
                                <Activity className="w-4 h-4 mr-3 text-gray-400" />
                                Tipo de Tuberculose
                            </Button> */}
                        </div>
                    </div>
                </div>
            </ScrollArea>
        </div>
    )
}

export default LeftSideBar