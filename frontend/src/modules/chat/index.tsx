"use client"

import { useEffect, useRef, useState } from "react"
import axios from "axios"
import ReactMarkdown from "react-markdown"
import {
    Settings,
    Send,
    Users,
    Loader2,
} from "lucide-react"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from "@/components/ui/dialog"
import LeftSideBar from "./components/leftSideBar"
import Header from "./components/header"
import { toast } from "@/hooks/use-toast"
import Modal from "@/components/Modal"
import { useNavigate } from "react-router-dom"
import { plot } from "@observablehq/plot"

type Message = {
    content: string
    position: "R" | "L"
    date: string
    sql?: string | null
}

const availableDataList = [
    "Tipo de entrada do paciente",
    "Raça",
    "Sexo",
    "População privada de liberdade",
    "População em situação de rua",
    "Forma clínica da tuberculose",
    "Tuberculose extrapulmonar",
    "Território de cidadania",
    "Coinfecção com AIDS",
    "Alcoolismo",
    "Diabetes",
    "Doença mental",
    "Uso de drogas ilícitas",
    "Tabagismo",
    "Outras doenças associadas",
    "Resultado de raio-x de tórax",
    "Status HIV",
    "Uso de antirretrovirais",
    "Cultura de escarro",
    "Baciloscopia (2 e 6 meses)",
    "Situação de encerramento do caso",
    "Ano de nascimento",
    "Data da notificação",
    "Estado (UF)",
]



