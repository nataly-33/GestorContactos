import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',        // permite acceder desde fuera del contenedor
    port: 5173,             // puerto por defecto de Vite
    watch: {
      usePolling: true,     // necesario para hot reload en Docker (especialmente en Mac y Windows)
    },
  },
})