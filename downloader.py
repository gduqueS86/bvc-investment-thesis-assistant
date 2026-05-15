import os
import yaml
import requests
import time
from datetime import datetime

print("=== BVC Investment Thesis Assistant - GitHub Actions ===\n")
print(f"Inicio: {datetime.now()}\n")

# Crear carpetas
os.makedirs("pdfs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Cargar configuración
try:
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    print("✅ Configuración cargada correctamente")
    print(f"Empresas en watchlist: {config.get('watchlist', [])}")
except Exception as e:
    print(f"❌ Error cargando config.yaml: {e}")
    config = {"watchlist": ["ECOPETROL", "BANCOLOMBIA"]}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def buscar_reportes(empresa):
    print(f"\n🔍 Buscando reportes para: {empresa}")
    search_url = f"https://www.superfinanciera.gov.co/SIMEV2/?s={empresa.replace(' ', '+')}"
    print(f"🔗 Enlace de búsqueda: {search_url}")
    print("   (Por ahora abre este enlace manualmente desde tu celular o PC)")

if __name__ == "__main__":
    for empresa in config.get('watchlist', []):
        buscar_reportes(empresa)
        time.sleep(3)
    
    print("\n✅ Proceso finalizado (versión básica)")