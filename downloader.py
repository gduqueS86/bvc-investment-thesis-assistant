import os
import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime

print("=== BVC Investment Thesis Assistant - Modo Abierto ===\n")
print(f"Inicio: {datetime.now()}\n")

os.makedirs("pdfs", exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def descargar_pdf(url, empresa, periodo):
    carpeta = os.path.join("pdfs", empresa.upper().replace(" ", "_"))
    os.makedirs(carpeta, exist_ok=True)
    filename = f"{empresa.upper()}_{periodo}.pdf"
    filepath = os.path.join(carpeta, filename)
    
    print(f"⬇️  Descargando: {empresa} - {periodo}")
    try:
        r = requests.get(url, headers=headers, timeout=90)
        if r.status_code == 200 and len(r.content) > 100000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✅ ¡DESCARGADO! → {filename} ({len(r.content)/1024/1024:.1f} MB)\n")
            return True
        else:
            print(f"❌ Error o archivo pequeño ({r.status_code})\n")
            return False
    except Exception as e:
        print(f"❌ Error: {e}\n")
        return False


def buscar_en_pagina_inversionistas(empresa, periodo):
    """Intenta buscar PDF en página de inversionistas conocida"""
    print(f"🔍 Buscando en página de inversionistas de {empresa}...")
    
    urls_paginas = {
        "MINEROS": "https://www.mineros.com.co/es-co/inversionistas/informes-financieros",
        "ECOPETROL": "https://www.ecopetrol.com.co/wps/portal/Home/es/Inversionistas/InformacionFinanciera/Estadosfinancieros",
        "BANCOLOMBIA": "https://www.grupobancolombia.com/inversionistas/informacion-financiera/estados-financieros"
    }
    
    if empresa in urls_paginas:
        try:
            r = requests.get(urls_paginas[empresa], headers=headers, timeout=30)
            soup = BeautifulSoup(r.text, 'html.parser')
            links = soup.find_all('a', href=True)
            
            for link in links:
                href = link['href']
                if any(ext in href.lower() for ext in ['.pdf']) and periodo.lower() in href.lower():
                    if not href.startswith('http'):
                        href = "https://www.mineros.com.co" + href if empresa == "MINEROS" else href
                    print(f"   Enlace encontrado: {href}")
                    descargar_pdf(href, empresa, periodo)
                    return True
        except Exception as e:
            print(f"   Error buscando en página: {e}")
    return False


if __name__ == "__main__":
    empresa = sys.argv[1].upper() if len(sys.argv) > 1 else "MINEROS"
    periodos = sys.argv[2:] if len(sys.argv) > 2 else ["1T2026"]

    print(f"Empresa: {empresa}")
    print(f"Períodos solicitados: {periodos}\n")

    for periodo in periodos:
        # Primero intenta con enlaces conocidos
        # ... (puedes mantener el diccionario de enlaces si quieres)
        encontrado = buscar_en_pagina_inversionistas(empresa, periodo)
        
        if not encontrado:
            print(f"⚠️ No encontré enlace automático para {empresa} - {periodo}")
            print("   Puedes darme el enlace directo y lo agrego.\n")

    print("✅ Proceso terminado.")