export default function ChatPage() {
    const baseURL = import.meta.env.VITE_API_URL

    const navigate = useNavigate()

    const [messages, setMessages] = useState<Message[]>([
        {
            content: `Bem-vindo ao Epi Research! 👋

Sou seu assistente de pesquisa epidemiológica, especializado em dados sobre tuberculose.

Clique no botão "Ver informações disponíveis" para ver quais informações eu tenho disponível para responder.`,
            position: "L",
            date: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
        },
    ])
    const [inputValue, setInputValue] = useState("")
    const [loading, setLoading] = useState(false)
    const [selectedSQL, setSelectedSQL] = useState<string | null>(null)
    const [isDataModalOpen, setIsDataModalOpen] = useState(false)
    const [chatId, setChatId] = useState<string | null>(null);

    const messagesEndRef = useRef<HTMLDivElement | null>(null)

    const scrollToBottom = () => {
        if (messagesEndRef.current) {
            messagesEndRef.current.scrollIntoView({ behavior: "smooth" })
        }
    }

    useEffect(() => {
        getLastMessages()
    }, [])

    useEffect(() => {
        scrollToBottom()
    }, [messages])

    const [jsonPlot, setJsonPlot] = useState('')
    const sendMessage = async () => {
        if (!inputValue.trim()) return

        const userMessage: Message = {
            content: inputValue,
            position: "R",
            date: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
        }

        setMessages((prev) => [...prev, userMessage])
        setInputValue("")
        setLoading(true)

        try {
            const response = await axios.post(`${baseURL}/chat-message`, { question: inputValue, chat_id: chatId })
            
            const newMessage: Message = {
                content: response.data.answer,
                position: "L",
                date: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
                sql: response.data.sql && response.data.sql !== "" ? response.data.sql : null,
            }

            setMessages((prev) => [...prev, newMessage])
            setJsonPlot(
                JSON.stringify({
                    visualizacoes: JSON.parse(response.data?.json_plot).visualizacoes?.map((visualizacao: any) => {
                    return { ...visualizacao, pergunta: inputValue };
                    })
                })
                );

        } catch (e: unknown) {
            console.error("Erro ao enviar mensagem:", e)

            let errorMessage = "Ocorreu um erro inesperado. Tente novamente."

            if (axios.isAxiosError(e)) {
                errorMessage = e.response?.data?.error ?? errorMessage
            }

            toast({
                title: "Erro ao consultar o assistente",
                description: errorMessage,
                variant: "destructive",
            })
        } finally {
            setLoading(false)
        }
    }

    const getLastMessages = async () => {
        let existingId = localStorage.getItem('chat_id');

        if (!existingId) {
            existingId = Math.floor(Math.random() * 1_000_000_000).toString();
            localStorage.setItem("chat_id", existingId);
        }

        setChatId(existingId);

        try {
            const response = await axios.get(`${baseURL}/chat-messages`, {
                params: { chat_id: existingId },
            });

            const loadedMessages: Message[] = response.data.map((msg: any) => ({
                content: msg.content,
                position: msg.position === "R" ? "R" : "L",
                date: new Date(msg.date).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
                sql: msg.sql ?? null
            }));

            setMessages((prev) => [...prev, ...loadedMessages]);
        } catch (error) {
            console.error("Erro ao buscar mensagens anteriores:", error);
            toast({
                title: "Erro ao carregar histórico",
                description: "Não foi possível carregar as mensagens anteriores.",
                variant: "destructive",
            });
        }
    };

    const [isOpen, setIsOpen] = useState(false)
    // console.log(jsonPlot)
    return (
        <div className="flex h-screen bg-gray-50/50 overflow-hidden">
            <Header />
            <LeftSideBar />

            <div className="flex-1 flex flex-col mt-14 md:ml-64 overflow-hidden">
                {/* Header da conversa */}
                <div className="bg-white border-b border-gray-100 p-4 md:p-5 shrink-0 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
    
    {/* Texto */}
    <div>
        <h2 className="text-base md:text-lg font-medium text-gray-800">
            Assistente de Pesquisa Epidemiológica
        </h2>
        <p className="text-xs md:text-sm text-gray-500">
            Especializado em Tuberculose
        </p>
    </div>

    {/* Botões */}
    <div className="flex flex-col sm:flex-row gap-2 sm:gap-4 w-full md:w-auto">
        <Button
            size="sm"
            className="bg-blue-600 hover:bg-blue-700 w-full sm:w-auto"
            onClick={() => setIsOpen(true)}
        >
            Ver gráficos
        </Button>

        <Button
            size="sm"
            className="bg-gray-300 hover:bg-gray-400 text-black w-full sm:w-auto"
            onClick={() => navigate('/dashboard')}
        >
            Dashboard
        </Button>

        <Button
            size="sm"
            className="bg-blue-500 hover:bg-blue-700 w-full sm:w-auto"
            onClick={() => setIsDataModalOpen(true)}
        >
            Informações
        </Button>
    </div>
</div>

                {/* Modal lista de dados disponíveis */}
                <Dialog open={isDataModalOpen} onOpenChange={setIsDataModalOpen}>
                    <DialogContent className="max-w-md">
                        <DialogHeader>
                            <DialogTitle>Informações disponíveis para análise</DialogTitle>
                            <DialogDescription>
                                Estas são as informações presentes no banco de dados que você pode perguntar:
                            </DialogDescription>
                        </DialogHeader>
                        <ul className="list-disc list-inside max-h-80 overflow-auto text-sm text-gray-700">
                            {availableDataList.map((item, idx) => (
                                <li key={idx}>{item}</li>
                            ))}
                        </ul>
                    </DialogContent>
                </Dialog>
                
                <Modal isOpen={isOpen} setIsOpen={setIsOpen} json_plot={jsonPlot ? JSON.parse(jsonPlot) : undefined} />

                {/* Mensagens com scroll */}
                <div className="flex-1 overflow-y-auto p-5">
                    <div className="space-y-4 max-w-4xl">
                        {messages.map((msg, idx) => (
                            <div key={idx} className={`flex items-start space-x-3 ${msg.position === "R" ? "justify-end" : ""}`}>
                                {msg.position === "L" && (
                                    <div className="w-7 h-7 bg-blue-600 rounded-full flex items-center justify-center flex-shrink-0">
                                        <Settings className="w-3.5 h-3.5 text-white" />
                                    </div>
                                )}
                                <div
                                    className={`${msg.position === "R" ? "bg-blue-600 text-white" : "bg-blue-50 text-gray-800"
                                        } rounded-lg p-3 max-w-2xl`}
                                >
                                    <div className="prose prose-sm max-w-none">
                                        <ReactMarkdown>{msg.content}</ReactMarkdown>
                                    </div>
                                    <span className={`text-xs mt-1 block ${msg.position === "R" ? "text-blue-200" : "text-gray-400"}`}>
                                        {msg.date}
                                    </span>
                                </div>
                                {msg.position === "R" && (
                                    <div className="w-7 h-7 bg-gray-200 rounded-full flex items-center justify-center flex-shrink-0">
                                        <Users className="w-3.5 h-3.5 text-gray-500" />
                                    </div>
                                )}
                                {msg.sql != null && msg.position === "L" && (
                                    <Dialog>
                                        <DialogTrigger asChild>
                                            <Button
                                                variant="ghost"
                                                className="text-xs mt-2 text-blue-600 hover:underline p-0 h-auto"
                                                onClick={() => setSelectedSQL(msg.sql!)}
                                            >
                                                Detalhes
                                            </Button>
                                        </DialogTrigger>
                                        <DialogContent className="max-w-lg">
                                            <DialogHeader>
                                                <DialogTitle>Consulta SQL utilizada</DialogTitle>
                                                <DialogDescription>
                                                    Para responder essa pergunta, eu executei o seguinte SQL no banco de dados para obter os dados:
                                                </DialogDescription>
                                            </DialogHeader>
                                            <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap break-words max-h-[300px] overflow-auto">
                                                {selectedSQL}
                                            </pre>
                                        </DialogContent>
                                    </Dialog>
                                )}
                            </div>
                        ))}
                        <div ref={messagesEndRef} />
                    </div>
                </div>

                {/* Input e ações */}
                <div className="bg-white border-t border-gray-100 p-5 shrink-0">
                    <div className="flex items-center space-x-2 mb-3">
                        <Input
                            placeholder="Digite sua pergunta ou comando..."
                            className="flex-1 text-sm"
                            value={inputValue}
                            onChange={(e) => setInputValue(e.target.value)}
                            onKeyDown={(e) => {
                                if (e.key === "Enter") sendMessage()
                            }}
                            disabled={loading}
                        />
                        <Button size="sm" className="bg-blue-600 hover:bg-blue-700" onClick={sendMessage} disabled={loading}>
                            {loading ? <Loader2 className="animate-spin w-4 h-4" /> : <Send className="w-4 h-4 mr-1" />}
                            {!loading && "Enviar"}
                        </Button>
                    </div>

                    {/* <div className="flex items-center space-x-3">
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
                    </div> */}
                </div>
            </div>
        </div>
    )
}