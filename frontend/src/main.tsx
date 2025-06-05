import { createRoot } from "react-dom/client";
import "./globals.css";
import React from "react";
import { RouterProvider } from "react-router-dom";
import { router } from "./routes/routes.tsx"; 
import { Toaster } from "./components/ui/toaster.tsx";

createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
      <RouterProvider router={router} />
      <Toaster /> 
  </React.StrictMode>
);

