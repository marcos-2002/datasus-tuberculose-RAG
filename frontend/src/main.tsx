import { createRoot } from "react-dom/client";
import "./globals.css";
import { RouterProvider } from "react-router-dom";
import { router } from "./routes/routes.tsx"; 
import { Toaster } from "./components/ui/toaster.tsx";

createRoot(document.getElementById("root")!).render(
  <>
      <RouterProvider router={router} />
      <Toaster /> 
  </>
);

