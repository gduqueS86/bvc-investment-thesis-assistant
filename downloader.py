import os
import sys
import requests
from datetime import datetime

print("=== BVC Investment Thesis Assistant - Múltiples Períodos ===\n")
print(f"Inicio: {datetime.now()}\n")

os.makedirs("pdfs", exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def descargar_pdf(url, empresa, periodo):
    carpeta = os.path.join("pdfs", empresa.upper().replace(" ", "_"))
    os.makedirs(carpeta, exist_ok=True)
    filename = f"{empresa.upper()}_{periodo}.pdf"   # Nombre limpio
    filepath = os.path.join(carpeta, filename)
    
    print(f"⬇️  {empresa} - {periodo}")
    try:
        r = requests.get(url, headers=headers, timeout=90)
        print(f"   HTTP: {r.status_code} | Tamaño: {len(r.content)/1024/1024:.2f} MB")
        
        if r.status_code == 200 and len(r.content) > 100000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✅ DESCARGADO → {filename}\n")
            return True
        else:
            print(f"❌ Falló (archivo pequeño o error)\n")
            return False
    except Exception as e:
        print(f"❌ Error: {e}\n")
        return False


if __name__ == "__main__":
    empresa = sys.argv[1].upper() if len(sys.argv) > 1 else "ECOPETROL"
    periodos = sys.argv[2:] if len(sys.argv) > 2 else ["1T2026"]

    print(f"Empresa: {empresa}")
    print(f"Períodos solicitados: {periodos}\n")

    # Base de enlaces (agregamos más según necesites)
    enlaces = {
        "ECOPETROL": {
            "1T2026": "https://files.ecopetrol.com.co/web/esp/inversionista/reporte-1t-2026.pdf",
            # Agrega aquí más si tienes enlaces directos
        },
        "MINEROS": {
            "1T2026": "https://cdn.prod.website-files.com/66c623b1be3c82e1f1d2c520/69fca2fc3300d2c7927432f3_Q1%202026%20EE.FF%20Separado%20(CO-882463)%20final%20(48231).pdf"
        }
    }

    for periodo in periodos:
        if empresa in enlaces and periodo in enlaces[empresa]:
            url = enlaces[empresa][periodo]
            descargar_pdf(url, empresa, periodo)
        else:
            print(f"⚠️ No tengo enlace para {empresa} - {periodo}")
            print("   Busca el enlace directo en la página de inversionistas y agrégalo.\n")

    print("✅ Proceso completo.")