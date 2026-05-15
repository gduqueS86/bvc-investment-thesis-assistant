import os
import yaml
import requests
import time
from datetime import datetime
from tqdm import tqdm

print("=== BVC Investment Thesis Assistant - Downloader Mejorado ===\n")
print(f"Inicio: {datetime.now()}\n")

# Crear carpetas
os.makedirs("pdfs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Cargar configuración
try:
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    print("✅ Configuración cargada")
except Exception as e:
    print(f"Error con config: {e}")
    config = {"watchlist": ["ECOPETROL", "BANCOLOMBIA"]}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def descargar_archivo(url, filepath):
    """Descarga un archivo PDF"""
    try:
        print(f"   Descargando: {filepath}")
        r = requests.get(url, headers=headers, timeout=60)
        if r.status_code == 200 and len(r.content) > 10000:  # mínimo tamaño
            with open(filepath, 'wb') as f:
                f.write(r.content)
            print(f"   ✅ Descargado ({len(r.content)/1024/1024:.1f} MB)")
            return True
        else:
            print(f"   ❌ Error o archivo vacío ({r.status_code})")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def buscar_informacion_relevante():
    """Busca reportes recientes en la página pública de Información Relevante"""
    print("🔍 Buscando reportes recientes en SIMEV (Información Relevante)...")
    url = "https://www.superfinanciera.gov.co/SIMEV2/informacionrelevantegeneral"
    
    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 200:
            print("   ✅ Conexión exitosa a SIMEV")
            print("   Nota: Por ahora mostramos la página. En próximas versiones extraeremos enlaces 'DESCARGAR'")
            # Aquí en el futuro usaremos BeautifulSoup para extraer links
        else:
            print(f"   Error {r.status_code}")
    except Exception as e:
        print(f"   Error accediendo a SIMEV: {e}")

if __name__ == "__main__":
    buscar_informacion_relevante()
    
    print("\n" + "="*50)
    print("Empresas en watchlist:")
    for empresa in config.get('watchlist', []):
        print(f"→ {empresa}")
        # En versiones futuras aquí buscaremos PDFs específicos por empresa
        time.sleep(2)
    
    print("\n✅ Descarga básica completada.")
    print("Próximo paso: Extraer enlaces directos de PDFs automáticamente.")