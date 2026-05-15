import os
import yaml
import requests
import sys
from datetime import datetime

print("=== BVC Investment Thesis Assistant - Diagnóstico Mejorado ===\n")
print(f"Inicio: {datetime.now()}\n")

os.makedirs("pdfs", exist_ok=True)
os.makedirs("data", exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def descargar_pdf(url, empresa, periodo):
    carpeta = os.path.join("pdfs", empresa.upper().replace(" ", "_"))
    os.makedirs(carpeta, exist_ok=True)
    filename = f"{empresa.upper()}_{periodo}.pdf"
    filepath = os.path.join(carpeta, filename)
    
    print(f"⬇️  Intentando: {empresa} - {periodo}")
    print(f"   URL: {url}")
    
    try:
        r = requests.get(url, headers=headers, timeout=90)
        print(f"   Código HTTP: {r.status_code} | Tamaño: {len(r.content)/1024/1024:.2f} MB")
        
        if r.status_code == 200 and len(r.content) > 100000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✅ ¡DESCARGADO CON ÉXITO!")
            print(f"   Archivo guardado: {filepath}")
            return True
        else:
            print(f"❌ Falló (archivo demasiado pequeño o error)")
            return False
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False


if __name__ == "__main__":
    empresa = sys.argv[1].upper() if len(sys.argv) > 1 else "ECOPETROL"
    periodo = sys.argv[2] if len(sys.argv) > 2 else "1T2026"

    print(f"Empresa: {empresa} | Período: {periodo}\n")

    if empresa == "MINEROS":
        url = "https://cdn.prod.website-files.com/66c623b1be3c82e1f1d2c520/69fca2fc3300d2c7927432f3_Q1%202026%20EE.FF%20Separado%20(CO-882463)%20final%20(48231).pdf"
        descargar_pdf(url, empresa, periodo)
    elif empresa == "ECOPETROL":
        url = "https://files.ecopetrol.com.co/web/esp/inversionista/reporte-1t-2026.pdf"
        descargar_pdf(url, empresa, periodo)
    else:
        print(f"⚠️ No tengo enlace preconfigurado para {empresa}")
        print("Agrega el enlace directo en el código.")

    print("\n✅ Fin del proceso.")