import os
import yaml
import requests
import sys
from datetime import datetime

print("=== BVC Investment Thesis Assistant - Selector de Empresa y Período ===\n")
print(f"Inicio: {datetime.now()}\n")

os.makedirs("pdfs", exist_ok=True)
os.makedirs("data", exist_ok=True)

with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def descargar_pdf(url, empresa, periodo):
    carpeta = os.path.join("pdfs", empresa.upper())
    os.makedirs(carpeta, exist_ok=True)
    filename = f"{empresa.upper()}_{periodo}.pdf"
    filepath = os.path.join(carpeta, filename)
    
    print(f"⬇️  Descargando: {empresa} - {periodo}")
    try:
        r = requests.get(url, headers=headers, timeout=60)
        if r.status_code == 200 and len(r.content) > 100000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✅ ¡ÉXITO! → {filename} ({len(r.content)/1024/1024:.1f} MB)")
            return True
        else:
            print(f"❌ Error ({r.status_code})")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    # Leer parámetros (empresa y período)
    empresa = "ECOPETROL"
    periodo = "1T2026"
    
    if len(sys.argv) > 1:
        empresa = sys.argv[1].upper()
    if len(sys.argv) > 2:
        periodo = sys.argv[2]

    print(f"Empresa seleccionada: {empresa}")
    print(f"Período seleccionado: {periodo}\n")

    # ==================== ENLACES REALES ====================
    if empresa == "ECOPETROL":
        if periodo == "1T2026":
            url = "https://files.ecopetrol.com.co/web/esp/inversionista/reporte-1t-2026.pdf"
        elif periodo == "2T2025":
            url = "https://files.ecopetrol.com.co/web/esp/inversionista/reporte-2t-2025.pdf"  # cambia según existan
        else:
            url = "https://files.ecopetrol.com.co/web/esp/inversionista/reporte-1t-2026.pdf"
        
        descargar_pdf(url, empresa, periodo)
    
    else:
        print(f"⚠️  Aún no tengo enlaces configurados para {empresa}")
        print("Agrega más empresas en el código.")

    print("\n✅ Proceso finalizado.")