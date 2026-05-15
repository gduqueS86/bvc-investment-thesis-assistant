import os
import yaml
import time
from datetime import datetime

print("=== BVC Investment Thesis Assistant ===\n")
print(f"Inicio: {datetime.now()}\n")

# Crear carpetas
os.makedirs("pdfs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Cargar configuración
try:
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    print("✅ Configuración cargada")
    print(f"Empresas: {config.get('watchlist', [])}")
except Exception as e:
    print(f"Error con config: {e}")
    config = {"watchlist": ["ECOPETROL", "BANCOLOMBIA"]}

print("\n🔍 Buscando reportes... (versión básica)\n")

for empresa in config.get('watchlist', []):
    print(f"→ {empresa}")
    search_url = f"https://www.superfinanciera.gov.co/SIMEV2/?s={empresa.replace(' ', '+')}"
    print(f"   Enlace: {search_url}")
    print("   (Abre el enlace manualmente por ahora)\n")
    time.sleep(2)

print("✅ Proceso terminado.")