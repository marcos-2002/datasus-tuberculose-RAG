"use client"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import {
    Settings,
    Paperclip,
    BarChart,
    Share,
    Send,
    Users,
    Loader2,
} from "lucide-react"
import LeftSideBar from "./components/leftSideBar"
import Header from "./components/header"
import { useEffect, useRef, useState } from "react"
import axios from 'axios'
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import ReactMarkdown from 'react-markdown'

type Message = {
    content: string,
    position: 'R' | 'L',
    date: string,
    sql?: string | null,
}

export default function ChatPage() {
    const baseURL = import.meta.env.VITE_API_URL

    const [messages, setMessages] = useState<Message[]>([
        {
            content: "Bem-vindo ao Epi Research. Como posso ajudar em sua pesquisa epidemiológica hoje?",
            position: 'L',
            date: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        }
    ])
    const [inputValue, setInputValue] = useState("")
    const [loading, setLoading] = useState(false)
    const [selectedSQL, setSelectedSQL] = useState<string | null>(null)

    const messagesEndRef = useRef<HTMLDivElement>(null)

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
    }

    useEffect(() => {
        scrollToBottom()
    }, [messages])

    const sendMessage = async () => {
        if (!inputValue.trim()) return

        const userMessage: Message = {
            content: inputValue,
            position: 'R',
            date: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        }

        setMessages(prev => [...prev, userMessage])
        setInputValue("")
        setLoading(true)

        try {
            const response = await axios.post(`${baseURL}/chat-message`, { question: inputValue })
            const newMessage: Message = {
                content: response.data.answer,
                position: 'L',
                date: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
                sql: response.data.sql && response.data.sql != "" ? response.data.sql : null
            }
            console.log(response.data)
            setMessages(prev => [...prev, newMessage])
        } catch (e) {
            console.error("Erro ao enviar mensagem:", e)
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="flex h-screen bg-gray-50/50">
            <Header />
            <LeftSideBar />

            <div className="flex-1 flex flex-col mt-14">
                <div className="bg-white border-b border-gray-100 p-5">
                    <h2 className="text-lg font-medium text-gray-800">Assistente de Pesquisa Epidemiológica</h2>
                    <p className="text-sm text-gray-500">Especializado em Tuberculose</p>
                </div>

                <ScrollArea className="flex-1 p-5">
                    <div className="space-y-4 max-w-4xl">
                        {messages.map((msg, idx) => (
                            <div key={idx} className={`flex items-start space-x-3 ${msg.position === 'R' ? 'justify-end' : ''}`}>
                                {msg.position === 'L' && (
                                    <div className="w-7 h-7 bg-blue-600 rounded-full flex items-center justify-center flex-shrink-0">
                                        <Settings className="w-3.5 h-3.5 text-white" />
                                    </div>
                                )}
                                <div className={`${msg.position === 'R' ? 'bg-blue-600 text-white' : 'bg-blue-50 text-gray-800'} rounded-lg p-3 max-w-2xl`}>
                                    <div className="prose prose-sm max-w-none">
                                        <ReactMarkdown>{msg.content}</ReactMarkdown>
                                    </div>
                                    <span className={`text-xs mt-1 block ${msg.position === 'R' ? 'text-blue-200' : 'text-gray-400'}`}>{msg.date}</span>
                                </div>
                                {msg.position === 'R' && (
                                    <div className="w-7 h-7 bg-gray-200 rounded-full flex items-center justify-center flex-shrink-0">
                                        <Users className="w-3.5 h-3.5 text-gray-500" />
                                    </div>
                                )}
                                {msg.sql && msg.position === 'L' && (
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
                </ScrollArea>

                <div className="bg-white border-t border-gray-100 p-5">
                    <div className="flex items-center space-x-2 mb-3">
                        <Input
                            placeholder="Digite sua pergunta ou comando..."
                            className="flex-1 text-sm"
                            value={inputValue}
                            onChange={e => setInputValue(e.target.value)}
                            onKeyDown={e => {
                                if (e.key === 'Enter') sendMessage()
                            }}
                            disabled={loading}
                        />
                        <Button
                            size="sm"
                            className="bg-blue-600 hover:bg-blue-700"
                            onClick={sendMessage}
                            disabled={loading}
                        >
                            {loading ? <Loader2 className="animate-spin w-4 h-4" /> : <Send className="w-4 h-4 mr-1" />}
                            {!loading && "Enviar"}
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
            {/* <RightSideBar /> */}

        </div>
    )
}
