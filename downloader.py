import os
import yaml
from datetime import datetime

print("=== BVC Investment Thesis Assistant - v3 ===\n")
print(f"Inicio: {datetime.now()}\n")

# Crear carpetas visibles
os.makedirs("pdfs", exist_ok=True)
os.makedirs("data", exist_ok=True)
os.makedirs("pdfs/ECOPETROL", exist_ok=True)
os.makedirs("pdfs/BANCOLOMBIA", exist_ok=True)

print("✅ Carpetas creadas:")
print("   - pdfs/")
print("   - data/")
print("   - pdfs/ECOPETROL/")
print("   - pdfs/BANCOLOMBIA/")

# Cargar config
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

print(f"\nEmpresas configuradas: {config.get('watchlist', [])}")
print("\n📌 Próximos pasos:")
print("   1. Descarga manual de PDFs desde SIMEV")
print("   2. Subir los PDFs a la carpeta pdfs/")
print("   3. Automatizar extracción de tablas")

print("\n✅ Workflow terminado correctamente.")