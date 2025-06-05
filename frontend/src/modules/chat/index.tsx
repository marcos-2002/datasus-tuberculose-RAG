import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Separator } from "@/components/ui/separator"
import {
  Settings,
  Search,
  FileText,
  HelpCircle,
  TrendingUp,
  MapPin,
  BarChart3,
  Calendar,
  Globe,
  Users,
  Activity,
  Database,
  BookOpen,
  FileBarChart,
  PieChart,
  Eye,
  Download,
  Paperclip,
  BarChart,
  Share,
  Send,
} from "lucide-react"

export default function ChatPage() {
  return (
    <div className="flex h-screen bg-gray-50/50">
      {/* Header */}
      <div className="fixed top-0 left-0 right-0 z-10 bg-white border-b border-gray-100">
        <div className="flex items-center justify-between px-5 py-2">
          <div className="flex items-center space-x-3">
            <div className="w-7 h-7 bg-blue-600 rounded-lg flex items-center justify-center">
              <Settings className="w-4 h-4 text-white" />
            </div>
            <div>
              <h1 className="text-base font-semibold text-gray-800">EpiTB Research</h1>
              <p className="text-xs text-gray-500">Sistema de Pesquisa Epidemiológica</p>
            </div>
          </div>
          <nav className="flex items-center space-x-6">
            <Button variant="ghost" size="sm" className="text-gray-500 font-normal">
              <Settings className="w-4 h-4 mr-2" />
              Painel
            </Button>
            <Button variant="ghost" size="sm" className="text-gray-500 font-normal">
              <Search className="w-4 h-4 mr-2" />
              Pesquisas
            </Button>
            <Button variant="ghost" size="sm" className="text-gray-500 font-normal">
              <FileText className="w-4 h-4 mr-2" />
              Documentação
            </Button>
            <Button variant="ghost" size="sm" className="text-gray-500 font-normal">
              <HelpCircle className="w-4 h-4 mr-2" />
              Suporte
            </Button>
          </nav>
        </div>
      </div>

      {/* Left Sidebar */}
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
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <TrendingUp className="w-4 h-4 mr-3 text-gray-400" />
                  Análise de Casos 2023
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-blue-600 hover:text-blue-700 font-normal text-sm h-8"
                >
                  <MapPin className="w-4 h-4 mr-3 text-blue-500" />
                  Distribuição Geográfica
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
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
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <Calendar className="w-4 h-4 mr-3 text-gray-400" />
                  Período de Análise
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <Globe className="w-4 h-4 mr-3 text-gray-400" />
                  Região Geográfica
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <Users className="w-4 h-4 mr-3 text-gray-400" />
                  Faixa Etária
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <Activity className="w-4 h-4 mr-3 text-gray-400" />
                  Tipo de Tuberculose
                </Button>
              </div>
            </div>
          </div>
        </ScrollArea>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col mt-14">
        {/* Chat Header */}
        <div className="bg-white border-b border-gray-100 p-5">
          <h2 className="text-lg font-medium text-gray-800">Assistente de Pesquisa Epidemiológica</h2>
          <p className="text-sm text-gray-500">Especializado em Tuberculose</p>
        </div>

        {/* Chat Messages */}
        <ScrollArea className="flex-1 p-5">
          <div className="space-y-4 max-w-4xl">
            <div className="flex items-start space-x-3">
              <div className="w-7 h-7 bg-blue-600 rounded-full flex items-center justify-center flex-shrink-0">
                <Settings className="w-3.5 h-3.5 text-white" />
              </div>
              <div className="bg-blue-50 rounded-lg p-3 max-w-2xl">
                <p className="text-gray-800 text-sm">
                  Bem-vindo ao EpiTB Research. Como posso ajudar em sua pesquisa epidemiológica hoje?
                </p>
                <span className="text-xs text-gray-400 mt-1 block">09:41</span>
              </div>
            </div>

            <div className="flex items-start space-x-3 justify-end">
              <div className="bg-blue-600 text-white rounded-lg p-3 max-w-2xl">
                <p className="text-sm">Quais são as tendências de casos de TB nos últimos 5 anos?</p>
                <span className="text-xs text-blue-200 mt-1 block">09:42</span>
              </div>
              <div className="w-7 h-7 bg-gray-200 rounded-full flex items-center justify-center flex-shrink-0">
                <Users className="w-3.5 h-3.5 text-gray-500" />
              </div>
            </div>
          </div>
        </ScrollArea>

        {/* Chat Input */}
        <div className="bg-white border-t border-gray-100 p-5">
          <div className="flex items-center space-x-2 mb-3">
            <Input placeholder="Digite sua pergunta ou comando..." className="flex-1 text-sm" />
            <Button size="sm" className="bg-blue-600 hover:bg-blue-700">
              <Send className="w-4 h-4 mr-1" />
              Enviar
            </Button>
          </div>

          <div className="flex items-center space-x-3">
            <Button variant="ghost" size="sm" className="text-gray-500 font-normal text-xs">
              <Paperclip className="w-3.5 h-3.5 mr-1.5" />
              Anexar Dados
            </Button>
            <Button variant="ghost" size="sm" className="text-gray-500 font-normal text-xs">
              <BarChart className="w-3.5 h-3.5 mr-1.5" />
              Inserir Gráfico
            </Button>
            <Button variant="ghost" size="sm" className="text-gray-500 font-normal text-xs">
              <Share className="w-3.5 h-3.5 mr-1.5" />
              Exportar Conversa
            </Button>
          </div>
        </div>
      </div>

      {/* Right Sidebar */}
      <div className="w-64 bg-white border-l border-gray-100 mt-14">
        <ScrollArea className="h-full">
          <div className="p-4">
            {/* Related Resources */}
            <div className="mb-5">
              <h3 className="text-xs font-medium text-gray-700 mb-2 uppercase tracking-wider">Recursos Relacionados</h3>
              <div className="space-y-1">
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <Database className="w-4 h-4 mr-3 text-gray-400" />
                  Base de Dados OMS
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <BookOpen className="w-4 h-4 mr-3 text-gray-400" />
                  Protocolos de Pesquisa
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <FileBarChart className="w-4 h-4 mr-3 text-gray-400" />
                  Artigos Relacionados
                </Button>
              </div>
            </div>

            <Separator className="my-3" />

            {/* Analysis Tools */}
            <div>
              <h3 className="text-xs font-medium text-gray-700 mb-2 uppercase tracking-wider">
                Ferramentas de Análise
              </h3>
              <div className="space-y-1">
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <PieChart className="w-4 h-4 mr-3 text-gray-400" />
                  Análise Estatística
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <Eye className="w-4 h-4 mr-3 text-gray-400" />
                  Visualização de Dados
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  className="w-full justify-start text-gray-500 hover:text-gray-800 font-normal text-sm h-8"
                >
                  <Download className="w-4 h-4 mr-3 text-gray-400" />
                  Exportar Relatório
                </Button>
              </div>
            </div>
          </div>
        </ScrollArea>
      </div>
    </div>
  )
}
