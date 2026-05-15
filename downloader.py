import os
import yaml
import requests
import sys
from datetime import datetime

print("=== BVC Investment Thesis Assistant - Descarga Dinámica ===\n")
print(f"Inicio: {datetime.now()}\n")

os.makedirs("pdfs", exist_ok=True)
os.makedirs("data", exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def descargar_pdf(url, empresa, periodo):
    carpeta = os.path.join("pdfs", empresa.upper().replace(" ", "_"))
    os.makedirs(carpeta, exist_ok=True)
    filename = f"{empresa.upper()}_{periodo}.pdf"
    filepath = os.path.join(carpeta, filename)
    
    print(f"⬇️  Intentando descargar: {empresa} - {periodo}")
    try:
        r = requests.get(url, headers=headers, timeout=60)
        if r.status_code == 200 and len(r.content) > 100000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✅ ¡DESCARGADO CON ÉXITO! → {filename}")
            print(f"   Tamaño: {len(r.content)/1024/1024:.1f} MB")
            return True
        else:
            print(f"❌ Error ({r.status_code}) o archivo muy pequeño")
            return False
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False


if __name__ == "__main__":
    # Leer parámetros desde GitHub Actions o comando
    empresa = sys.argv[1].upper() if len(sys.argv) > 1 else "ECOPETROL"
    periodo = sys.argv[2] if len(sys.argv) > 2 else "1T2026"

    print(f"Empresa solicitada: {empresa}")
    print(f"Período solicitado: {periodo}\n")

    # Base de enlaces conocidos (vamos agregando más)
    urls_conocidas = {
        "ECOPETROL": {
            "1T2026": "https://files.ecopetrol.com.co/web/esp/inversionista/reporte-1t-2026.pdf",
            "2T2025": "https://files.ecopetrol.com.co/web/esp/inversionista/reporte-2t-2025.pdf"
        },
        "MINEROS": {
            "1T2026": "https://cdn.prod.website-files.com/66c623b1be3c82e1f1d2c520/69fca2fc3300d2c7927432f3_Q1%202026%20EE.FF%20Separado%20(CO-882463)%20final%20(48231).pdf"
        },
        "BANCOLOMBIA": {
            # Agrega aquí cuando tengas enlaces directos
        }
    }

    if empresa in urls_conocidas and periodo in urls_conocidas[empresa]:
        url = urls_conocidas[empresa][periodo]
        descargar_pdf(url, empresa, periodo)
    else:
        print(f"⚠️ No tengo enlace directo para {empresa} - {periodo}")
        print("Puedes buscar el enlace directo en el sitio de la empresa o SIMEV y agregarlo al diccionario.")
        print(f"Sugerencia: Busca en https://www.superfinanciera.gov.co/SIMEV2/ o en la página de inversionistas de {empresa}")

    print("\n✅ Proceso finalizado.")