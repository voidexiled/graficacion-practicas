import http.server
import socketserver

PORT = 8000

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Historia de la Animación por Computadora</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        h1, h2 {
            color: #333;
        }
        .seccion {
            background: white;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        ul {
            list-style: none;
            padding-left: 0;
        }
        li::before {
            content: "• ";
            color: #2a6ebb;
        }
    </style>
</head>
<body>
    <h1>Historia, Evolución y Aplicación de la Animación por Computadora</h1>

    <div class="seccion">
        <h2>📜 Historia</h2>
        <ul>
            <li>1960: Ivan Sutherland crea Sketchpad.</li>
            <li>1982: Disney lanza Tron con gráficos por computadora.</li>
            <li>1995: Pixar revoluciona el cine con Toy Story.</li>
        </ul>
    </div>

    <div class="seccion">
        <h2>📈 Evolución</h2>
        <ul>
            <li>1980–90: Nacimiento del CGI.</li>
            <li>2000–2010: Captura de movimiento, iluminación realista.</li>
            <li>2010+: Inteligencia Artificial, Realidad Virtual, motores 3D.</li>
        </ul>
    </div>

    <div class="seccion">
        <h2>🚀 Aplicaciones</h2>
        <ul>
            <li>Cine y TV: Personajes virtuales, efectos visuales.</li>
            <li>Videojuegos: Mundos 3D y realistas.</li>
            <li>Medicina: Visualización de órganos, simulaciones.</li>
            <li>Educación: Videos didácticos y e-learning.</li>
            <li>Arquitectura: Renderizados y recorridos virtuales.</li>
        </ul>
    </div>
</body>
</html>
"""

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
        else:
            self.send_error(404, "Archivo no encontrado")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Servidor iniciado en http://localhost:{PORT}")
    httpd.serve_forever()
