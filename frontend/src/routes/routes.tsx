import ChatPage from "@/modules/chat";
import { createBrowserRouter } from "react-router-dom";

export const router = createBrowserRouter([
  { path: "/", element: <ChatPage /> },
]);
