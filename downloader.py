import os
import yaml
import requests
import time
from datetime import datetime

print("=== BVC Investment Thesis Assistant - Downloader v2 ===\n")
print(f"Inicio: {datetime.now()}\n")

# Crear carpetas
os.makedirs("pdfs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Cargar config
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def descargar_pdf(url, filename):
    filepath = os.path.join("pdfs", filename)
    print(f"Descargando: {filename}")
    try:
        r = requests.get(url, headers=headers, timeout=60)
        if r.status_code == 200 and len(r.content) > 50000:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"✅ Descargado correctamente ({len(r.content)/1024/1024:.1f} MB)")
            return True
        else:
            print(f"❌ Archivo vacío o error ({r.status_code})")
            return False
    except Exception as e:
        print(f"❌ Error descargando: {e}")
        return False


if __name__ == "__main__":
    print("Buscando reportes recientes...\n")
    
    # Ejemplo de enlaces directos (vamos a mejorar esto)
    # Por ahora probamos con un enlace público conocido de prueba
    test_url = "https://www.superfinanciera.gov.co/SIMEV2/InformacionRelevante"
    print("Por ahora solo mostramos enlaces. La descarga automática completa de SIMEV es compleja.")
    
    for empresa in config.get('watchlist', []):
        print(f"\n🔍 Empresa: {empresa}")
        search_url = f"https://www.superfinanciera.gov.co/SIMEV2/?s={empresa}"
        print(f"   Busca aquí: {search_url}")
        print("   → Abre el enlace y descarga manualmente los PDFs más recientes por ahora")
    
    print("\n📁 Los PDFs se guardarán en la carpeta 'pdfs/'")
    print("✅ Workflow terminado.")